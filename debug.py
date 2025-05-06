# SYNTAX ERRORS
# def funcao:
#   print('Gerando um erro')
#   File c:\Users\TESTE\Desktop\Python\debug.py, line 2
#     def funcao:
#               ^
# SyntaxError: expected (
# EXCEPTIONS
# pritn(Gerando uma exceção do tipo NameErros)
# Traceback (most recent call last):
#   File c:\Users\TESTE\Desktop\Python\debug.py, line 7, in <module>
#     pritn(Gerando uma exceção do tipo NameErros)
#     ^^^^
# NameError: name pritn is not defined. Did you mean: print?

# TypeError
print(len(5))

print('Type' + [])

# IndexError - Para qualquer elemento que possa acessar via index
lista = ['Testanto']
print(lista[2])

# ValueError
print(int('Wesley'))

# KeyError
dic = {'Python' : 'Course'}
print(dic['C++'])

