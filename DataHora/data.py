"""
import datetime

print(datetime.MAXYEAR) # MAXIMO DE ANO SUPORTADO

print(datetime.MINYEAR) # MINIMO DE ANO SUPORTADO

print(datetime.datetime.now()) # MOSTRA A HORA DE AGORA


from datetime import datetime, timezone, timedelta

# Naive
naive_dt = datetime(2025, 5, 27, 15, 0, 0)

# Aware (com fuso de -3h, ex: Brasília)
aware_dt = datetime(2025, 5, 27, 15, 0, 0, tzinfo=timezone(timedelta(hours=-3)))

#-----------------------------------------------------------------------------------

# OPERAÇÃO LÓGICA
year = timedelta(days=365)
another_year = timedelta(weeks=40,days=84,hours=23,
                         minutes=50,seconds=600)

print(year == another_year)

print(year.total_seconds())

# ----------------------------------------------------------------------------------

# OPERÇÃO ARITMÉTICA
ano = timedelta(days=365)

dez_anos = 10 * ano

print(dez_anos)

nove_anos = dez_anos - ano
print(nove_anos)

tres_anos = nove_anos // 3
print(tres_anos)

# -------------------------------------------------------------------------------
# FORMATAÇÃO DEFAOUT
data = datetime.datetime.now()

# Formatar a data no padrão brasileiro: dia/mês/ano hora:minuto:segundo
data_formatada = data.strftime('%d/%m/%Y %H:%M:%S')

print(data_formatada)

# -----------------------------------------------------------------------------------


from datetime import datetime

data = datetime.now()

aniversario = datetime(2025, 7, 26, 22, 0, 0)

delta = aniversario - data

print(f"Faltam {delta.days} dias e {delta.seconds//3600} horas.")

# ----------------------------------------------------------------------------------------------

from datetime import datetime, timedelta

agora = datetime.now()

mais_5_dias = agora + timedelta(days=5)

print(mais_5_dias.strftime('%d/%m/%Y'))

# A DIFERENÇA ENTRE DOIS OBJETOS DATATIME

from datetime import datetime

hoje = datetime.now()
evento = datetime(2025, 5, 31, 0, 0, 0)

fantaria = evento - hoje  # Isso é um timedelta

print(f"Faltam {fantaria.days} dias e {fantaria.seconds // 3600} horas para o fantaria.")
"""





