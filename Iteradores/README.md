**Iterators** e **Generators** são conceitos fundamentais em Python, especialmente úteis quando se trabalha com **coleções de dados**, **loops** e **grandes volumes de informação**.

---

## O que é um **Iterator**?

Um **iterator (iterador)** é um **objeto que pode ser percorrido elemento por elemento**, como em um `for`. Ele implementa os métodos:

- `__iter__()` → retorna o próprio objeto iterator.
- `__next__()` → retorna o próximo item ou lança `StopIteration`.

### Exemplo básico:

```python
lista = [1, 2, 3]
iterador = iter(lista)  # Cria um iterator

print(next(iterador))  # 1
print(next(iterador))  # 2
print(next(iterador))  # 3
# print(next(iterador))  # Lança StopIteration
```

### Criando o próprio iterador

```python
# CRIAÇÃO DE ITADORES
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

# PRIMEIRA EXECUÇÃO: ITERADOR CRIADO
for n in Contador(1,61):
    print(n)
```

Qualquer estrutura **iterável** (listas, strings, tuplas, arquivos) pode ser transformada em um iterator com `iter()`.

<aside>
💡

**Os iteradores tem chamadas para os método `next()` e `__iter()**__`

</aside>

---

## O que é um **Generator**?

Um **generator (gerador)** é um **tipo especial de iterator**, criado com **funções normais** usando a palavra-chave `yield` no lugar de `return`.

- `yield` **pausa a função**, **mantém o estado** e **retoma depois**, sem perder os valores anteriores.
- Isso economiza **memória**: os valores são gerados **sob demanda**, um por vez.

### Exemplo básico de generator:

```python
def contar_ate_3():
    yield 1
    yield 2
    yield 3

g = contar_ate_3()

print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
```

⚠️ Comparando com `return`, que **encerra** a função, o `yield` **pausa** e pode continuar depois.

---

## Diferença em resumo

| Característica | Iterator | Generator |
| --- | --- | --- |
| É um objeto? | Sim | Sim |
| Armazena estado? | Sim (manual) | Sim (automaticamente com `yield`) |
| Fácil de criar? | Não (precisa implementar métodos) | Sim (com função e `yield`) |
| Uso de memória | Pode ser alto | Baixo (gera valores sob demanda) |

---

### Exemplo prático: iterador vs generator

### Iterator manual:

```python
class Contador:
    def __init__(self, limite):
        self.contador = 0
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

for n in Contador(3):
    print(n)
```

### Generator:

```python
def contador(limite):
    for i in range(1, limite + 1):
        yield i

for n in contador(3):
    print(n)
```

💡 O generator faz o mesmo com **menos código** e **mais eficiência**.

---

# Teste de memórias

<aside>
💡

**GENERATOR TEM MELHOR EFICIENCIA EM USO DE MEMÓRIA**

</aside>