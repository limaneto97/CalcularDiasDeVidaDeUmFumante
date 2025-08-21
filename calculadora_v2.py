import time

print("\n******************* Python Calculator *******************")

def somar(x, y):
	"""Esta função soma dois números"""
	return x + y

def subtrair(x, y):
	"""Esta função subtrai dois números"""
	return x - y

def multiplicar(x, y):
	"""Esta função multiplica dois números"""
	return x * y

def dividir(x, y):
	"""Esta função divide dois números"""
	return x / y

print("--- Bem-vindo à Calculadora Python ---")

while True:
	print("Escolha a operação: ")
	print("1 - somar")
	print("2 - subtrair")
	print("3 - multiplicar")
	print("4 - dividir")
	print("5 - sair")

	escolha = input("Digite a operação desejada: ")

	if escolha == "5":
		print("Saindo da calculadora...")
		time.sleep(1.5)
		print("Até a próxima!")
		time.sleep(1)
		break

	if escolha in ["1", "2", "3", "4"]:

		numero1 = int(input("Digite o primeiro número: "))
		numero2 = int(input("Digite o segundo número: "))

		if escolha == "1":
			print("\nOk, vamos somar!")
			time.sleep(1.5)
			print("O resultado da soma é: ", somar(numero1, numero2))
			time.sleep(1.5)

		elif escolha == "2":
			print("\nOk, vamos subtrair!")
			time.sleep(1.5)
			print("O resultado da subtração é: ", subtrair(numero1, numero2))
			time.sleep(1.5)

		elif escolha == "3":
			print("\nOk, vamos multiplicar!")
			time.sleep(1.5)
			print("O resultado da multiplicação é: ", multiplicar(numero1, numero2))
			time.sleep(1.5)

		elif escolha == "4":
			print("\nOk, vamos dividir!")
			time.sleep(1.5)
			if numero2 == 0:
				print("Não é possível dividir o número por 0!")
			else:
				print("O resultado da divisão é:", dividir(numero1, numero2))
			time.sleep(2)
	else:
		print("\nOpção inválida! Por favor, escolha um número de 1 a 5.")
		time.sleep(1.5)