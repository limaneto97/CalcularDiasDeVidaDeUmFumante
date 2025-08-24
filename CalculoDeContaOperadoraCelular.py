# O programa calcula o custo mensal de um plano de celular da operadora TCHAU.
# Solicita os Dados: Pede ao usuário que informe seu plano (falopouco ou falomuito)
# e a quantidade total de minutos que utilizou.
# Verifica o Plano:
# Se for "falopouco": O custo base é de R$ 50. Se os minutos ultrapassarem 100,
# é adicionado R$ 0,20 por cada minuto excedente.
# Se for "falomuito": O custo base é de R$ 99. Se os minutos ultrapassarem 500,
# é adicionado R$ 0,15 por cada minuto excedente.
# Se não for nenhum dos dois: O programa não faz nada.
# Exibe o Resultado: Imprime o valor final a ser pago.

plano = input('Qual o seu plano?: \n')
minutos = int(input('Quantos minutos você utilizou?: \n'))

minutos_extra = 0
valor_extra = 0
valor_total = 0
precofalopouco = 50
precofalomuito = 99
minutosfalopouco = 100
minutosfalomuito = 500
extrafalopouco = 0.20
extrafalomuito = 0.15

if plano == "falopouco" and minutos <= minutosfalopouco:
    print(f'\nO seu plano é {plano}, o total a pagar é: {precofalopouco}.')

if plano == "falopouco" and minutos > minutosfalopouco:
    minutos_extra = minutos - minutosfalopouco
    valor_extra = minutos_extra * extrafalopouco
    valor_total = precofalopouco + valor_extra
    print(f'\nO seu plano é {plano}, o total a pagar é: {valor_total}.')

if plano == "falomuito" and minutos <= minutosfalomuito:
    print(f'\nO seu plano é {plano}, o total a pagar é: {precofalomuito}.')

if plano == "falomuito" and minutos > minutosfalomuito:
    minutos_extra = minutos - minutosfalomuito
    valor_extra = minutos_extra * extrafalomuito
    valor_total = precofalomuito + valor_extra
    print(f'\nO seu plano é {plano}, o total a pagar é: {valor_total}.')
else:
    print(f"\nPLANO INVÁLIDO! Digite o plano correto 'falopouco' ou 'falomuito'.")
