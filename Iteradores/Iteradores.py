"""
# CRIANDO UM ITERADOR

def meu_for(iterável):
    it = iter(iterável)
    while True:
        try: 
            print(next(it))
        except StopIteration:
            break

meu_for('Wesley Henrique Batista SantAnna')
meu_for([x for x in range(1,101)])

# -------------------------------------------------------------

# CRIANDO MEU PROPRIO ITERADOR

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
    
con = Contador(1,6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# ------------------------------------------------


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

#SEGUNDA EXECUÇÃO: RANGE
for i in range(1,61):
    print(i)

# -------------------------------------------------------------

# GERADORES

def contador(limite):
    for i in range(1, limite + 1):
        yield i

for n in contador(3):
    print(n)

# --------------------------------------------------------------


# USO DE MEMÓRIA

# UTILIZAÇÃO DE LISTAS OU CONJUTOS QUE NÃO SÃO TUPLAS (GERADORES)
def fib_list(valor):
    lista = []
    a, b = 0, 1
    while len(lista) < valor:
        lista.append(b)
        a, b = b, a + b
    return lista

for n in fib_list(0):
    print(n)

# UTILIZANDO GERADORES
def fib_gen(valor):
    a, b, contador = 0, 1, 0
    while contador < valor:
        a, b = b, a + b
        yield a
        contador = contador + 1

for n in fib_gen(10000):
    print(n)

"""

