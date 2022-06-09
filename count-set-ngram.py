import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
import ast

#1. Pegar conteúdo HTML a partir da URL
url = "https://books.google.com/ngrams#"

option = Options()
option.headless = True
driver = webdriver.Firefox()
# codigo executa em background 
# driver = webdriver.Firefox(options=option)
driver.get(url)


#import json and convert to list
with open('categorias.json') as json_file:
    data = json.load(json_file)
print(data)

source = driver.find_element_by_xpath(
    "//input[@type='text']")
source.clear()
source = driver.find_element_by_xpath(
    "//input[@type='text']")
source.send_keys(data)
source.send_keys(Keys.ENTER)

time.sleep(10)


#2. Parsear o conteúdo HTML - BeautfulSoup
#3. Estruturar o conteúdo em um Data Frame - Pandas
#4. Transformar os Dados em um Dicionário de dados próprio
driver.quit()

#5. Converter e salvar em um arquivo JSON