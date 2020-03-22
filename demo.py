from selenium import webdriver
import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


def clima_login(clima_driver, user, passwd):
    clima_driver.get(r'http://clima.feis.unesp.br/login.php')
    user_field = driver.find_element_by_xpath('//input[@id="usuario"]')
    user_field.send_keys(user)

    passwd_field = driver.find_element_by_xpath('//input[@id="senha"]')
    passwd_field.send_keys(passwd)

    submit = driver.find_element_by_xpath('//input[@id="enviar"]')
    submit.click()


def fetch_daily(clima_driver, from_date, till_date):
    fromdt_field = clima_driver.find_element_by_xpath('//input[@id="dataini"]')
    fromdt_field.send_keys(datetime.datetime.strftime(from_date, '%d/%m/%Y'))

    tilldt_field = clima_driver.find_element_by_xpath('//input[@id="datafin"]')
    tilldt_field.send_keys(datetime.datetime.strftime(till_date, '%d/%m/%Y'))

    # TODO: Select parameters
    # TODO: Return csv table


# Tire o comment das linhas abaixo para iniciar o FF headless (sem GUI)
## options = Options()
## options.headless = True
## driver = webdriver.Firefox(options=options, executable_path=r'/usr/bin/geckodriver')
driver = webdriver.Firefox()  # Comente a linha para headless

# Substituir os.environ[...] por usuário e senha em texto se não for usar variáveis de ambiente
## clima_login(driver, 'usuário', 'senha')
clima_login(driver, os.environ['USER_CLIMAFEIS'], os.environ['PASSWD_CLIMAFEIS'])

# Pode colocar qualquer tipo de data, desde que se especifique o formato.
# Confira https://docs.python.org/3.8/library/datetime.html#strftime-and-strptime-format-codes
## fetch_daily(driver, datetime.datetime.strptime('01/01/2020', '%d/%m/%Y'), datetime.date.today())
## fetch_daily(driver, datetime.datetime.strptime('01-01-2020', '%d-%m-%Y'), datetime.date.today())
fetch_daily(driver, datetime.date(2020, 1, 1), datetime.date.today())  # Formato ano, mes e dia
