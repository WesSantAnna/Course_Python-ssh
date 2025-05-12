# SYNTAX ERRORS
# def funcao:
#   print('Gerando um erro')
#   File c:\Users\TESTE\Desktop\Python\debug.py, line 2
#     def funcao:
#               ^
# SyntaxError: expected '('

# ------------------------------------------------------------------

# EXCEPTIONS

# pritn(Gerando uma exceção do tipo NameErros)
# Traceback (most recent call last):
#   File c:\Users\TESTE\Desktop\Python\debug.py, line 7, in <module>
#     pritn(Gerando uma exceção do tipo NameErros)
#     ^^^^
# NameError: name pritn is not defined. Did you mean: print?

# TYPEERROR
# print(len(5))
# print('Type' + [])

# INDEXERROR - Para qualquer elemento que possa acessar via index
# lista = ['Testanto']
# print(lista[2])

# VALUEERROR
# print(int('Wesley'))

# KEYERROR
# dic = {'Python' : 'Course'}
# print(dic['C++'])

# ----------------------------------------------------------------------

# EXEMPLO REAL

# def color(texto, cor):
#     cores = ('Amarelo','Azul','Branco','Verde')
#     if type(texto) is not str:
#         raise TypeError('O texto precisa ser uma string')
#     if type(cor) is not str:
#         raise TypeError('A cor precisa ser uma string')
#     if cor not in cores:
#         raise ValueError(f'A cor precisa ser uma entre: {cores}')
#     print(f'O texto "{texto}" vai ser impresso na cor {cor}.')

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# try:
#     len(5)
# except TypeError as err:
#     print(f'A aplicação gerou o seguinte erro: {err}')

# --------------------------------------------------------------------

# MULTIPLOS EXCEPT

# except (RuntimeError, TypeError, NameError):
#    pass

# ---------------------------------------------------------------------
# HERANÇA

# class B(Exception): # classe genérica: trata tudo
#     pass
# 
# class C(B): # Trata somente quando o erro for C
#     pass
# 
# class D(C): # Trata somente quando o erro for D
#     pass
# 
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# ----------------------------------------------------------------------
# ELSE E FINALLY

# try: 
#     num = int(input("Informe um numero inteiro: "))
# except ValueError:
#     print('Valor incorreto')
# else:
#     print(f'O valor digitado foi: {num}')
# finally:
#     print('O bloco foi executado por completo')
# 
# -----------------------------------------------------------------------

# DEBUGANDO VIA PDB (PYTHON DEBUGER)

# def dividir(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError as err:
#         return f'Ocorreu um erro: {err}'
# 
# try:
#     num1 = int(input('Digite um valor inteiro: '))
#     num2 = int(input('Digite outro valor inteiro: '))
#     valor_recebido = dividir(num1, num2)
#     print(valor_recebido)
# except ValueError:
#     print("Você deve digitar apenas números inteiros.")
# ---------------------------------------------------------------------------