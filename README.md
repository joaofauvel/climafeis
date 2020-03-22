# climafeis
Demo de uma interface em Python para a consulta de dados climatológicos do banco de dados do [Canal CLIMA](http://clima.feis.unesp.br) da [UNESP Ilha Solteira](https://www.feis.unesp.br/) com a biblioteca [Selenium](https://selenium-python.readthedocs.io/).  

#
### Configuração no Windows
1. Confira sua versão do Python em uma shell (Powershell ou CMD) com `python -V`
1. Instale o [Python 3.4](https://www.python.org/downloads/windows/) ou superior, caso já não esteja instalado
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git` ou baixe o [repositório](https://github.com/joaofauvel/climafeis/archive/master.zip) e extraia o conteúdo do arquivo master.zip 
1. Abra o diretório `climafeis`, recem extraído, que contém os arquivos `demo.py` e `requirements.txt`
1. Instale os requisitos `pip install -r requirements.txt`
1. Baixe a versão mais nova do [geckodriver](https://github.com/mozilla/geckodriver/releases) e coloque o executável extraído na raiz do diretório
1. Execute o script `python .\demo.py`

### Configuração em uma distribuição GNU/Linux
1. Confira sua versão do Python com `python -V`
1. Instale o Python 3.4 ou superior e pip com o gerenciador de pacotes da sua distribuição, caso já não estejam instalados:  

    - Ubuntu e derivados `apt install python3 python3-pip`
    - Arch e derivados `pacman -S python python-pip`
    - Fedora `dnf install python3 python3-pip`  
    
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git && cd climafeis`
1. Instale os requisitos `pip install -r requirements.txt`
1. Instale o geckodriver:
    - Para Ubuntu e derivados e Fedora  
    `wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz`  
    `tar -xvzf geckodriver-v0.26.0-linux64.tar.gz`  
    `chmod +x geckodriver`  
    `sudo mv geckodriver /usr/local/bin/` 
    
    - Arch e derivados `pacman -S geckodriver`
1. Execute o script `python ./demo.py`  

#
Alternativamente, é recomendado a instalação dos requisitos em um ambiente virtual do Python, como [venv](https://docs.python.org/3/library/venv.html) ou [virtualenv](https://virtualenv.pypa.io/en/stable/).
