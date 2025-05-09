# Leitura e escrita de arquivos

`open()` → retorna um objeto arquivo e sua utilização requer dois argumento posicionais e um argumanto nomeado:

```python
f = open('nome do arquivo' , 'w', encoding= "utf-8")
```

- O primeiro argumento é uma string contendo o nome do arquivo ou o caminho para encontrar o arquivo
- O segundo é outra string contendo as opções de operação. Omitindo o segundo argumento por padrão será `r`:
    - `r` → quando o arquvo só vai ser lido
    - `w` → quando o arquivo so vai ser escrito
    - `r+` → quando o arquivo será lido e escrito
    - `b` → adicionando o b em qualquer um dos anterios o arquivo será aberto em modo binário
- O terceiro argumento consiste na forma de códificação de texto, o mais moderno é o utf-8 que também, por padrão, será utf-8

Exemplo:

```python
# TESTE
arq = open('texto.txt') 

print(arq)

print(type(arq))

# SAÍDA
# <_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
# <class '_io.TextIOWrapper'>
```

## Leitura

Para ler um arquivo depois de aberto utilizamos o método `read()` . O método  `read()` lê todo o conteúdo quando nenhum argumento é passado ou quando tem um valor negativo. 

```python
arq = open('texto.txt') 

print(arq.read())

# SAÍDA
# NÃO DESVIE DO CAMINHO
```

Uma vez lido o conteúdo do arquivo, o cursor se encotra no fim do arquivo, desse modo, se chamado o método arq.read() novamente, o retorna será uma string vazia. 

**OBS.:** Todo conteúdo é colocado em memória portanto se o conteúdo do arquivo é maior do que a quantidade de memória disponível vai ser lido apenas até o máximo e todo conteúdo posterior vai ser ignorado.

### Seek

O método `seek()` manipula o cursor. Que recebe um argumento de onde ele vai começar a percorrer

```python
arq = open('texto.txt') 

print(arq.read())

# NÃO DESVIE DO CAMINHO

# É importante que mantenha o foco

# Não esqueça da constância. 

# Constância é 100x melhor do que inspiração

arq.seek(5)

print(arq.read())

# DESVIE DO CAMINHO

# É importante que mantenha o foco

# Não esqueça da constância. 

# Constância é 100x melhor do que inspiração
```

### readline

O método `f.readline()` lê uma única linha do arquivo; o caractere de quebra de linha (`\n`) é mantido ao final da string, e só é omitido na última linha do arquivo, se o arquivo não terminar com uma quebra de linha. Isso elimina a ambiguidade do valor retornado; se `f.readline()` retorna uma string vazia, o fim do arquivo foi atingido. Linhas em branco são representadas por um `'\n'` – uma string contendo apenas o caractere terminador de linha.

```python
f.readline()
'Está é a primeira linha do arquivo.\n'
f.readline()
'Segunda linha do arquivo\n'
f.readline()
''
```

### readlines & laços

o método lê todas as linhas do arquivo.

```python
for line in f:
    print(line, end='')
   
'Está é a primeira linha do arquivo.\n'
'Segunda linha do arquivo\n'
```

## Escrita

Para escrita utilizamos o método `write(<string>)` 

```python
arq.write('\nSeja paciente e cauteloso') # ESCRITA EM ARQUIVOS
```

Podemos criar um arquivo diretamente do script do python caso ele não exista na declaração de abertura. Caso o arquivo já exista todo o conteúdo escrito nele anteriormente é perdido e o novo contéudo é sobrescrito.

## Boa prática

É importante usar a palavra chave `with` para trabalhar com arquivos. A vantagem é que o arquivo é fechado corretamente após o término da utilização, mesmo que uma exceção seja levantada em algum momento.

```python
with open('arquivo_de_trabalho', encoding="utf-8") as f:
    read_data = f.read()

# Podemos verificar se o arquivo foi fechado automaticamente.
f.closed
# True
```

