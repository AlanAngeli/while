frase = "Aranha arranha o jarro"
tamanho_frase = len(frase)
contador = 0
nova_str = ""

print("A frase compõe", tamanho_frase, "caracteres")

while contador < tamanho_frase:
    nova_str += frase[contador]
    print(nova_str)
    contador += 1


##################################
print()
print()

frase2 = "A joaninha subiu pela parede"
tamanho_frase2 = len(frase2)
contador2 = 0
nova_str2 = ""

while contador2 < tamanho_frase2:
    letra =  frase2[contador2]
    if letra == "a":
        nova_str2 += "A"
    else:
        nova_str2 += letra
    contador2 += 1

print(nova_str2)

