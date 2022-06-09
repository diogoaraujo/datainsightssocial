import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

#1. Pegar conteúdo HTML a partir da URL
url = "https://books.google.com/ngrams#"

option = Options()
option.headless = True
#driver = webdriver.Firefox(executable_path=r'C:\usr\local\bin\geckodriver.exe')
driver = webdriver.Firefox()
driver.get(url)

time.sleep(10)



#2. Parsear o conteúdo HTML - BeautfulSoup
#3. Estruturar o conteúdo em um Data Frame - Pandas
#4. Transformar os Dados em um Dicionário de dados próprio
driver.quit()

#5. Converter e salvar em um arquivo JSON