def esBinario(binario):
	for comprueba in binario:
		if int(comprueba) != 0 or int (comprueba) != 1:
			return True
		else:
			return False


binario = input("Escribe un número binario para pasarlo a decimal: ")

#main

if esBinario(binario):
	try:
		decimal = int(binario,2)
		print = ("El número binario introducido es: " + binario + "y su conversion: " + str(decimal))

	except ValueError:
		print("No has introducido un número binario")