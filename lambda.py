
"""
# DECLARAÇÃO

calc = lambda x: 3 * x + 1

print(calc(3))

# MULTIPLAS ENTRADAS
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(" wesley          ",' santAnna'))
print(nome_completo('FERNANDA','SANTOS           '))

# ZERO ENTRADAS
texto = lambda: 'O mundo é uma selva'

# UMA ENTRADA
uma = lambda x: x ** 2

# DUAS ENTRADA
duas = lambda x, y: (x - y) / (y * x)

# TRÊS ENTRADAS
tres = lambda x, y, z:  (pow(x, y) / (y - z)) * z

print(texto())

print(duas(4,2))

print(tres(4,5,6))

# FORMA CERTA DE UTILIZAR UMA FUNÇÃO LAMBDA
atores = [
    'Robert J. Downey',
    'Scarlett Johansson',
    'Thomas J. Hanks',
    'Emma Stone',
    'Leonardo Wilhelm DiCaprio',
    'Natalie H. Portman',
    'Denzel Hayes Washington',
]

atores.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(atores)

# UTILIZANDO O MAP()

import math as mt

def area_circle(r):
    return mt.pi * pow(r, 2)

print(area_circle(2))
print(area_circle(7.2))

raios = [2, 8, 41, 34, 9, 14.7, 7.3]

# FORMA 1
areas = []
for i in raios:
    areas.append(area_circle(i))

print(areas)

# FORMA 2
areas = map(area_circle, raios)
print(list(areas))

# FORMA 3

print(list(map(lambda r: mt.pi * pow(r,2), raios)))

# UTILIZANDO FILTER()

import statistics as st

dados = [1, 7,  8, 98, 0.95, 8.4, 9.0, 5.52, 41.74, -54]

print(f'Média: {st.mean(dados)}')

dados_filtrados = filter(lambda x: x < st.mean(dados), dados)

print(f'Os valores acima da média são: {list(dados_filtrados)}')

print(list(dados_filtrados))

# OUTRO EXEMPLO

usuarios = {
    "Lucas Andrade": {
        "tweets": []
    },
    "Maria Costa": {
        "tweets": ["A vida é feita de escolhas."]
    },
    "João Lima": {
        "tweets": ["Bom dia!", "Foco, força e fé."]
    },
    "Ana Paula": {
        "tweets": []
    },
    "Carlos Meireles": {
        "tweets": ["Aprendizado constante é a chave."]
    },
    "Beatriz M.": {
        "tweets": ["Segunda-feira começando...", "Café é vida."]
    },
    "Renato Gouveia": {
        "tweets": []
    }
}

print(usuarios)

# FILTRAR OS USUÁRIOS QUE ESTÃO INATIVOS

inativos = list(filter(lambda nome: len(usuarios[nome]['tweets']) == 0, usuarios))

ativos = list(filter(lambda nome: len(usuarios[nome]['tweets']) != 0, usuarios))

print(f'Os usuários inativos são: {inativos}')

print(f'Os usuários ativos são: {ativos}')

# ALL & ANY

print(all((0, 1, 2, 3, 4, 5)))
print(all((1, 2, 3, 4, 5)))
print(all([]))
print(all('Wesley'))

print(any((0, 0, 0)))  # False – todos são falsos (0 é considerado False)
print(any((0, 0, 1)))  # True – pelo menos um valor é verdadeiro
print(any([]))         # False – lista vazia: nenhum valor para ser verdadeiro
print(any(''))         # False – string vazia é falsa
print(any('Wesley'))   # True – string não vazia é verdadeira (cada caractere é "truthy")

# GERADORES
def infinite_sequence(num):
    while True:
        yield num
        num += 1

# Criando o gerador apenas uma vez
gen = infinite_sequence(1)

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4

# COMPARANDO MEMÓRIA

from sys import getsizeof

list_compr = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

gera_comp = getsizeof((x * 10 for x in range(1000)))


print(f'List Comprehesion: {list_compr} bytes')
print(f'Set Comprehesion: {set_comp} bytes')
print(f'Dict Comprehesion: {dict_comp} bytes')
print(f'Generator Comprehesion: {gera_comp} bytes')

# sort() e sorted()

valores = [1,7,6,4,8,1,2,5,45,102,518,41,6561,58,41,-2,74,-98,125,-451]

print(sorted(valores)) # CRIA UM LISTA ORDENADA

valores.sort()

print(valores) # MODIFICA VALORES DIRETAMENTE

print(sorted(valores, reverse=True))

lista = [x for x in range(1,11)]
        
print(reversed(lista))

print(list(reversed(lista)))

print(tuple(reversed(lista)))

print(set(reversed(lista)))

print('Wesley SantAnna'[::-1])

# ZIP

lista1 = ['Wesley SantAnna', 'Fernanda Santos']
lista2 = ['Filho', 'Mae']
lista3 = [21,42]

zip1 = zip(lista1,lista2,lista3)

print(list(zip1))
"""


