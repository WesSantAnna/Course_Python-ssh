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

"""
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