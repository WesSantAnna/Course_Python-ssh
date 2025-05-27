Em Python, existe um módulo build-in que fornce suporte a inplementação de scripts que trabalham com data e hora.

# Objeto Conciete e Ingênuo

Quando estamos trabalhando com data e hora em python temos que ter em mente que temos questões relativas a fuso horário (**`timezone`**) e a presença de informações a respeito - ou falta dela -  nos introduz dois objetos diferentes:

## Awere

- Tem informação de fuso horário (**`tzinfo`**)
- Sabe exatamente em que local do mundo e em que momento do tempo ele está.
- Pode ser comparado precisamente com outros objetos aware (mesmo que em fusos diferentes).
- Exemplo: **`print(datetime.datetime.now())` → 2025-05-27 08:29:00.749705**

## Naive

- Não tem fuso associado (**`tzinfo = None`**)
- Representa apenas data e hora, mas sem saber onde e em que momento do mundo ele está.
- Pode ser explicitamente declarado pelo programador em formato UTC.
- Exemplo: `2025-05-27 15:00:00` (hora sem fuso definido)

```python
from datetime import datetime, timezone, timedelta

# Naive
naive_dt = datetime(2025, 5, 27, 15, 0, 0)

# Aware (com fuso de -3h, ex: Brasília)
aware_dt = datetime(2025, 5, 27, 15, 0, 0, tzinfo=timezone(timedelta(hours=-3)))
```

# Tipos disponíveis

*Todos são **`class .datatime`** 

- date
    - Classe do tipo **naive** que assume o calendário gregroriano que tem como atributos **`year`**, **`month`** e **`day`**
- time
    - Assume que cada dia tem exatamente 24*60*60 e seus atributos são  [`year`](https://docs.python.org/3/library/datetime.html#datetime.datetime.year), [`month`](https://docs.python.org/3/library/datetime.html#datetime.datetime.month), [`day`](https://docs.python.org/3/library/datetime.html#datetime.datetime.day), [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute), [`second`](https://docs.python.org/3/library/datetime.html#datetime.datetime.second), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond), e [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo).
- datetime
    - Combinação de data e hora: Atributos: [`year`](https://docs.python.org/3/library/datetime.html#datetime.datetime.year), [`month`](https://docs.python.org/3/library/datetime.html#datetime.datetime.month), [`day`](https://docs.python.org/3/library/datetime.html#datetime.datetime.day), [`hour`](https://docs.python.org/3/library/datetime.html#datetime.datetime.hour), [`minute`](https://docs.python.org/3/library/datetime.html#datetime.datetime.minute), [`second`](https://docs.python.org/3/library/datetime.html#datetime.datetime.second), [`microsecond`](https://docs.python.org/3/library/datetime.html#datetime.datetime.microsecond), e [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo).
- timedelta
    - Expressão da duração da diferença entre dois **`timedelta`** ou **`data`** resolução de microsegundos
- tzindo
    - Uma classe que implementa a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo)classe base abstrata como um deslocamento fixo do UTC.

## Timedelta

O time delta é uma diferença no tempo e um tipo de objeto próprio. Ele deve ser utilizado quando temos que fazer operações com data

```python
from datetime import datetime, timedelta

agora = datetime.now()
mais_5-dias = agora + timedelta(days=5)

print(mais_5_dias)
```

Quando temos realizamos a diferença entre dois objetos do tipo `datetime` a saída é um objeto do tipo `deltatime` 

```python
from datetime import datetime

hoje = datetime.now()
evento = datetime(2025, 5, 31, 0, 0, 0)

tempo_rest = evento - hoje  # Isso é um timedelta

print(f"Faltam {tempo_rest.days} dias e {tempo_rest.seconds//3600} horas para o evento.")
```

## Propriedades comuns

Os objetos date, datetime, time e timezone são

- Imutavéis
- hashados portanto podem ser usados como chaves de dicionário
- tem suporte a pickling via módulo pickle n
- Suportam operações matemáticas e lógicas: `+ - * / //`  ,  `or and not ==`

```python
# OPERÇÃO ARITMÉTICA
ano = timedelta(days=365)

dez_anos = 10 * ano

print(dez_anos)

nove_anos = dez_anos - ano
print(nove_anos)

tres_anos = nove_anos // 3
print(tres_anos)
```

```python
# OPERAÇÃO LÓGICA
year = timedelta(days=365)

another_year = timedelta(weeks=40,
days=84,hours=23,
minutes=50,seconds=600)

print(year == another_year)

print(year.total_seconds())
```

# Funcionalidades

Podemos formatar os padrões defaut para os padrões que queremos utilizando o método `strftime()` 

```python
import datetime

data = datetime.datetime.now()

# Formatar a data no padrão brasileiro: dia/mês/ano hora:minuto:segundo
data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)
```

```python
from datetime import datetime

data = datetime.now()

aniversario = datetime(2025, 7, 26, 22, 0, 0)

delta = aniversario - data

print(f"Faltam {delta.days} dias e {delta.seconds//3600} horas.")
```