def exercice1():
    for i in range(1,7):
        if i % 3 == 0:
            print(f"This value {i} is multiple of 3")

def exercice2():
    contador = 10
    while (contador != -1):
        print(contador, end=' ')
        contador -= 1
    
    print("END")

def exercice3():
    mil = 0
    while (mil  < 100000):
        for i in range(101):
            print(f'Iterator {i}: {mil}')
            mil += 1000

def main():
    
    num1 = 0
    print("What exercice do you want play?")
    print("1 - Exercice 1")
    print("2 - Exercice 2")
    print("3 - Exercice 3")

    print("Enter with an value:")
    num1 = int(input())

    print("---------------")

    if num1 == 1:
        exercice1()
    elif num1 == 2:
        exercice2()
    else:
        exercice3()

main()