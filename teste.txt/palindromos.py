def main():
	txt = input("digite a palavra :")
	aux = ""
	for i in range(len(txt)-1,-1,-1):
		aux +=txt[i]
	if txt == aux:
		print(f"{txt} é um palindromos")
	else:
		print(f"{txt} não é um palindromos")
main()

