"""
# PROBLEMAS
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        '''Eu sou uma função (logar) dentro de outra'''
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui fica a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    '''Soma dois números'''
    return a + b

# SAÍDA ESPERADA
print(soma(10,20))   # 30
print(soma.__name__) # soma
print(soma.__doc__)  # Soma dois números

# SAÍDA OBTIDA
# Você está chamando soma
# Aqui fica a documentação: Soma dois números
# 30
# soma
# Soma dois números

"""
def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args,**kwargs)
        return converter
    return decorador

@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(int(vezes)):
        print(msg)

repete_msg('Mensagem repitida', '3')

@forca_tipo(float,float)
def dividir(a, b):
    print(a / b)

dividir(4,5)

