n = int(input("Jogo 1: "))
aux = n
cont = 0

while aux > 0:
    n = aux % 10
    aux = aux // 10
    if aux % 10 == n:
        cont = cont + 1

if cont > 0:
    print("sim")
else:
    print("não")
