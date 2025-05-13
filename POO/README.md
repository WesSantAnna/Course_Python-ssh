Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objetos, permitindo que novas instâncias sejam produzidas. Cada instância da classe, passa a ser um objeto e cada objeto tem métodos para manipulação.

<aside>

💡 **POO é a capacidade de oferecer recursos como herança, polimorfirmos e sobrecarga.**

</aside>

---

# Sintaxe

```python
class NomeClasse:
	<instrução 1>
	.
	.
	.
	<instrução N>
```

## Objeto Classe

Objetos classe suportam dois tipos de oerações: *referências a atributos e instanciação.*

*Referências a atributos* de classe utilizam a sintaxe padrão utilizada para quaisquer referências a atributos em Python: `obj.nome`. Nomes de atributos válidos são todos os nomes presentes dentro do espaço de nomes da classe, quando o objeto classe foi criado. Portanto, se a definição de classe tem esta forma:

```python
class MinhaClasse:
    """Um exemplo de classe simples"""
    i = 12345

    def f(self):
        return 'olá mundo'
```

então `MinhaClasse.i` e `MinhaClasse.f` são referências a atributo válidas, retornando, respectivamente, um inteiro e um objeto função. Atributos de classe podem receber valores, pode-se modificar o valor de `MinhaClasse.i` num atribuição. [`__doc__`](https://docs.python.org/pt-br/3/reference/datamodel.html#type.__doc__) também é um atributo válido da classe, retornando a docstring associada à classe: `"Um exemplo de classe simples"`.

Para *instanciar* uma classe, usa-se a mesma sintaxe de invocar uma função. Apenas finja que o objeto classe do exemplo é uma função sem parâmetros, que devolve uma nova instância da classe. Por exemplo (presumindo a classe acima):

```python
x = MinhaClasse()
```

cria uma nova *instância* da classe e atribui o objeto resultante à variável local `x`.

A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Muitas classes preferem criar novos objetos com um estado inicial predeterminado. Para tanto, a classe pode definir um método especial chamado [`__init__()`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__init__), assim:

```python
def __init__(self):
	self.data = []
```

Quando uma classe define um método [`__init__()`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__init__), o processo de instanciação automaticamente invoca `__init__()` sobre a instância recém criada. Em nosso exemplo, uma nova instância já inicializada pode ser obtida desta maneira:

```python
x = MinhaClasse()
```

Naturalmente, o método [`__init__()`](https://docs.python.org/pt-br/3/reference/datamodel.html#object.__init__) pode ter parâmetros para maior flexibilidade. Neste caso, os argumentos fornecidos na invocação da classe serão passados para o método `__init__()`. Por exemplo,

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

# SAÍDA
# (3.0, -4.5)
```

### Objetos instância

São objetos cujas únicas operações compreendidas são atributos de referência. Existem duas maneiras válidas de nomear atributos: atributos de dados e métodos.

1. Atributos de dados - guardam valores (strig, números, listas, etc.) e são acessados via `obj,atributo` 
2. Métodos - são objetos funções que realizam alguma operação com os dados internos e são acessados via `obj.método()` 

```python
class Pessoa:
    def __init__(self, nome):     # método especial
        self.nome = nome          # atributo de dado

    def cumprimentar(self):       # método
        print(f"Olá, eu sou {self.nome}")
```

### Objeto método

```python
x.f()
```

Uma particularidade sobre os métodos é que o objeto da instânia é passado como primeiro argumento da função. No exemplo, a chama `x.f()`é exatamente equivalente a `MinhaClasse.f(x)` 

### Variáveis de classe e instância

Variáveis de instância são vairáveis que indicam dados que são únicos a cada instância idividual e vairiáveis de classe são variáveis de atributos e de métodos que são comuns a todas as instâncias de uma classe

```python
class Cachorro:
    tipo = 'canino'            # variável de classe
    def __init__(self, nome):
        self.nome = nome       # variável de instância

d = Cachorro('Frido')
e = Cachorro('Buddy')

print(e.tipo) # canino
print(d.tipo) # canino

print(d.nome) # exclusiva de d = Frido
print(e.nome) # exclusiva de e = Buddy
```

---

# Observações aleatórias

Por convensão dados iniciados com `(__)` duplo underscore são atributos privados e ao tentar acessa-lo via referência levanta um erro

```python
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

user = Acesso('wesley@exemplo.com','1234')

print(user.email)
print(user.__senha)

# SAÍDA
# wesley@exemplo.com
# Traceback (most recent call last):
#   File "c:\Users\TESTE\Desktop\Python\POO\POO.py", line 71, in <module>
#     print(user.__senha)
#           ^^^^^^^^^^^^
# AttributeError: 'Acesso' object has no attribute '__senha'
```

```python
class Produto:
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descrição, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descrição = descrição
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

p1 = Produto('PS5', 'VideoGame', 3000)
p2 = Produto('Xbox','VideoGame', 2500)

print(p1.valor)
print(p2.valor)

print(p1.id)
print(p2.id)
```

# Encapsulamento

Segurança. Na utilização do encapsulamento de dados você possuí uma blindagem contra acesso indevido. Com encapsulamento, os dados protegidos (privados) não podem ser acessados diretamente por conta dos modificadores de acesso **`(__)`**. A única forma de aceder ao dado do tipo privado é através dos métodos (membros da classe). Isso assegura proteção. 

```python
class A:
    a = 1 # Atributo público
    __b = 2 # Atributo privado a class A

class B(A):
    __c = 3 # Atributo privado a B

    def __init__(self):
        print(self.a)
        print(self.__c)

a = A()

print(a.a) # imprime 1

b = B()

print(b.__b)

# SAÍDA
# 1
# 1
# 3
# Traceback (most recent call last):
#   File "c:\Users\TESTE\Desktop\Python\POO\POO.py", line 147, in <module>
#     print(b.__b)
#           ^^^^^
# AttributeError: 'B' object has no attribute '__b'
```

Outro exemplo;

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial  # atributo privado

    def ver_saldo(self):
        return f'Saldo atual: R$ {self.__saldo:.2f}'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f'Depósito de R$ {valor:.2f} realizado com sucesso.'
        return 'Valor inválido para depósito.'

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return f'Saque de R$ {valor:.2f} realizado com sucesso.'
        return 'Saldo insuficiente ou valor inválido.'

conta = ContaBancaria("Ana", 1000)

print(conta.ver_saldo())                # Saldo atual: R$ 1000.00
print(conta.depositar(500))             # Depósito de R$ 500.00 realizado com sucesso.
print(conta.sacar(200))                 # Saque de R$ 200.00 realizado com sucesso.
print(conta.ver_saldo())                # Saldo atual: R$ 1300.00

# TENTATIVA DE ACESSAR DIRETAMENTE (NÃO RECOMENDADO)
print(conta.__saldo)  # Erro: AttributeError
```

Se não estive protegido eu poderia acessar meu saldo e modificalo para qualquer valor que eu quisesse.

# Herança

### Sintaxe básica

```python
class NomeClasseDerivada(NomeClasseBase):
	<instrução 1>
	.
	.
	.
	<instrução N>
```

Quando estamos trabalhando com uma classe que está em outro módulo devemos declarar a classe derivada da seguinte maneira

```python
class NomeClasseDerivada(nomemódulo NomeClasseBase):
```