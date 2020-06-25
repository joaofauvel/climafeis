# climafeis
Script CLI em Python para scrape do banco de dados climatológicos do [Canal CLIMA](http://clima.feis.unesp.br) da [UNESP Ilha Solteira](https://www.feis.unesp.br/) com a biblioteca [Requests](https://2.python-requests.org/en/master/).  

### Configuração no Windows
1. Confira sua versão do Python em uma shell (Powershell ou CMD) com `python -V`
1. Instale o [Python 3.4](https://www.python.org/downloads/windows/) ou superior, caso já não esteja instalado
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git` ou [baixe o repositório](https://github.com/joaofauvel/climafeis/archive/master.zip) e extraia o conteúdo do arquivo master.zip 
1. Abra o diretório `climafeis`, recem extraído, que contém os arquivos `climascraper.py` e `requirements.txt`
1. Instale os requisitos `pip install -r --user requirements.txt`

### Configuração em uma distribuição GNU/Linux
1. Confira sua versão do Python com `python -V`
1. Instale o Python 3.4 ou superior e pip, caso já não estejam instalados:  

    - Ubuntu e derivados `apt install python3 python3-pip`
    - Arch e derivados `pacman -S python python-pip`
    - Fedora `dnf install python3 python3-pip`  
    
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git && cd climafeis`
1. Instale os requisitos `pip install --user -r requirements.txt`

### Utilização
    usage: climascraper.py [-h] [-U USER] [-P PW] estacao dataInicial [dataFinal]

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
        climascraper.py ILHA_SOLTEIRA 30/05/2020 03/06/2020             Extraí dados diários da estação de Ilha
        Solteira dos dias 30/05/2020 ao dia 03/05/2020
        
        climascraper.py MARINOPOLIS 30/05/2020                          Extraí dados diários da estação de
        Marinópolis dos dias 30/05/2020 ao presente dia
        
        climascraper.py ILHA_SOLTEIRA 30/05/2020 -U usuário -P senha    
#
Alternativamente, é recomendado a instalação dos requisitos em um ambiente virtual do Python, como [venv](https://docs.python.org/3/library/venv.html) ou [virtualenv](https://virtualenv.pypa.io/en/stable/).


