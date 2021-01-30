import datetime as dt
from enum import Enum
from typing import Callable, NewType, Optional, TypeVar, Union
from urllib.parse import urljoin

import requests

from .parser import Operation, Operations, parse

Fmt = NewType("Fmt", str)
DT = TypeVar("DT", dt.datetime, dt.date)
TupleSpan = NewType("TupleSpan", tuple[DT, Optional[DT]])


class Station(Enum):
    """Station codes for requesting data from the website."""

    ILHA_SOLTEIRA = 1
    MARINOPOLIS = 2
    JUNQUEIROPOLIS = 3
    PARANAPUA = 4
    IRAPURU = 9
    POPULINA = 10
    SANTA_ADELIA_PIONEIROS = 11
    SANTA_ADELIA = 12
    BONANCA = 13
    ITAPURA = 14
    DRACENA = 19


# TODO: Encapsulate some data from dadostemporeal.php or lat, long, etc?


class HalfSpan:
    def __init__(self, datetime: DT):
        if isinstance(datetime, dt.date):
            self.datetime = dt.datetime.combine(datetime, dt.time())
        else:
            self.datetime = datetime

    @property
    def date(self):
        return self.datetime.date()

    @property
    def time(self):
        return self.datetime.time()

    def fmt_date(self, fmt: str = "%d/%m/%Y"):
        return self.date.strftime(fmt)

    def fmt_time(self, fmt: str = "%H:%m"):
        return self.date.strftime(fmt)


class DatetimeSpan:
    """An object that represents an initial and an end date(time) -- a span.
    Implements a few methods to make easier working with this modal of datetime.

    :param initial: initial (older) date(time). If a dt.date is passed,
        then it is combined with a time of dt.time(0, 0).
    :param final: final (more recent) date(time). If a dt.date is passed,
        then it is combined with a time of dt.time(0, 0). Default is
        datetime.datetime.now()
    """

    # TODO: class wide fmt string?
    # :param fmt: format of date and time of the given date(times):
    #     (date_fmt, time_fmt). Default is %d/%m/%Y and %H:%m

    def __init__(
        self,
        initial: Union[DT, HalfSpan],
        final: Union[DT, HalfSpan] = None,
    ):

        if isinstance(initial, HalfSpan):
            self.initial = initial
        else:
            self.initial = HalfSpan(initial)
        if isinstance(final, HalfSpan):
            self.final = final
        elif isinstance(final, (dt.datetime, dt.date)):
            self.final = HalfSpan(final)
        if final is None:
            self.final = HalfSpan(dt.datetime.now())

        self.delta: dt.timedelta = final.datetime - initial.datetime

    @staticmethod
    def from_tuple(datetime_span_tuple: tuple[DT, DT]) -> __init__:
        return DatetimeSpan(
            initial=datetime_span_tuple[0], final=datetime_span_tuple[1]
        )

    # TODO: Check if initial date(time) is older than final?


