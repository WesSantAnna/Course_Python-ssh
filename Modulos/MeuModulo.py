""" 
    mensagem = "Entre passos e tropeços"
    
    def mostrar_mensagem():
        print(mensagem)

"""

def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, sep=' ')
        a , b = b, a + b
    print()

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
