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

"""

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

user = Acesso('wesley@semeq.com','1234')

print(user.email)