class Robo:
    def __init__(self, nome, bateria = 100, habilidade = []):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidade = habilidade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def bateria(self):
        return self.__bateria
    
    @property
    def habilidade(self):
        return self.__habilidade
    
    def carregar(self):
        self.__bateria = 100

    def fala_nome(self):
        if self.__bateria > 0:
            self.__bateria = self.__bateria -1
            return f'BEP BOOP. EU SOU {self.__nome.upper()}'
        return f'Bateria fraca, Por favor recarregue'
    
    def aprender_habilidades(self, nova_habilidade, custo):
        if self.__bateria >= custo:
            self.__bateria = self.__bateria - custo
            self.__habilidade.append(nova_habilidade)
            return f'Habilidade nova carregada'
        return f'Bateria insuficiente'
    
