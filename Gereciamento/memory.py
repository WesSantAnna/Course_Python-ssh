"""
import sys as s

x = 10 
print(type(x))

y = x

print(id(x))
print(id(y))

class Teste:
    def __init__(self):
        pass

print(s.getsizeof(Teste))
print(s.getsizeof(int))
print(s.getsizeof(float))

# ---------------------------------------------------------
import time
from threading import Thread 

CONTADOR = 50000000

def contagem_regressiva(n):
    while n > 0:
        n = n -1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tem em segundos com uma única thread: {fim - inicio}' )



t1 = Thread(target=contagem_regressiva, args=(CONTADOR//4,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//4,))
t3 = Thread(target=contagem_regressiva, args=(CONTADOR//4,))
t4 = Thread(target=contagem_regressiva, args=(CONTADOR//4,))

inicio_mult = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
fim_mult = time.time()

print(f'Tem em segundos com uma multi thread: {fim_mult - inicio_mult}' )
"""


