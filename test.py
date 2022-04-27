from cgitb import text
import requests
USER_URL = 'https://www.milanuncios.com/anuncios-usuario/juan-dario-2.htm'



r = requests.get(USER_URL)
print(r.text)
with open('test.txt', 'w+') as file:
    file.write(r.text   )