## **Modos de Abertura:**

- **`'w'` (write):**Abre o arquivo para escrita. Se o arquivo já existir, ele é sobrescrito (seu conteúdo é apagado). Se o arquivo não existir, é criado um novo arquivo.
- **`'a'` (append):**Abre o arquivo para escrita e adiciona novos dados ao final do arquivo, sem sobrescrever o conteúdo existente. Se o arquivo não existir, ele é criado.
- **`'x'` (exclusive creation):**Cria um novo arquivo para escrita. Se o arquivo já existir, uma exceção é lançada (um erro é disparado).
- **`'r+'` (read and write):**Abre o arquivo para leitura e escrita. Se o arquivo não existir, é lançado um erro.

**Exemplos:**

```python
# Abre um arquivo para escrita, sobrescrevendo o conteúdo existente
arquivo = open("meu_arquivo.txt", "w")
arquivo.write("Este é um novo conteúdo.\n")
arquivo.close()

# Abre um arquivo para adicionar ao final, sem sobrescrever
arquivo = open("meu_arquivo.txt", "a")
arquivo.write("Adicionando mais texto.\n")
arquivo.close()

# Abre um arquivo para leitura e escrita, se existir
try:
    arquivo = open("meu_arquivo.txt", "r+")
    arquivo.write("Modificando o arquivo.\n")
    arquivo.seek(0) # Posição para ler a partir do início
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
except FileNotFoundError:
    print("Arquivo não encontrado.")
```

## Recursos

### StringIO

Podemos fazer a utilização de um recurso chama StringIO que permite a leitura e escrita de dados em memória sem a necessidade de ter acesso ao disco

```python
# StringIO

from io import StringIO as st

mensagem = 'Colocando em prática utilização do módulo StringIO'

arq = st(mensagem)

arq.write('\nQue permite a manipulação de arquivo via memória')

arq.seek(0)

print(arq.read())
```

### Sistema de  Arquivos: Navegação e Manipulação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos utilizar o módulo OS. Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes de sistema operacional.

```python

```

⚠️ No Windows, use **barras invertidas duplas** (`\\`) ou **strings brutas** (`r"C:\caminho"`):

```python
python
CopiarEditar
os.chdir(r"C:\Users\SeuUsuario\Documents")
```

### Funções úteis do módulo `os.path` para código multiplataforma

| Função | Descrição |
| --- | --- |
| `os.path.join()` | Junta partes do caminho com o separador correto |
| `os.path.abspath()` | Retorna o caminho absoluto |
| `os.path.exists()` | Verifica se o caminho existe |
| `os.path.isdir()` | Verifica se é uma pasta |
| `os.path.isfile()` | Verifica se é um arquivo |
| `os.path.split()` | Separa caminho e arquivo |
| `os.path.basename()` | Pega apenas o nome do arquivo |
| `os.path.dirname()` | Pega apenas o caminho (sem o nome do arquivo) |

### CROSS-PLATAFORM

**"Cross-platform" (ou multiplataforma)** significa escrever código que **funciona igualmente bem em diferentes sistemas operacionais**, como Windows, macOS e Linux — **sem precisar de mudanças** no código-fonte.

### Problema: Separadores de caminho diferentes

Cada sistema operacional usa um **separador de diretório diferente**:

- **Windows**: usa **barra invertida** (`\`)
- **Linux/macOS**: usam **barra normal** (`/`)

### Exemplo incorreto (não portável):

```python
python
CopiarEditar
# Funciona no Windows, mas pode quebrar no Linux
arquivo = "C:\\Users\\Usuario\\documento.txt"
```

### Exemplo correto e portável:

```python
python
CopiarEditar
import os

arquivo = os.path.join("C:", "Users", "Usuario", "documento.txt")
```

O `os.path.join()` **automaticamente usa o separador correto** para o sistema onde o script está rodando. Isso é a chave do comportamento cross-platform.