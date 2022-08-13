import requests  # permitirá enviar solicitações http
from bs4 import BeautifulSoup  # extrai dados de arquivos html e xml
from configparser import ConfigParser  # para manipulação de arquivos INI

# Primeiro foi necessário inserir uma chave ('dados') dentro do arquivo .ini
# para que o interpretador possa localizar as informações

# Aqui ele usa o ConfigParser para leitura do arquivo solicitado
config = ConfigParser()
config.read('desafio.ini')

# captura a informação na seção (criada) 'dados' e chave 'url', 'inicio', 'fim'
url = (config.get('dados', 'url'))
inicio = (config.get('dados', 'inicio'))
fim = (config.get('dados', 'fim'))

# tratamento do erro se não conter '=' ao final da url, para não ocorrer Erro 404
if '=' in url:
    # concatena a url com o nome do candidato
    new_url = url + 'alison-martin'
    url = new_url

page = requests.get(url)


# Conteúdo da página do URL do site
# Função para remover as tags
def remove_tags(html):
    # analisa o conteudo html
    # é criado um objeto chamado soup que está interpretando o documento HTML
    soup = BeautifulSoup(html, "html.parser")

    for dados in soup(['script']):
        # Remove tags
        dados.decompose()

    # Retorna dados recuperando o conteúdo da tag
    return ' '.join(soup.stripped_strings)


# Imprime os dados extraídos sem tags
# usa a função 'remove_tags' para remover as tags e converte todos os caracteres em minusculas
sem_tags = remove_tags(page.content).lower()

# localiza todas as palavras que iniciam com o conteudo de 'inicio' (con) e termina com o conteúdo de 'fim' (e)
for i in sem_tags.split():  # separa o conteudo em uma lista para realizar a busca
    palavras = list()
    if i.startswith(inicio) and i.endswith(fim):  # condição de busca do conteudo das variáveis inicio e fim
        print(i)

# for i in sem_tags.split():  # separa o conteudo em uma lista para realizar a busca
#     if i.startswith(inicio) and i.endswith(fim):  # condição de busca do conteudo das variáveis inicio e fim
#         print(i)  # imprime as palavras encontradas que iniciam e terminam com os valores das variáveis inicio e fim
