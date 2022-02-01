contador = 1
acumulador = 1

while contador <= 10:
    print("Contador = ", contador)
    print("Acumulador = ", acumulador)
    print()
    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1

else:
    print("FIM")
print("Break")