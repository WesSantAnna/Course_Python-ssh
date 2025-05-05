
import math as mt

def exercicio1():
    num1 = 0;
    num2 = 0

    print("Enter with an real value: ")

    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        print(f'The biggest value is:{num1}')
    else:
        print(f'The second value "{num2}" is the biggest')

def exercicio2():
  num1 = 0
  print("Enter with an real value:")
  num1 = int(input())
  if num1 > 0:
      root = mt.sqrt(num1)
      print(f'The square root of the number is: {root}')
  else:
      print("The value entered ins't a positive value!")

def exercicio3():
    num1 = 0

    print("Enter with an real value:")
    num1 = int(input())

    if num1 % 2 == 0:
        print("This is a even value")
    else:
        print("This odd value")


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
        exercicio1()
    elif num1 == 2:
        exercicio2()
    else:
        exercicio3()

    
main()