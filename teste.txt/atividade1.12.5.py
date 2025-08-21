def main():
	populaçao_A=90000000
	populaçao_B =20000000
	i = 0
	while populaçao_B <= populaçao_A:
		populaçao_A=populaçao_A*1.03
		populaçao_B=populaçao_B*1.015
		i+= 1 
	print(f"populaçao_A {populaçao_A :.2f}")
	print(f"populaçao_B {populaçao_B :.2f}")
	print(f"anos de duração: {i}")
main()