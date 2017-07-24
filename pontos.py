x1 = int(input("Digite um numero para X: "))
y1 = int(input("Digite um numero para Y: "))
x2 = int(input("Digite um numero para X: "))
y2 = int(input("Digite um numero para Y: "))


distancia = ((y2 - y1)**2 + (x2 - x1)**2)

if distancia < 0:
    distancia = distancia * -1
    distancia = distancia**0.5
else:
    distancia = distancia**0.5

    
if distancia <= 10:
        print("perto")
else:
        print("longe")

