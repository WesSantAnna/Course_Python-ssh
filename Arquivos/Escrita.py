"""
# TESTE
arq = open('texto.txt') 

print(arq)

print(type(arq))

# SAÍDA
<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

# -----------------------------------------------------------------
# ALGUNS MÉTODOS

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

# --------------------------------------------------------------
# ABERTURA DE ARQUIVO

with open('arquivo.txt', 'w') as arq:
    arq.write('Estamos comecançando uma nova etapa')
    arq.write('O passado não importa mais')

    
with open('Tarefas.txt', 'w') as taf:
while True:
    tarefa = input('Digite um tarefa ou digite sair: ')
    if tarefa != 'sair':
        taf.write(tarefa + '\n')
    else:
        break

# --------------------------------------------------------------------
# StringIO

from io import StringIO as st

mensagem = 'Colocando em prática utilização do módulo StringIO'

arq = st(mensagem)

arq.write('\nQue permite a manipulação de arquivo via memória')

arq.seek(0)

print(arq.read())

# ---------------------------------------------------------------------

# MANIPULAÇÃO DE ARQUIVOS: NAVEGAÇÃO

import os 

print(os.name) # 'nt' para Win

# NAVEGAÇÃO

diretorio_atual = os.getcwd()
print(f'Diretório atual: {diretorio_atual}')


# MOVIMENTAÇÃO ENTRE DIETÓRIOS
os.chdir("C:\Users\TESTE\Desktop\Python\Modulos") # caminho
print(os.getcwd())

# CONTEÚDO
lista_arq = os.listdir() # lista os arquivos e pastas
print(lista_arq)

# MANIPULAÇÃO

# CRIAR
os.mkdir("ManipulacaoArq") # cria uma pasta
os.makedirs("Base\\primeiro_ramo") # cria uma hierarquia de pastas

# REMOVER
os.rmdir("ManipulacaoArq")
os.removedirs("Base\\primeiro_ramo")


# VERIFICAÇÃO

# VERIFICA SE EXISTE
caminho = r"C:\Users\TESTE\Desktop\Python\Modulos"
print(os.path.exists(caminho))

# VERIFICA SE É ARQUIVO OU DIRETÓRIO
print(os.path.isfile(caminho))
print(os.path.isdir(caminho))

# OBTER NOME DO ARQUIVO OU DIRETÓRIO
caminho = r"C:\Users\SeuUsuario\Documents\arquivo.txt"

print(os.path.basename(caminho))  # 'arquivo.txt'
print(os.path.dirname(caminho))   # 'C:\\Users\\SeuUsuario\\Documents'

# JUNTAR CAMINHOS VIA CROSS-PLATAFORM
novo_caminho = os.path.join("C:\\Users\\SeuUsuario", "Documents", "arquivo.txt")
print(novo_caminho)

# --------------------------------------------------------------------------------------

"""
