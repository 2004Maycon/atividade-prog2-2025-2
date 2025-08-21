def main():
	produto = str(input("qual é o produto? "))
	valor_compra = 0
	valor_venda = 0
	valor_lucro = 0
	lucro = 0
	lucro_percentual = 0
	lucro_baixo = ""
	lucro_alto = ""
	lucro_medio = ""
	while produto != "":
		preço_de_compra = float(input("qual o valor de compra? "))
		preço_de_venda = float(input("qual o valor de venda? "))

		lucro = (preço_de_venda - preço_de_compra)
		lucro_percentual = (lucro/preço_de_compra)*100
		if lucro_percentual < 10:
			lucro_baixo+= produto + ","
		elif lucro_percentual >= 10 and lucro_percentual <= 20:
			lucro_medio += produto + ","
		elif lucro_percentual > 20:
			lucro_alto += produto + ","
		valor_compra += preço_de_compra
		valor_venda += preço_de_venda
		produto = str(input("qual é o produto? "))
	valor_lucro = valor_venda - valor_compra
	print(f"lucro_baixo {lucro_baixo}")
	print(f"lucro_medio {lucro_medio}")
	print(f"lucro_alto {lucro_alto}")
	print(f"Total de Compra:{valor_compra}")
	print(f"Total de Venda:{valor_venda :.2f}")
	print(f"Total de lucro:{valor_lucro :.2f}")
if __name__ == '__main__':
	main()