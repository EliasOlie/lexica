from bs4 import BeautifulSoup
import requests
import unicodedata
import time

content = []
classified_words = []

def normalization(word):
    normalized = unicodedata.normalize('NFD',word)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

sitelist = ['https://origemdapalavra.com.br/lista-palavras/?letra=a', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=b',
            'https://origemdapalavra.com.br/lista-palavras/?letra=c', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=d', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=e', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=f', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=g', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=h', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=i', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=j', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=k', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=l', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=m', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=n', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=o', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=p', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=q', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=r',
            'https://origemdapalavra.com.br/lista-palavras/?letra=s',
            'https://origemdapalavra.com.br/lista-palavras/?letra=t', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=u', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=v', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=w', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=x', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=y', 
            'https://origemdapalavra.com.br/lista-palavras/?letra=z']

def get_content(sitelista: list, resultlist: list) -> list:
    
    for i in sitelista:
        site = requests.get(i)
        soup = BeautifulSoup(site.content, 'html.parser')

        datas = soup.find_all('li')
        
        for data in datas:
            resultlist.append(data.get_text())

def classifier(wordlist: list, resultlist: list) -> list:
    for i in wordlist:
        if i[-1] == 'r':
            i = f'{i}, verbo'
        else:
            i = f'{i}, substantivo'
    
        resultlist.append(i)

t1 = time.time()

get_content(sitelist, content)
classifier(content, classified_words)

arquivo = open('lexica.txt','w')

for i in classified_words:
    arquivo.write(normalization(i)) 
    arquivo.write('\n')

t2 = time.time()

print(f'Done! in {t2-t1} seconds')