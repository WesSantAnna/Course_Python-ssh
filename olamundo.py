valores = [0,0,0]
soma = 0
square = [0,0,0]
for i in range(len(valores)):
    valores[i] = int(input("Digite um valor inteiro: "))
    soma += valores[i]
    square[i] = pow(valores[i],2)

print(f'a soma dos valores são {soma} e o quadrado dos valores originais são: {square}')