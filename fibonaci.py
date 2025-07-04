a, b = 0, 1
contador = 1
while contador <= 20:
    print(f"Número {contador} - Sequência: {a}")
    a, b = b,a + b
    contador += 1