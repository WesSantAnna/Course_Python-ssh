
"""
# SINTAXE
class NomeClasse:
<instrução 1>
.
.
.
<instrução N>
# ------------------------------------------------------

# OBJETO CLASSE

class MinhaClasse:
    '''Um exemplo de classe simples'''
    i = 12345

    def f(self):
        return 'olá mundo'

x = MinhaClasse()

def __init__(self):
	self.data = []

x = MinhaClasse()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i

# SAÍDA
# (3.0, -4.5)

#---------------------------------------------------------


# ------------------------------------------------------------

class Cachorro:
    tipo = 'canino'
    def __init__(self, nome):
        self.nome = nome

d = Cachorro('Frido')
e = Cachorro('Buddy')

print(e.tipo)
print(d.tipo)

print(d.nome)
print(e.nome)

# ------------------------------------------------------------

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

user = Acesso('wesley@semeq.com','1234')

print(user.email)
print(user.__senha)


# -------------------------------------------------------------------

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

# ---------------------------------------------------------

from passlib.hash import pbkdf2_sha256 as cryp
        
class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
         print(f'Temos {cls.contador} usuários no sistema')


    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200000, salt_size = 16)
        Usuario.contador = self.__id

    def nome_completo(self):
            return f'{self.__nome} {self.__sobrenome}'
        
    def check_senha(self, senha):
            if cryp.verify(senha, self.__senha):
                return True
            return False
        

user = Usuario('Wesley','SantAnna','wesley@semeq.com','123456')
user2 = Usuario('Fernanda','Batista','fernanda@exemplo.com','456123')

Usuario.conta_usuario()

# ------------------------------------------------------------------------------

# ABSTRAÇÃO E ENCAPSULAMENTO
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

# --------------------------------------------------------------------
# EXEMPLO BANCÁRIO

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
"""

