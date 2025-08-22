def F_maior(lst):
	maior = -9999
	for numero in lst:
		if numero > maior:
			maior = numero
	return maior
def F_menor(lst):
	menor = 9999
	for numero in lst:
		if numero < menor:
			menor = numero
	return menor
def main():
	lista = [1, 2, 3, 4, 5]
	numero_maior = F_maior(lista)
	numero_menor = F_menor(lista)
	print(f"esse é o maior da lista {numero_maior}")
	print(f"esse é o menor numero da lista {numero_menor}")
	return 0
main()