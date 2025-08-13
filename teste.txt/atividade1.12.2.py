def main():
	
	quanti_h = 0
	quanti_m = 0
	soma_f =0
	altura_total_menor = 9999
	altura_total_maior = -9999
	for i in range(5):
		sexo = input("qual e seu sexo f ou m ")
		if  sexo == "f" or sexo =="m":
			altura =float(input("qual a sua altura "))
			if sexo == "m":
				quanti_h +=1
			elif sexo == "f":
				soma_f += altura
				quanti_m +=1
			if altura > altura_total_maior:
				altura_total_maior = altura
			if altura < altura_total_menor :
				altura_total_menor = altura
		else:
			print("sexo invalido")
	media= soma_f / quanti_m 
	print(f"------------------------------------------------------------------------------------")
	print(f" menor altura= {altura_total_menor:.2f} ,maior e altura {altura_total_maior:.2f}")
	print("_____________________________________")
	print(f"media feminina = {media :.2f}")
	print("_____________________________________")
	print(f"quantidade de homem {quanti_h}")
main()