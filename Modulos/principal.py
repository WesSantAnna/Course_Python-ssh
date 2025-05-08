import Modulos.MeuModulo as MeuModulo

MeuModulo.mostrar_mensagem() # acessa a função

print(MeuModulo.mensagem) # acessa a veriável

#---------------------------------------------------------------

# GERANDO SOBRESCRITA
mensagem = "Eu não serei executado"

from Modulos.MeuModulo import mensagem

print(mensagem) # SERÁ SOBRESCRITA

