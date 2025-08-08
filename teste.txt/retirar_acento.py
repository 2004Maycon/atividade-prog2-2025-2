def main():
	txt=(input("qual texto quer que seja removido os acentos?  ")).upper()
	alterado =""
	for i in range(len(txt)):
		if txt[i] == "Á" or txt[i] == "À"  or txt[i] == "Â" or txt[i] == "Ã":
			alterado+="A" 
		elif txt[i] == "É" or txt[i] == "È"  or txt[i] == "Ê":
			alterado +="E"
		elif txt[i] == "Í" or txt[i] == "Ì"  or txt[i] == "î":
			alterado +="I "
		elif txt[i] == "Ó" or txt[i] == "Ò"  or txt[i] == "Ô" or  txt[i] == "Õ":
			alterado += "O "
		elif txt[i] == "Ú" or txt[i] == "Ù"  or txt[i] == "Û":
			alterado +="U"
		else:
			alterado +=txt[i]
	
	print(f"texto original: {txt}")
	print(f"texto alterado: {alterado}")
main()