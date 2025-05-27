# CSV

CSV são valores separados por vírgula cujo são o formato de exportação e importação mais utilizado para planilhas e banco de dados. Em Python para fazer a manipulação dos mesmos utilizamos um módulo chamado `csv` capaz de manipular esses dados com eficiência, ocultando do programador os detalhes de leitura e gravação dos dados.

Para facilitar a forma como um csv vai ser tratado como saída ou como entrada essas especificidades são tratados como `dialect` .  

## Parâmetros

| `delimiter=’ ‘`  | Substitui o separador `,` (vírgula) por espaço Ex `spamwriter.writerow([‘Wesley','Sant’])` saída `Wesley` `Sant`  |
| --- | --- |
| `quotechar=’|’`  | Encontra a palavra com um delimitador presente e coloca o caracter passado. Ex.: `spamwriter.writerow([‘Wesley Sant’])` a saída será `|Wesley Sant|`  |
| `quoting=`  | define quando colcocar aspas duplas. Ex. `['Olá', 'bom dia', 'valor,especial']` saída `Olá,bom dia,"valor,especial"`
 |

### Valores possíveis para `quoting`

| Valor | Explicação |
| --- | --- |
| `csv.QUOTE_MINIMAL` (padrão) | **Só coloca aspas quando precisa**, ex: se o campo tiver vírgula, quebra de linha, espaço (se o delimitador for espaço), etc. |
| `csv.QUOTE_ALL` | **Sempre** coloca aspas em todos os campos. |
| `csv.QUOTE_NONNUMERIC` | Coloca aspas **em todos os campos não numéricos**. |
| `csv.QUOTE_NONE` | **Nunca** coloca aspas. Você **precisa usar** `escapechar` se tiver delimitadores ou aspas dentro dos campos. |

## Módulo CSV

O módulo `csv` permite a leiitura e gravação de dados tabulares no formato `CSV` 

```python
import csv
```

## csv.reader

```python
# SINTAXE
csv.reader(csvfile, dialect='excel', **kwargs)
```

Retorna um objeto que lê linhas de um arquivo CSV. Esse arquivo deve ser algo que possa ser percorrido linha por linha, como uma lista de strings, um arquivo aberto ou qualquer objeto iterável. Se for um arquivo, ele deve ser aberto com `newline=''`  para funcionar corretamente com o leitor csv

```python
import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
```

## csv.writer

```python
# SINTAXE
csv.writer(csvfile, dialect='excel', **kwargs)
```

Retorna um objeto que converte os dados do usuário em uma string delimitada. O dialect define a forma como o arquivo será tratado 

## csv.DictReader

```python
import csv
with open("pokemons.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
```

Cria um objeto como os outros mas com o incremento de uma função map() por padrão. Ao utilizar DictReader() é preservado a sequencia de leiitura isso quano o para os nomes dos campos são fornecidos. Se os nome das colunas não forem fornecidos o python assumirá os valores da primeira linha e não mostra eles:

```python
# COM FIELDNAMES
import csv

with open('dados.csv') as f:
    leitor = csv.DictReader(f, fieldnames=['a', 'b', 'c'])
    for linha in leitor:
        print(linha)
# SAÍDA
# {'a': 'nome', 'b': 'idade', 'c': 'cidade'}
# {'a': 'João', 'b': '30', 'c': 'SP'}
# {'a': 'Ana', 'b': '25', 'c': 'RJ'}
```

```python
# SEM FIELDNAMES
import csv

with open('dados.csv') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(linha)
        
# SAÍDA
# {'nome': 'João', 'idade': '30', 'cidade': 'SP'}
# {'nome': 'Ana', 'idade': '25', 'cidade': 'RJ'}
```

## csv.DictWriter

Sintaxe básica:

```bash
	csv.DictWriter(f, fieldnames, restval='', extrasaction='raise',
	dialect='excel', *args, **kwds
```

Cria um objeto de escrita como qualquer outro com o adicional de mapear as chaves e valores. `fieldnames`  é uma sequência de chaves para especificar quais valores serão passados para o `writerow()` .  O parâmetro `restval`  determina o que vai acontecer quando for passado um nome a menos do especificado em `fieldnames` . O parâmetro `extrasaction=`  que pode receber dois valores `'raise'`  ou `‘ignore’` quando for passado valores a mais. Se setdo como `‘raise’` levanta um erro `ValueError` caso setado com `‘Ignore’` não acontece nada.

Exemplo com `restval` :

```bash
import csv

with open('exemplo.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'idade', 'cidade'], restval='N/A')
    writer.writeheader()
    writer.writerow({'nome': 'Ana', 'idade': 30})
    
# SAÍDA
# nome,idade,cidade
# Ana,30,N/A
```

Exemplo com `extrasaction` :

```bash
import csv

with open('exemplo.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['nome', 'idade'], extrasaction='ignore')
    writer.writeheader()
    writer.writerow({'nome': 'Ana', 'idade': 30, 'cidade': 'SP'})
    
# SAÍDA
# nome,idade
# Ana,30
```

# JSON

É muito comum em usuarios de API que utilizam os módulos `marshal` e `pickle` 

```bash
import csv
```

Usos:

```bash
import json

print(json.dumps(['foo', {'Bar': ('baz', None, 1.0, 2)}]))

print(json.dumps("\"foo\bar"))

print(json.dumps('\u1234'))

print(json.dumps('\\'))

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))

print(json.dumps({'Carla': 7, 'Bruno': 5, 'Ana': 9}, sort_keys= True, 
separators=(',',':'), indent= 4))

# SAÍDA
# ["foo", {"Bar": ["baz", null, 1.0, 2]}]
# "\"foo\bar"
# "\u1234"
# "\\"
# {"a": 0, "b": 0, "c": 0}
# {
#     "Ana":9,
#     "Bruno":5,
#     "Carla":7
# }
```

## Uso básico

Use com base a documentação 

https://docs.python.org/pt-br/3.13/library/json.html