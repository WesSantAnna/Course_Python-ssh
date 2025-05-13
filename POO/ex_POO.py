class Pessoa:
    def __init__(self, nome, data_nascimento, email):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.email = email
    
    def ver_dados(self):
        return f'{self.nome}\n{self.data_nascimento}\n{self.email}'

class Contato:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, numero):
        contato = Contato(nome, numero)
        self.contatos.append(contato)

    def ver_contatos(self):
        if not self.contatos:
            print("Nenhum contato na agenda.")
        else:
            for i, contato in enumerate(self.contatos, 1):
                print(f'{i}: Nome: {contato.nome}, Telefone: {contato.numero}')
    
    def remover_contato(self):
        self.ver_contatos()
        try:
            valor = int(input("Digite o número do contato que deseja remover: "))
            if 1 <= valor <= len(self.contatos):
                del self.contatos[valor - 1]
                print("Contato removido com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
        self.ver_contatos()

    def buscar_contato(self):
        nome = input('Digite o nome que deseja buscar: ')
        encontrados = [c for c in self.contatos if c.nome.lower() == nome.lower()]
        if encontrados:
            for c in encontrados:
                print(f'Nome: {c.nome}, Telefone: {c.numero}')
        else:
            print('O contato não foi encontrado.')

# Exercício 1: Pessoa
def exercice1():
    nome = input('Digite seu nome: ')
    data = input('Digite sua data de nascimento (DD/MM/YY): ')
    email = input('Digite seu email: ')
    user = Pessoa(nome, data, email)
    print(f'Aqui são apresentados os dados do usuário:\n{user.ver_dados()}')

# Exercício 2: Agenda de contatos
def exercice2():
    agenda = Agenda()
    while True:
        print("\nEscolha uma operação:")
        print("1 - Adicionar contato")
        print("2 - Remover contato")
        print("3 - Buscar contato")
        print("4 - Ver contatos")
        print("0 - Voltar")

        try:
            op = int(input("Opção: "))
            if op == 1:
                nome = input("Nome: ")
                numero = input("Número: ")
                agenda.adicionar_contato(nome, numero)
            elif op == 2:
                agenda.remover_contato()
            elif op == 3:
                agenda.buscar_contato()
            elif op == 4:
                agenda.ver_contatos()
            elif op == 0:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida.")


def main():
    print("Qual exercício você deseja executar?")
    print("1 - Exercício 1 (Pessoa)")
    print("2 - Exercício 2 (Agenda de Contatos)")
    print("3 - Exercício 3 (Televisão)")

    try:
        num1 = int(input("Digite o número do exercício: "))
        print("---------------")

        if num1 == 1:
            exercice1()
        elif num1 == 2:
            exercice2()
        else:
            print("Número inválido. Escolha 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

main()
