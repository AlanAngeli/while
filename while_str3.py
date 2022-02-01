frase = "A joaninha subiu pela parede"
tamanho_frase = len(frase)
contador = 0
nova_str = ""
usuario_input = input("Qual letra deseja colocar maiúscula? ")

while contador < tamanho_frase:
    letra =  frase[contador]
    if letra == usuario_input:
        nova_str += usuario_input.upper()
    else:
        nova_str += letra
    contador += 1

print(nova_str)