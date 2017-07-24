n = int(input("Digite o valor de n: "))
aux = 1
cont = n

while cont > 0:
    if not aux % 2 == 0:
        print(aux)
        cont = cont - 1
        aux = aux + 1
    else:
        aux = aux + 1
