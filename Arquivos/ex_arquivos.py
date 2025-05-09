# EXERCÍCIOS DE ARQUIVOS

def exercice1():
    with open('arq.txt', 'a+') as arq:
        while True:
            anotacoes = input('Digite qualquer conteúdo ou 0 para sair: ')
            if anotacoes != '0':
                arq.write(anotacoes + '\n')
            else:
                break
        arq.seek(0)  
        print("Conteúdo atual do arquivo:")
        print(arq.read())


def exercice2():
    vogais = 0
    with open('arq.txt', 'r') as arq:
        for linha in arq:
            for i in linha.lower():
                if i in 'aeiou':
                    vogais += 1
    print(f'A quantidade de vogais presentes no arquivo é: {vogais}')


def exercice3():
    with open('arq.txt', 'r') as arq:
        linhas = arq.readlines()
        print(f'A quantidade de linhas do arquivo é: {len(linhas)}')


def main():
    print("Qual exercício você deseja executar?")
    print("1 - Exercício 1 (Escrever e ler arquivo)")
    print("2 - Exercício 2 (Contar vogais)")
    print("3 - Exercício 3 (Contar linhas)")

    try:
        num1 = int(input("Digite o número do exercício: "))
        print("---------------")

        if num1 == 1:
            exercice1()
        elif num1 == 2:
            exercice2()
        elif num1 == 3:
            exercice3()
        else:
            print("Número inválido. Escolha 1, 2 ou 3.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


main()
