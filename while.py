"""
    while True:
    nome = input("Digite seu nome: ")
    print("Olá,",nome)
"""

x = input("Digite um número: ")

while x.isdigit():
    x = int(x)
    print(x)
    break
else:
    print("Você não digitou um número inteiro")



