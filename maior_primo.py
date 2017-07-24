def maior_primo(x):
    teste = 1
    cont = 0
    primalidade = False
    if x < 2:
            primalidade = True
            return 0
    else:
        while primalidade == False:
            while teste <= x:
                if x % teste == 0:
                    cont = cont + 1
                    teste = teste + 1
                else:
                    teste = teste + 1
            if cont > 2:
                primalidade = False
                x = x - 1
                teste = 1
                cont = 0
            else:
                primalidade = True
                return x

