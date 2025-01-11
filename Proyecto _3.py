texto_ingresado = input("Ingresa un texto: ").lower()
letra_1 = input("Ingresa la primera letra: ").lower()
letra_2 = input("Ingresa la segunda letra: ").lower()
letra_3 = input("Ingresa la tercera letra: ").lower()

lista_letras = list([letra_1,letra_2,letra_3])


##Veces que aparece la letra en el texto

print(f"\nLa letra {letra_1} aparece: {texto_ingresado.count(letra_1)} veces")
print(f"La letra {letra_2} aparece {texto_ingresado.count(letra_2)} veces")
print(f"La letra {letra_3} aparece {texto_ingresado.count(letra_3)} veces\n")

##Palabras a lo largo del texto

longitud_texto = len(texto_ingresado)
print(f"La longitud total del texto ingresado es: {longitud_texto}")


##Informar de la primera letra y la ultima

primera_letra = texto_ingresado[0]
ultima_letra = texto_ingresado[-1]

print(f"La primera palabra del texto introducido es: {primera_letra} y la ultima letra es: {ultima_letra}")

##Texto al reves

print(f"\nTexto al reves: {texto_ingresado[::-1]}")

##Aparece la palabra Python

aparicion = "python" in texto_ingresado
print(f"La palabra python aparece: {aparicion}")











