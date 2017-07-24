n = int(input("Digite o valor de n: "))
aux = n
fat = False

if n == 0:
    n = n + 1
    print(n)
else:
    n = n - 1
    while fat == False:
        if n > 1:
            aux = aux * n
            n = n - 1
        else:
            fat = True
    print(aux)
