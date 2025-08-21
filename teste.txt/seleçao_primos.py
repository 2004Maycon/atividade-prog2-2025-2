def f_seleçao_primos(a):
	aux = []
	for num in a:
		if num > 1:
			primo = True
			for i in range(2,int(num**0.5)+1):
				if num % i == 0:
					lis = num
					primo = False
			if primo:
				aux.append(num)
	return aux
def main():
	lista =[42, 7, 19, 88, 56, 3, 91, 27, 64, 11]
	primos = f_seleçao_primos(lista)
	print(f"lista anterior{lista}")
	print()
	print(f"esses sao primos{primos}")
	return 0
if __name__ == '__main__':
	main()