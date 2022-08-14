import requests  # permitirá enviar solicitações http
from bs4 import BeautifulSoup  # extrai dados de arquivos html e xml
from configparser import ConfigParser  # para manipulação de arquivos INI
import time

# Primeiro foi necessário inserir uma chave ('dados') dentro do arquivo .ini
# para que o interpretador possa localizar as informações

# Aqui ele usa o ConfigParser para leitura do arquivo solicitado
config = ConfigParser()
config.read('desafio.ini')

# captura a informação na seção (criada) 'dados' e chave 'url', 'inicio', 'fim'
url = (config.get('dados', 'url'))
inicio = (config.get('dados', 'inicio'))
fim = (config.get('dados', 'fim'))

if '=' in url:
    # concatena a url com o nome do candidato
    new_url = url + 'alison-martin'
    url = new_url

# Conteúdo da página do URL do site
page = requests.get(url)


# Função para remover as tags
def remove_tags(html):
    # analisa o conteudo html
    soup = BeautifulSoup(html, "html.parser")  # é criado um objeto chamado soup que está interpretando o documento HTML

    for data in soup(['script']):
        # Remove tags
        data.decompose()

    # Retorna dados recuperando o conteúdo da tag
    return ' '.join(soup.stripped_strings)


# Imprime os dados extraídos sem tags
# usa a função 'remove_tags' para remover as tags
sem_tags = remove_tags(page.content)
print(sem_tags)


# converte os caracteres em minuscula
tags_lower = sem_tags.lower()

palavras = []
# localiza todas as palavras que iniciam com o conteudo de 'inicio' (con) e termina com o conteúdo de 'fim' (e)
for i in tags_lower.split():  # separa o conteudo em uma lista para realizar a busca
    if i.startswith(inicio) and i.endswith(fim):  # condição de busca do conteudo das variáveis inicio e fim
        palavras.append(i)

print()
print(f'LISTA DE PALAVRAS: {palavras}')
print(f'A LISTA CONTÉM "{len(palavras)}" PALAVRAS')
