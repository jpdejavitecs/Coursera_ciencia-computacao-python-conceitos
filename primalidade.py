p = int(input("Digite um número inteiro: "))
teste = 1
cont = 0

if p < 2:
    print("não primo")
else:
    while teste <= p:
        if p % teste == 0:
            cont = cont + 1
            teste = teste + 1
        else:
            teste = teste + 1
    if cont > 2:
        print("não primo")
    else:
        print("primo")
