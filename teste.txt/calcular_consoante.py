def f_consoante(a):
	consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
	contador =0
	for letra in a:
		if letra in consoantes:
			contador+=1
	return contador
def main ():
	nomes_lista=["Ana","Bruno","Carlos","Daniela","Eduardo","Fernanda","Gabriel","Helena","Igor","Juliana","Lucas","Mariana","Nicolas","Olivia","Paulo","Quintino","Rafaela","Sergio","Tatiana","Victor"]
	for nome in nomes_lista:
		lista = f_consoante(nome)
		print(f"Nome: {nome}, Consoantes: {lista}")
if __name__ == '__main__':
	main()

