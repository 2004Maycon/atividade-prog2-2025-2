def F_compare(id,al,media):
	cont = 0
	for i in range(len(id)):
		if id[i] >= 13 and al[i] < media:
			cont +=1
	return cont
def main():
	media_altura =float(0)
	j = 0
	lista_id = []
	lista_alt = []
	for i in range(30):
		idade = int(input("qual a sua idade"))
		lista_id.append(idade)
		altura = float(input("qual a sua altura"))
		lista_alt.append(altura)
		if altura != "":
			media_altura += altura
			j +=1
	media = media_altura/ j
	comparaçao = F_compare(lista_id,lista_alt,media)
	print(f"a media é {media}")
	print(f"a quantidade de pessoas de 13 anos com altura menor que a media é {comparaçao}")
	return 0
if __name__ == '__main__':
	main()
