# desafio

O objetivo deste desafio é testar seus conhecimentos em Python e lógica de programação além de sua capacidade de entendimento de problemas.


Instruções:

Anexo consta um arquivo desafio.ini que deverá ser baixado no seu computador. Ele deve ser salvo na mesma pasta onde você criará seu arquivo fonte Python. Neste arquivo constam alguns parâmetros que você OBRIGATORIAMENTE deverá usar no seu script Python, de acordo com os passos que serão detalhados.

O nome do arquivo com o seu script Python deverá ser desafio-[seu-nome].py (ex.: no meu caso seria desafio-evandro.py)


OBJETIVO: O que queremos é que você desenvolva um script Python que leia uma página web (indicada pelo parâmetro url do arquivo desafio.ini), remova todo conteúdo javascript e todas as tags html, converta caracteres html em caracteres normais e deixe apenas uma quebra de linha entre as linhas. Após isto, seu script deverá localizar todas as palavras iniciadas por uma determinada sequência de caracteres (parâmetro inicio do arquivo desafio.ini) e terminadas com outra sequência de caracteres (parâmetro fim do arquivo desafio.ini) . 


Passo a passo que seu script deverá executar:



passo 1: ler o arquivo desafio.ini (anexo) e carregar os 3 parâmetros que constam nele (url, inicio e fim);

passo 2: carregar o conteúdo apontado pelo parâmetro url que consta no arquivo desafio.ini e que você carregou no passo 1. Passe seu nome em minúsculo como conteúdo do parâmetro candidato na url;

passo 3: fazer os seguintes tratamentos no conteúdo carregado no passo 2:

remover todo código javascript;
remover todas as tags html;
converter todos os caracteres html (Exemplo: &amp; deve ser convertido para &, &aacute; deve ser convertido para á e assim por diante);
manter apenas uma quebra de linha entre cada linha (se entre duas linhas existirem 10 quebras de linha, as 10 quebras deverão ser transformadas em 1 quebra)

passo 4: localizar todas as palavras que comecem com conteúdo do parâmetro inicio e terminem com o conteúdo do parâmetro fim que você carregou no passo 1. Ignore maiúscula e minúsculas;

passo 5: imprimir no console o conteúdo do html tratado, a quantidade de palavras encontradas e a lista das palavras encontradas;



IMPORTANTE: 

o código deverá estar comentado e você fará a defesa do que foi entregue.

a interpretação faz parte do desafio;

se tiver dificuldade com algum tratamento do passo 3, você pode ignorá-lo justificando o porquê.

o script deve ser capaz de procurar qualquer palavra iniciando e terminando com as sequências colocadas no arquivo desafio.ini.

não existe “pegadinha” neste desafio.
