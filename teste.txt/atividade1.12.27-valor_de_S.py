def main ():
	s =0
	for num in range(1,11):
		denon = num**2
		if (num%2)== 0:
			s=+num/denon
		else:
			s=-num/denon
	print(f"o valor de S: {s}")
main()