def F_uniao(a,b):
	intercessao = []

	for i in range (len(a)):
		for j in range (len(b)):
			if a[i] == b[j]:
				intercessao.append(a[i])
	return intercessao
def main():
	lista1 = (1,2,3,4,6,8,9,11)
	lista2= (1,4,5,8,2,7,6,9,10)
	uniao = F_uniao(lista1,lista2)
	print(lista1)
	print(lista2)
	print(uniao)
	print()
	return 0
main()