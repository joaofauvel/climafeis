# climafeis
Script CLI em Python para scrape do banco de dados climatológicos do [Canal CLIMA](http://clima.feis.unesp.br) da [UNESP Ilha Solteira](https://www.feis.unesp.br/) com a biblioteca [Requests](https://requests.readthedocs.io/en/latest/).  

### Instalação
1. Certifique-se que o Python 3.8 ou superior e o pip estejam instalados
1. Rode `pip install climafeis`

### Instalação para desenvolvimento
1. Confira sua versão do Python com `python -V`
1. Instale o Python 3.8 ou superior e pip, caso já não estejam instalados:

    - Windows `winget install Python.Python.3.X` (substitua X com a minor version desejada)
    - Ubuntu e derivados `apt install python3 python3-pip`
    - Arch e derivados `pacman -S python python-pip`
    - Fedora `dnf install python3 python3-pip`

1. [Instale o poetry](https://python-poetry.org/docs/#installation) 
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git && cd climafeis`
1. Instale os requisitos `poetry install`

### Utilização
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
        
    Exemplos:
        climafeis ILHA_SOLTEIRA 30/05/2020 03/06/2020             Extraí dados diários da estação de Ilha
        Solteira dos dias 30/05/2020 ao dia 03/05/2020
        
        climafeis MARINOPOLIS 30/05/2020                          Extraí dados diários da estação de
        Marinópolis dos dias 30/05/2020 ao presente dia
        
        climafeis ILHA_SOLTEIRA 30/05/2020 -U usuário -P senha    