class Clima:
    """API for clima.feis.unesp.br

    :param user: username registered.
    :param passwd: password registered.
    :param st: station name or a Station object.
    :param dt_span: span of date(times) to use for fetching data. First
        date(time) is inclusive, last is exclusive.
    """

    base_url = "http://clima.feis.unesp.br/"
    login = "valida.php"
    attrs = {
        "T_mean": "tempmedia",
        "T_max": "tempmaxima",
        "T_min": "tempminima",
        "RH_mean": "umrmedia",
        "RH_max": "umrmaxima",
        "RH_min": "umrminima",
        "P_mean": "pressaoatm",
        "R_s": "radiacaoglobal",
        "R_n": "radiacaoliquida",
        "G": "fluxocalor",
        "par": "par",
        "ET_tca": "ettca",
        "ETo_pm": "etopm",
        "ETo_tca": "etotca",
        "U_max": "velocidadeventomaxima",
        "U_mean": "velocidadevento",
        "U_dir": "direcaovento",
        "rain": "chuva",
        "sunlight": "insolacao",
    }

    def __init__(
        self,
        user: str,
        passwd: str,
        st: Union[str, Station] = None,
        dt_span: Union[TupleSpan, DatetimeSpan] = None,
    ):

        if isinstance(dt_span, tuple):
            self.dt_span = DatetimeSpan.from_tuple(dt_span)
        else:
            self.dt_span = dt_span
        if dt_span.delta < dt.timedelta(0):
            raise ValueError("Timedelta in dt_span must not be negative.")

        if isinstance(st, str):
            self.st = Station[st]
        else:
            self.st = st.value

        self.user = user
        self.passwd = passwd

    @property
    def session(self) -> requests.Session:
        """Session of the site.

        :return: requests.Session object.
        """

        login_url = urljoin(Clima.base_url, Clima.login)
        payload = {
            "usuario": self.user,
            "senha": self.passwd,
            "enviar": "Enviar",
        }
        s = requests.Session()
        s.post(login_url, data=payload)

        return s

    def realtime(self):
        pass

    def hourly(self):
        """Hourly data in span.

        :return: the response in bytes if less than or equal to 1 day in
            span, that is DatetimeSpan.delta.days less than or equal to 1.
            Else, a list of bytes (for now, I will change this behavior).
        """

        if self.dt_span is None or self.st is None:
            raise TypeError(
                "Neither dt_span or st attributes can be None when "
                "accessing Clima.hourly"
            )

        # r.text?
        return [r.content for r in self._exec_request(Operations.hourly)]

    def daily(self, parser: Callable = None, *args):
        """Daily data in span.

        :return: the response in bytes.
        """

        if self.dt_span is None or self.st is None:
            raise TypeError(
                "Neither dt_span or st attributes can be None when "
                "accessing Clima.daily"
            )
        raw = self._exec_request(Operations.daily).text
        return parse(raw, Operations.daily, parser, args)

    def monthly(self):
        """Monthly data in span.

        :return: the response in bytes.
        """

        if self.dt_span is None or self.st is None:
            raise TypeError(
                "Neither dt_span or st attributes can be None when "
                "accessing Clima.monthly"
            )
        # r.text?
        return self._exec_request(Operations.monthly).content

    def compare_daily(self, attr):
        """Daily data in span of all stations for a given attribute.
        See `Clima.attrs`.

        :return: the response in bytes.
        """

        if self.dt_span is None:
            raise TypeError(
                "dt_span attribute cannot be None when accessing "
                "Clima.compare_daily()"
            )

        # r.text?
        return self._exec_request(Operations.compare_daily, attr).content

    def _exec_request(
        self, operation: Operation, attr: str = None
    ) -> Union[requests.Response, list[requests.Response]]:
        """Executes a request.

        :return: a response or list of responses if operation == "hourly"
        """

        fetch_url = urljoin(Clima.base_url, operation.frag)
        if operation.op == "hourly":
            return [
                self.session.post(fetch_url, payload)
                for payload in self._hourly_compat_payload()
            ]
        payload = self._prepare_payload(
            operation.op, self.dt_span, operation.r_value, attr
        )
        return self.session.post(fetch_url, payload)

    def _hourly_compat_payload(self, span: DatetimeSpan = None) -> dict:
        """Yields a daily (hourly operation compatible) payload for post
        request. These payloads are exclusively for fetching hourly data.

        Initial and final times are preserved: if initial datetime is
        2020-12-31 15:00, a payload from 15:00 to 23:00 of that day is returned.
        If final datetime is 2020-01-01 19:00 a payload from 00:00 to 19:00 of
        that day is returned. If initial and final times are 23:00 and 00:00
        respectively, a payload from 23:00 to 23:00 or 00:00 to 00:00
        for the day is returned. For every other case a payload from 00:00 to
        23:00 is returned.

        :return: payload dict.
        """
        if span is None:
            span = self.dt_span
        baseline = span.initial.date
        for d in range(span.delta.days):
            #: end of baseline day
            eod = dt.datetime.combine(baseline, dt.time(23))
            if d == 1:
                #: payload span
                pl_span = DatetimeSpan(self.dt_span.initial, eod)
            elif d == self.dt_span.delta.days - 1:
                pl_span = DatetimeSpan(baseline, self.dt_span.final)
            else:
                pl_span = DatetimeSpan(baseline, eod)
            payload = self._prepare_payload("hourly", pl_span, None, None)
            baseline += dt.timedelta(d)
            yield payload

    def _prepare_payload(
        self,
        op: str,
        span: DatetimeSpan,
        daily_r_value: Optional[str],
        attr: Optional[str],
    ) -> dict:
        """Prepares an operation compatible payload for post request.

        :param op: operation of the payload.
        :param span: date(time) span of the payload.
        :param daily_r_value: daily request value of the payload.
        :param attr: specifies an attribute for the fetch operation.
        :return: payload dict.
        :raise ValueError: if span.delta.days exceeds 1 and op == "hourly"
        """
        payload = {
            "requireddataini": span.initial.fmt_date(),
            "requireddatafim": span.final.fmt_date(),
            "estacao": self.st.value,
            "enviar": "Enviar",
        }
        if op == "daily" or op == "monthly" or op == "compare_daily":
            payload["RadioGroup1"] = daily_r_value
        elif op == "hourly":
            if span.delta.days > 1:
                raise ValueError(
                    "span timedelta (span.delta.days) cannot "
                    "exceed 1 when preparing an hourly payload."
                )
            payload["horarioini"] = span.initial.fmt_time()
            payload["horariofim"] = span.final.fmt_time()
        if op == "compare_daily" and attr is not None:
            payload["var"] = Clima.attrs[attr]
            # Raise exception if attr is not specified when preparing a
            # compare_daily payload

        return payload

    # TODO: Implement method for 5 minute data and altering the database.
    # TODO: Implement methods for retrieving real-time data
    #   http://clima.feis.unesp.br/dadostemporeal.php
    # TODO: Generic method for retrieving data
