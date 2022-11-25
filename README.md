# climafeis
Script CLI em Python para scrape do banco de dados climatológicos do [Canal CLIMA](https://clima.feis.unesp.br) da [UNESP Ilha Solteira](https://www.feis.unesp.br/) com a biblioteca [Requests](https://requests.readthedocs.io/en/latest/).  

### Installation
1. Certifique-se que o Python 3.8 ou superior e o pip estejam instalados
1. Rode `pip install climafeis`

### Development
1. Confira sua versão do Python com `python -V`
1. Instale o Python 3.8 ou superior e pip, caso já não estejam instalados:

    - Windows `winget install Python.Python.3.X` (substitua X com a minor version desejada)
    - Ubuntu e derivados `apt install python3 python3-pip`
    - Arch e derivados `pacman -S python python-pip`
    - Fedora `dnf install python3 python3-pip`

1. [Instale o poetry](https://python-poetry.org/docs/#installation) 
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git && cd climafeis`
1. Instale os requisitos `poetry install`

### Output headers
| Header     | Description                                           |
| ---------- | ----------------------------------------------------- |
| Date       | Observation date (dd-mm-yyyy)                         |
| Tmean      | Mean temperature (ºC)                                 |
| Tmax       | Max temperature (ºC)                                  |
| Tmin       | Min temperature (ºC)                                  |
| RHmean     | Mean relative humidity (%)                            |
| RHmax      | Max relative humidity (%)                             |
| RHmin      | Min relative humidity (%)                             |
| Pmean      | Mean pressure (kPa)                                   |
| Rn         | Net radiation (MJ/m^2*day)                            |
| Rl         | Liquid radiation (MJ/m^2*day)                         |
| G          | Soil heat flux (MJ/m^2*day)                           |
| PAR        | (μmoles/m^2)                                          |
| ETcat      | Evapotranspiration Class A Tank (mm/day)              |
| ET0pm      | Reference evapotranspiration Penman–Monteith (mm/day) |
| ET0cat     | Reference evapotranspiration Class A Tank (mm/day)    |
| U2max      | Max windspeed at 2 meters (m/s)                       |
| U2mean     | Mean windspeed at 2 meters (m/s)                      |
| U2dir      | Wind direction at 2 meters (º)                        |
| Rain       | Rainfall (mm)                                         |
| Insolation | Solar insolation (h/day)                              |

### Usage
    usage: climafeis [-h] [-U USER] [-P PW] estacao dataInicial [dataFinal]

    Scrape dados diários do Canal CLIMA (http://clima.feis.unesp.br).

    positional arguments:
        estacao               Nome da estação: ILHA_SOLTEIRA, MARINOPOLIS, JUNQUEIROPOLIS, PARANAPUA,
        IRAPURU, POPULINA, SANTA_ADELIA_PIONEIROS, SANTA_ADELIA, BONANCA, ITAPURA, DRACENA.
        
        dataInicial           Data inicial no formato dd/MM/YYYY (30/05/2020).
        dataFinal             Data final no formato dd/MM/YYYY (03/05/2020). Padrão: presente dia.

    optional arguments:
        -h, --help            show this help message and exit
        -U USER, --user USER  Usuário do Canal CLIMA. Caso seu usuário não esteja em $USER_CLIMAFEIS.
        -P PW, --pw PW        Senha do Canal CLIMA. Caso sua senha não esteja em $PASSWD_CLIMAFEIS.
        
    Examples:
        climafeis ILHA_SOLTEIRA 30/05/2020 03/06/2020             Daily data from ILHA_SOLTEIRA station from 30/05/2020 to 03/05/2020
        
        climafeis MARINOPOLIS 30/05/2020                          Daily data from MARINOPOLIS station from 30/05/2020 to today
        
        climafeis ILHA_SOLTEIRA 30/05/2020 -U user -P password    


