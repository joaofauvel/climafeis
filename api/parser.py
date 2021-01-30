from dataclasses import dataclass
from typing import Callable, NamedTuple, Optional

import lxml.html
import pandas as pd


class Operation(NamedTuple):
    op: str
    frag: str
    r_value: Optional[str] = None
    table_xpath: str = None
    bad_xpaths: list[str] = None
    # TODO: Remove first attribute from operation?


@dataclass
class Operations:
    """Contains the operations which may be performed on the Clima API."""

    realtime = Operation("realtime", "dadostemporeal.php", None)
    hourly = Operation("hourly", "recebe_formulario_60minutos.php", None)
    daily = Operation(
        "daily",
        "recebe_formulario.php",
        "dados_diario",
        "//td[@class='valor_coluna']/ancestor::table",
        [
            "//tr[@style='vnd.ms-excel.numberformat:0.0_)']",
            "//tr[count(.//td[@class='valor_coluna']) = 0]/"
            "preceding-sibling::tr[1]/following-sibling::tr",
            "//td[last()]",
        ],
    )
    monthly = Operation("monthly", "recebe_formulario.php", "dados_medios")
    compare_daily = Operation(
        "compare_daily", "recebe_formulario.php", "dadosestacao"
    )

    # TODO: Implement iteration (do dataclasses have them already implemented?)
    #  and appending methods.
    # TODO: Delete the dataclass and leave the operations in the 'root' scope?
    #   Create a new file operation.py?


class Parser:
    """Parses the response into a `pd.DataFrame`.

    :param response: raw response.
    :param operation: parses the response from an operation.
    """

    def __init__(self, response: str, operation: Operation):
        self.response = response
        self.operation = operation

    def _cleanup(self, table):
        # lxml.html.xpath() always return a list
        for bad in self.operation.bad_xpaths:
            elem = table.xpath(bad)
            if elem is None:
                continue
            elif isinstance(elem, list):
                for elem in table.xpath(bad):
                    elem.drop_tree()
            else:
                elem.drop_tree()

    def realtime(self) -> pd.DataFrame:
        pass

    def hourly(self) -> pd.DataFrame:
        pass

    def daily(self) -> pd.DataFrame:
        # lxml.html.xpath() always return a list
        tree = lxml.html.fromstring(self.response)
        table = tree.xpath(self.operation.table_xpath)[0]
        self._cleanup(table)
        return pd.read_html(table)[0]

    def monthly(self) -> pd.DataFrame:
        pass

    # TODO: Implement the other parsers.


def parse(
    text_reponse, operation: Operation = None, parser: Callable = None, *args
):
    # TODO: Access Operations as a dictionary and allow str operation to be
    #  passed
    if parser is not None:
        return parser(text_reponse, args)
    _parser = Parser(text_reponse, operation)
    operation = operation.op
    if operation is None and parser is None:
        raise ValueError("operation cannot be None when parser is None.")
    if operation == "realtime":
        return _parser.realtime()
    elif operation == "hourly":
        return _parser.hourly()
    elif operation == "daily":
        return _parser.daily()
    elif operation == "monthly":
        return _parser.monthly()
