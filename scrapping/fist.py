from bs4 import BeautifulSoup
import requests
import unicodedata

def normalization(word):
    normalized = unicodedata.normalize('NFD',word)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

url = 'https://www.conjugacao.com.br/verbos-regulares/'
site = requests.get(url)

soup = BeautifulSoup(site.content, 'html.parser')


lista = []
data = soup.find_all('li')

for i in data:
    lista.append(i.get_text())

arquivo = open('lexica.txt','w')

# for i in lista:
#     arquivo.write(normalization(i)) ----> Já realizei o procedimento
#     arquivo.write('\n')

#print(lista[0:5])