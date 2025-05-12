Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objetos, permitindo que novas instâncias sejam produzidas. Cada instância da classe, passa a ser um objeto e cada objeto tem métodos para manipulação.

<aside> 
💡
**POO é a capacidade de oferecer recursos como herança, polimorfirmos e sobrecarga.**

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