"""
# TESTE
arq = open('texto.txt') 

print(arq)

print(type(arq))

# SAÍDA
<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

# ALGUNS

arq = open('texto.txt', 'r+') # ABERTURA DE ARQUIVOS

print(arq.read()) # LEITURA DE ARQUIVOS

arq.seek(5) # MANIPULAÇÃO DO CURSOR

print(arq.read())

arq.write('\nSeja paciente e cauteloso') # ESCRITA EM ARQUIVOS

print(arq.readline(5)) # LEITURA DE UMA LINHA ESPECÍFICA

print(arq.readlines()) # LEITURA DE TODAS AS LINHAS

print(arq.closed) # VERIFICAÇÃO DE FECHAMENTO DE ARQUIVO

print(arq.close) # FECHAMENTO DE ARQUIVO

print(arq.closed) 

with open('texto.txt') as f:
    lendo_dados = f.readlines()
    for i in lendo_dados:
        print(i, end='')

print(f.close())

# ABERTURA DE ARQUIVO

with open('arquivo.txt', 'w') as arq:
    arq.write('Estamos comecançando uma nova etapa')
    arq.write('O passado não importa mais')


"""
