import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

USER_URL = 'https://www.milanuncios.com/anuncios-usuario/{id}.htm'
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
names = {'Names': [], 'URL': []}
cond = True
id = 0

while cond:
    id += 1
    driver.get(USER_URL.format(id=id))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    time.sleep(10)
    name = soup.find('h1', {'class': 'ma-UserOverviewProfileName'})

    if '¡Vaya! No hemos encontrado esta página' in driver.page_source:
        cond = False

    if name != None:
        names['Names'].append(name.getText())
        names['URL'].append(driver.current_url)
        print(name)

print(names)