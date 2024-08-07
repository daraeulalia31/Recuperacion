def es_vocal(caracter):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if caracter.lower() in vocales:
        return True
    else:
        return False

# Ejemplo de uso
caracter = 'B'
resultado = es_vocal(caracter)
print(f"¿El carácter '{caracter}' es una vocal? {resultado}")