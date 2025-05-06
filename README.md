# 🐍 Estudo de Python

Este repositório contém exemplos organizados para estudo de programação em Python, com foco em conceitos essenciais e práticas modernas. Siga as seções abaixo na ordem recomendada para maximizar seu aprendizado.

---

## 📌 Índice

1. [Variáveis e Tipos](#variáveis-e-tipos)
2. [Coleções de Dados](#coleções-de-dados)
3. [Laços de Repetição](#laços-de-repetição)
4. [Funções](#funções)
5. [List Comprehension](#list-comprehension)
6. [Tratamento de Erros](#tratamento-de-erros)
7. [Funções Lambda](#funções-lambda)
8. [Map, Filter, Zip](#map-filter-zip)
9. [Funções Built-in: all, any, reversed](#funções-built-in)
10. [Geradores e Consumo de Memória](#geradores-e-consumo-de-memória)
11. [Ordenação com sort e sorted](#ordenação)

---

## 📊 Variáveis e Tipos

```python
num1 = 0
num2 = 0
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f'{num1} é maior')
else:
    print(f'{num2} é maior')
```
## 📦 Coleções de Dados
### Dicionários e Iteração
``` python
nums = {'a': 1 , 'b': 2, 'c': 3}
square = {chave: valor ** 2 for chave, valor in nums.items()}
print(square)

chaves = [chr(a) for a in range(97,123)]
valores = [i for i in range(1,27)]
mix = {chaves[i]: valores[i] for i in range(len(chaves))}
print(mix)
```
## 🔁 Laços de Repetição
### for com range()
```python
for i in range(1, 7):
    if i % 3 == 0:
        print(f"{i} é múltiplo de 3")
while

contador = 10
while contador >= 0:
    print(contador, end=' ')
    contador -= 1
print("FIM")
```
## 🧮 Funções
```python
def exercicio1():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    print(f'Maior valor: {max(num1, num2)}')

def exercicio2():
    import math
    num = int(input("Digite um número: "))
    if num > 0:
        print(f'Raiz quadrada: {math.sqrt(num)}')
    else:
        print("Número não é positivo")

def exercicio3():
    num = int(input("Digite um número: "))
    print("Par" if num % 2 == 0 else "Ímpar")
    ```

## 🔃 List Comprehension
```python
quadrados = [x**2 for x in range(10)]
pares = [x for x in range(20) if x % 2 == 0]
print(quadrados)
print(pares)
```
## 🛑 Tratamento de Erros
### Erros comuns
```python
# SyntaxError: falta parênteses
# def funcao:

# NameError
 print(nome_nao_definido)

# TypeError
 len(5)

# IndexError
 lista = [1, 2, 3]
 print(lista[5])

# ValueError
 int("abc")

# KeyError
 dicionario = {"chave": "valor"}
 print(dicionario["outra"])
```
## 🔁 Herança de Exceções
```python
class B(Exception): pass
class C(B): pass
class D(C): pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```
## 🧠 Funções Lambda
```python
calc = lambda x: 3 * x + 1
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(calc(3))
print(nome_completo(" wesley ", " santAnna"))
```
## 🔧 Map, Filter, Zip
### map()
```python
import math
raios = [2, 4, 6]
areas = list(map(lambda r: math.pi * r ** 2, raios))
print(areas)
```
### filter()
```python
import statistics
dados = [1, 2, 3, 99, -2]
media = statistics.mean(dados)
abaixo = list(filter(lambda x: x < media, dados))
print(abaixo)
```
### zip()
```python
nomes = ["Ana", "João"]
funcoes = ["Engenheira", "Médico"]
idades = [30, 40]
print(list(zip(nomes, funcoes, idades)))
```
## ✅ Funções Built-in
```python
print(all([1, 2, 3]))   # True
print(all([1, 0, 3]))   # False
print(any([0, 0, 1]))   # True
print(reversed([1, 2, 3]))
```
## ⚙️ Geradores e Consumo de Memória
```python
def infinite_sequence(n):
    while True:
        yield n
        n += 1

gen = infinite_sequence(1)
print(next(gen))
print(next(gen))

from sys import getsizeof

print(f"List: {getsizeof([x * 10 for x in range(1000)])}")
print(f"Generator: {getsizeof((x * 10 for x in range(1000)))}")

```
## 🔢 Ordenação
```python
valores = [4, 1, 3, 7]
print(sorted(valores))          # Retorna nova lista ordenada
valores.sort()
print(valores)                  # Modifica a lista original
print(sorted(valores, reverse=True))
```
