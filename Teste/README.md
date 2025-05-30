Os testes são mecanimos de validação de compotamento. Quando estamos desenvolvendo alguma aplicação  precisamos ter a segurança de que o código está retornando os tipo de dados que desejamos.  Para validar os códigos temos muitas ferramentas desde textes manuais qaunto testes automatizados. 

Existem diversos paradigmas de programação orientada a testes, um exemplo é o **Test-Drive Development (TDD)** que tem a premissa de projetar os testes antes mesmos escrevermos as linhas de código que se divide em 3 partes: escrita de teste, aprovação dos testes e refatoração.

# TDD

TDD é uma **forma de desenvolver software escrevendo testes antes do código**. Funciona em três passos:

1. **Escreve um teste** baseado no que o código **deve fazer**.
2. **Executa o teste** e vê ele **falhar** (já que o código ainda não existe ou está incompleto).
3. **Escreve o código** para fazer o teste passar.
4. Quando o teste passa, você pode **refatorar** com segurança, pois os testes vão continuar garantindo que o comportamento está correto.

Isso garante que estamos desenvolvendo códigos orientados ao problema que nos ajuda a entender melhor o que cada funcionalidade do código deve fazer 

Em Python temos a palavra reservada `assert` que é uma pergunta ao argumento que vai retornar None se a pergunta for verdadeira ou levantar um  `AssertionError:`  caso for negativo.

```python
def soma(a: int, b: int) -> int:
    assert a > 0 and b > 0, 'Ambos os valore devem ser positivos'
    return a + b

print(soma(2,4))  # 6
print(soma(-2,4)) # levanta um erro
```

> Se for rodado com uma flag **`-o`**   as verificações com assert não serão executadas
> 

## PyTest

Framework de teste para Python oferece soluções de execução, validação e produção de relatórios. 

Quando executado ele realiza uma varredura nos diretório em busca de arquivos e métodos de teste que possuem prefixos *test_** e arquivos [*conftest.py](http://conftest.py)* (* é um nome para referenciar o arquivo original de teste e conftest.py é um arquivo para colocar fixtures)

**Precisa ser instalado via pip** 

```python
pip install pytest pytest-cov 
```

**Para rodar precisamos digitar `pytest` no terminal que o restante será executado automaticamente**

### fixtures

São funções que permitem configurar um modelo de teste personalizado para representar tudo que o teste precisa fazer para realizar o seu trabalho  Fixtures são funções que preparam o ambiente para os testes. Elas criam os dados ou objetos necessários e os entregam ao teste que precisar.

```python
# Arquivo principal

class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, outher):
        return self.name == outher.name
```

```python
# Arquivo de teste: test_arq.py

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
    assert len(fruit_basket) == 2
    assert fruit_basket[0].name == "banana"
    assert fruit_basket[1].name == "apple"
```

```python
# Arquivo conftest

import pytest as t
from arq import Fruit

@t.fixture()
def my_fruit():
    return Fruit("apple")

@t.fixture()
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]
```

Ver ⤵️

<aside>
💡

[Get Started - pytest documentation](https://docs.pytest.org/en/stable/getting-started.html)

</aside>

## Unittest

Outro framework para teste no formato buid-in baseado em classes. Ele suporta a automação de testes, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework de relatórios. 

### Caso de teste

Uma unidade de teste individual. O mesmo verifica uma resposta específica a um determinado conjuto de entradas. Ao importat o `unittest` temos uma classe base `TestCAse` que pode ser usada para criar novos casos de testes.

Sua execução segue o mesmo padrão de PyTest onde são executados os método de classe que se iniciam com **test_*.**

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

Tabela de utilidade

| Método | Avalia se | Novo em |
| --- | --- | --- |
| [`assertEqual(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertEqual) | `a == b` |  |
| [`assertNotEqual(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertNotEqual) | `a != b` |  |
| [`assertTrue(x)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertTrue) | `bool(x) is True` |  |
| [`assertFalse(x)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertFalse) | `bool(x) is False` |  |
| [`assertIs(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIs) | `a is b` | 3.1 |
| [`assertIsNot(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIsNot) | `a is not b` | 3.1 |
| [`assertIsNone(x)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIsNone) | `x is None` | 3.1 |
| [`assertIsNotNone(x)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIsNotNone) | `x is not None` | 3.1 |
| [`assertIn(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIn) | `a in b` | 3.1 |
| [`assertNotIn(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertNotIn) | `a not in b` | 3.1 |
| [`assertIsInstance(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertIsInstance) | `isinstance(a, b)` | 3.2 |
| [`assertNotIsInstance(a, b)`](https://docs.python.org/pt-br/3.13/library/unittest.html#unittest.TestCase.assertNotIsInstance) | `not isinstance(a, b)` | 3.2 |

### Hooks

Consiste no momente antes de realziar o teste em si. Temos a configuração antes de realziar o teste e a configuração após o teste.

- Setup() → Configuração antes do teste
- Teardiwn() → Configuração após o teste

```python
import unittest as t

class Testes(t.TestCase):
    def setUp(self):
        # Configuração do setUp()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar apos o teste
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar apos o teste
        pass

    def tearDown(self):
        # Configuração de tearDown()
        pass
```

Exemplo

```python
# Robo.py
class Robo:
    def __init__(self, nome, bateria = 100, habilidade = []):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidade = habilidade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def bateria(self):
        return self.__bateria
    
    @property
    def habilidade(self):
        return self.__habilidade
    
    def carregar(self):
        self.__bateria = 100

    def fala_nome(self):
        if self.__bateria > 0:
            self.__bateria = self.__bateria -1
            return f'BEP BOOP. EU SOU {self.__nome.upper()}'
        return f'Bateria fraca, Por favor recarregue'
    
    def aprender_habilidades(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria = self.__bateria - custo
            self.__habilidade.append(nova_habilidade)
            return f'Habilidade nova carregada'
        return f'Bateria insuficiente'

```

```python
# Robo testes

import unittest as t

from robo import Robo

class RoboTeste(t.TestCase):
    def setUp(self):
        print('setUp() sendo executado ...')
        self.mega = Robo('Mega', bateria=50)

    def test_carregar(self):
        self.mega.carregar()
        self.assertEqual(self.mega.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.mega.fala_nome(), 'BEP BOOP. EU SOU MEGA')
        self.assertEqual(self.mega.bateria, 49, 'Bateria deveria estar em 49')

    def tearDown(self):
        print('tearDown() sendo executado ...')
        
if __name__ == '__main__':
    t.main()
```