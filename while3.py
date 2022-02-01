x = 0
while x < 10:
    if x == 5:
        x = x + 1
        continue #O número 5 é pulado e continua a conta

    print(x)
    x = x + 1


print("FIM")

y = 0
while y < 10:
    if y == 5:
        y = y + 1
        break #Não pula o número 5, mas para antes de chegar nele

    print(y)
    y = y + 1

a = 0 #coluna
b = 0 #linha

while a < 10:
    print(a)
    a += 1 # É uma forma simpificada de escrever a = a + 1

print("FIM")
