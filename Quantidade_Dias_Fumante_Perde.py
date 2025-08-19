# ESCREVA UM PROGAMA PARA CALCULAR A REDUÇÃO DE TEMPO DE VIDA DE UM FUMANTE.
# PERGUNTE A QUANTIDADE DE CIGARROS FUMADOS POR DIA E QUANTOS ANOS ELE JÁ FUMOU
# CONSIDERE QUE UM FUMANTE PERDE 10 MINUTOS DE VIDA A CADA CIGARRO
# CALCULE QUANTOS DIAS DE VIDA UM FUMANTE PERDERÁ
# EXIBA O TOTAL EM DIAS
import time
cigarro_dia = int(input('Quantos cigarros fumados por dia?: \n'))
time.sleep(1.5)
anos_fumados = int(input('Há quantos anos você fuma?: \n'))
time.sleep(1.5)
total_cigarros = cigarro_dia * (anos_fumados * 365)
minutos_perdido_cigarro = total_cigarros * 10
dias_perdidos = (minutos_perdido_cigarro / 60) / 24
print(f'O total em dias que você perdeu é: {dias_perdidos}')
