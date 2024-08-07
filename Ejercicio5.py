def sumar_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def multiplicar_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

# Ejemplo de uso
lista_suma = [1, 2, 3, 4]
resultado_suma = sumar_lista(lista_suma)
print(f"La suma de los números en la lista es: {resultado_suma}")

lista_multip = [1, 2, 3, 4, 5]
resultado_multip = multiplicar_lista(lista_multip)
print(f"El producto de los números en la lista es: {resultado_multip}")
