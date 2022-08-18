import re  # expressões regulares
import requests  # permitirá enviar solicitações http
from bs4 import BeautifulSoup  # extrai dados de arquivos html e xml
from configparser import ConfigParser  # para manipulação de arquivos INI

# Adicionei manualmente uma chave ('dados') dentro do arquivo .ini para que o interpretador localizar as informações

# Aqui ele usa o ConfigParser para leitura do arquivo solicitado
config = ConfigParser()
config.read('desafio.ini')

# Captura a informação na seção (criada) 'dados' e chave 'url', 'inicio', 'fim'
url = (config.get('dados', 'url'))
inicio = (config.get('dados', 'inicio'))
fim = (config.get('dados', 'fim'))

# Concatena a url com o nome do candidato
if '=' in url:
    new_url = url + 'alison'
    url = new_url

# Conteúdo da página do URL do site
page = requests.get(url)


# Função para remover as tags
def remove_tags(html):
    # analisa o conteúdo html
    soup = BeautifulSoup(html, "html.parser")  # cria um objeto chamado soup que está interpretando o documento HTML

    for data in soup(['script']):
        # Remove tags
        data.decompose()

    # Retorna dados removendo as tags e recuperando o conteúdo
    return ' '.join(soup.stripped_strings)


# Imprime os dados extraídos sem tags
# usa a função 'remove_tags' para remover as tags
sem_tags = remove_tags(page.content)

# localiza todas as palavras que iniciam com o valor de "inicio" (con)
start = re.findall(r'\b' + inicio + '\w+', sem_tags, flags=re.I)

print("HTML TRATADO: ")
print(sem_tags)

palavras = []  # lista para receber as palavras buscadas

# localiza todas as palavras terminam com o conteúdo de 'fim' (e)
for i in start:  # separa o conteúdo em uma lista para realizar a busca
    if i.endswith(fim):  # condição de busca do conteúdo das variáveis "fim"
        palavras.append(i)

print(f'\nLISTA DE PALAVRAS: {palavras}')  # imprime a lista das palavras encontradas
print(f'A LISTA CONTÉM: {len(palavras)} PALAVRAS')  # imprime a quantidade de letras encontradas
