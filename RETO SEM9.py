#Actividad RETO 9. Funciones

# Programa con un bucle infinito que solicite al usuario una letra (debe especificar
# al usuario la condición para terminar el programa. Para salir presione enter).
# 2. # Hacer una función que imprima en la pantalla la letra siguiente en el
# alfabeto y la letra anterior a la ingresada.
# 3. # El programa debe continuar en el bucle hasta que el usuario decida
# salir del programa.

def letras_adyacentes(letra):
    """Función que recibe una letra y devuelve la letra anterior y la siguiente en el alfabeto.
    Si la letra es 'a' o 'z', maneja los casos especiales."""
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    if letra in abecedario:
        indice = abecedario.index(letra)
        letra_anterior = abecedario[indice - 1] if indice > 0 else 'No hay letra anterior'
        letra_siguiente = abecedario[indice + 1] if indice < len(abecedario) - 1 else 'No hay letra siguiente'
        return letra_anterior, letra_siguiente
    else:
        return None, None
while True:
    letra = input("Ingrese una letra (presione Enter para salir): ").lower()
    if letra == "":
        print("Saliendo del programa.")
        break
    letra_anterior, letra_siguiente = letras_adyacentes(letra)
    if letra_anterior is not None:
        print(f"La letra anterior a '{letra}' es: {letra_anterior}")
        print(f"La letra siguiente a '{letra}' es: {letra_siguiente}")
    else:
        print("Por favor, ingrese una letra válida del alfabeto.")