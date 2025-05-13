Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objetos, permitindo que novas instâncias sejam produzidas. Cada instância da classe, passa a ser um objeto e cada objeto tem métodos para manipulação.

<aside>

💡 __POO é a capacidade de oferecer recursos como herança, polimorfirmos e sobrecarga.__

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