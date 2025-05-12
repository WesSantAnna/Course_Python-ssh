# Funções de maior grandeza

Permite que funções retornem outras funções como resultado ou até mesmo que podemos passar funções como argumentos para outras funções e criar variavéis do tipo de funções.

Também conhecido como **HOF - Higher Oder Functions**

## Exemplo

```python
# - DEFININDO FUNÇÕES

def soma(a, b):
    return a + b

def diferenca(a, b):
    return a - b

def produto(a, b):
    return a * b

def razao(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

print(calcular(4, 2, soma))
print(calcular(4, 2, diferenca))
print(calcular(4, 2, produto))
print(calcular(4, 2, razao))
```

---

# Funções aninhadas

Funções dentro de funções conhecida como Nested Functions ou Inner Functions

```python
# FUNÇÕES ANINHADAS

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de voce '))
    return humor() + pessoa

print(cumprimento('Wesley'))
print(cumprimento('Gabs'))
```

---

<aside>
💡

Inner Functions podem acessar o escopo de funções mais externas

</aside>

---

# Decoradores

Decoradores em Python são uma forma de **modificar ou estender o comportamento de funções ou métodos** sem alterar diretamente o código delas. Eles são muito usados para reutilizar lógica comum, como **logar chamadas de função**, **verificar permissões**, **medir tempo de execução**, entre outros.

### Estrutura básica de um decorador

Um decorador é basicamente **uma função que recebe outra função como argumento e retorna uma nova função** (ou a mesma, modificada).

### Exemplo simples:

```python
def meu_decorador(func):
    def wrapper():
        print("Antes da função")
        func()
        print("Depois da função")
    return wrapper

@meu_decorador
def diz_ola():
    print("Olá!")

diz_ola()
```

### Saída:

```
Antes da função
Olá!
Depois da função
```

### O que está acontecendo aqui?

1. `@meu_decorador` é **sintaxe açucarada** para:
    
    ```python
    diz_ola = meu_decorador(diz_ola)
    ```
    
2. A função `diz_ola` é passada como argumento para `meu_decorador`, que retorna a função `wrapper`.
3. Quando você chama `diz_ola()`, na verdade está chamando `wrapper()` — a versão decorada da função original.

---

### Decoradores com argumentos

Se a função original recebe argumentos, o `wrapper` também precisa aceitar esses argumentos:

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Chamando a função decorada")
        return func(*args, **kwargs)
    return wrapper

@meu_decorador
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
```

### Saída:

```
Chamando a função decorada
Olá, Maria!
```

---

### Decoradores prontos no Python

- `@staticmethod`
- `@classmethod`
- `@property`
- `@functools.lru_cache`
- `@functools.wraps` (usado dentro de decoradores para preservar o nome e docstring da função original)

---

# Decoradores com diferentes assinaturas

Decoradores com diferentes assinaturas em Python são úteis quando você quer criar um decorador que funcione com funções que têm diferentes números e tipos de argumentos. Para isso, geralmente usamos `*args` e `**kwargs` na definição do decorador interno, permitindo capturar qualquer combinação de argumentos posicionais e nomeados.

### Exemplo Básico de Decorador com Suporte a Diferentes Assinaturas

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com args={args} kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} retornou {resultado}")
        return resultado
    return wrapper
```

Você pode usar esse decorador com qualquer função:

```python
@meu_decorador
def soma(a, b):
    return a + b

@meu_decorador
def saudacao(nome="Mundo"):
    return f"Olá, {nome}!"

soma(2, 3)                 # args=(2, 3), kwargs={}
saudacao(nome="Alice")    # args=(), kwargs={'nome': 'Alice'}
```

---

### Decoradores com Argumentos (Funções de Ordem Superior)

Se você quiser passar argumentos para o decorador, precisará de mais um nível de função:

```python
def repetir(n):
    def decorador(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador
```

Uso:

```python
@repetir(3)
def diga_oi():
    print("Oi!")
```

---

### Preservando a Assinatura da Função Decorada

Se você quiser que a função decorada mantenha sua assinatura (para documentação ou introspecção), use `functools.wraps`:

```python
from functools import wraps

def meu_decorador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## Preservando metadados com wraps

Com a utilização de decoradores algumas informação provenientes do dado que estamos trabalhando são perdidas justamente pelo fato de estarmos trabalhando com funções modificadas

```python
# PROBLEMAS

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui fica a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

# SAÍDA ESPERADA
print(soma(10,20))   # 30
print(soma.__name__) # soma
print(soma.__doc__)  # Soma dois números

# SAÍDA OBTIDA
# 30
# logar
# Eu sou uma função (logar) dentro de outra
```

A informação que queríamos não foi a que recebemos porque o Python entende que queremos as informações da função decoradora. Para corrigir isso precisamos fazer um import.

```python
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui fica a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b

print(soma(10,20))   
print(soma.__name__) 
print(soma.__doc__)  

# SAÍDA ESPERADA
# 30
# soma
# Soma dois números
```

Isso problema não afeta a execuçõa do código, mas pode ser um problema quando queremos consultar a documentação.

---

## Forçar casting

```python
def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args,**kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)

repete_msg('Mensagem repitida', '3')

@forca_tipo(float,float)
def dividir(a, b):
    print(a / b)

dividir(4,5)
```