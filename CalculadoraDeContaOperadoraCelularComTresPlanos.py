# CONTA DE TELEFONE COM 3 FAIXAS DE PREÇO
# Os planos da empresa Tchau são bem interessantes e oferecem preços diferenciados de acordo com a quantidade de minutos
# usados por mês. Abaixo de 200 minutos a empresa cobra 0.20
# Entre 200 e 400 minutos , a empresa cobra 0.18
# Acima de 400 o preço por minuto é de 0.15

minuto = int(input("Quantos minutos você utilizou?: \n"))
preco = 0
if minuto < 200:
	preco = minuto * 0.20
	print(f"O total a pagar é {preco}")

if minuto >= 200 and minuto <=400:
    preco = minuto * 0.18
    print(f'O total a pagar é {preco}')

if minuto > 400:
    preco = minuto * 0.15
    print(f'O total a pagar é: {preco}')
