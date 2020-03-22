# Climafeis
Demo de uma interface em Python para a consulta de dados climatológicos do banco de dados do [Canal CLIMA](http://clima.feis.unesp.br) com a biblioteca [Selenium](https://selenium-python.readthedocs.io/).  

### Instalação no Windows
1. Confira sua versão do Python em uma shell (Powershell ou CMD) com `python -V`
1. Instale o [Python 3.4](https://www.python.org/downloads/windows/) ou superior, caso não esteja instalado
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git` ou baixe o [repositório](https://github.com/joaofauvel/climafeis/archive/master.zip) e extraia o conteúdo do arquivo master.zip 
1. Navegue até a raiz do repositório, que contém o script e `requirements.txt`
1. Instale os requisitos digitando `pip install -r requirements.txt`
1. Baixe a versão mais nova do [geckodriver](https://github.com/mozilla/geckodriver/releases) e coloque o executável extraído na raiz do repositório
1. Execute o script `python .\demo.py`

### Instalação em uma distribuição GNU/Linux
1. Confira sua versão do Python com `python -V`
1. Instale o Python 3.4 ou superior com o gerenciador de pacotes da sua distribuição, caso não esteja instalado  
    - Ubuntu e derivados `apt install python3.6`
    - Arch e derivados: `pacman -S python`
1. Clone esse repositório com `git clone https://github.com/joaofauvel/climafeis.git && cd climafeis`
1. Instale os requisitos digitando `pip install -r requirements.txt`
1. Instale o geckodriver
    - Para Ubuntu e derivados:  
    `wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz`  
    `tar -xvzf geckodriver-v0.26.0-linux64.tar.gz`  
    `chmod +x geckodriver`  
    `sudo mv geckodriver /usr/local/bin/` 
    
    - Arch e derivados `pacman -S geckodriver`
1. Execute o script `python ./demo.py`
