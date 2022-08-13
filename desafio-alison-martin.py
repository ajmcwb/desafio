import urllib
import requests
from bs4 import BeautifulSoup  # extrai dados de arquivos html e xml
from configparser import ConfigParser

# Aqui ele ele usa o ConfigParser para leitura do arquivo solicitado
config = ConfigParser()
config.read('desafio.ini')  # arquivo solicitado

candidato = 'alison-martin'
url = (config.get('dados', 'url'))  # captura a informação na seção (criada) 'dados' e chave 'url'
inicio = (config.get('dados', 'inicio'))  # captura a informação da seção 'dados' e chave 'inicio'
fim = (config.get('dados', 'fim'))  # captura a informação da seção 'dados' e chave 'fim'

new_url = url + candidato
url = new_url

# html = requests.get(url).content  # pegando o conteudo de uma requisição get na url solicitada
# soup = BeautifulSoup(html, 'html.parser')  # é criado um objeto chamado soup que está interpretando o documento HTML.

# Page content from Website URL
page = requests.get(url)


# Function to remove tags
def remove_tags(html):
    # parse html content
    soup = BeautifulSoup(html, "html.parser")

    for data in soup(['script']):
        # Remove tags
        data.decompose()

    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)


# Print the extracted data
print(remove_tags(page.content))
