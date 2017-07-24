
a = float(input("Digite A: "))
b = float(input("Digite B: "))
c = float(input("Digite C: "))

delta = b**2 - 4 * a * c

if (delta < 0):
    print("esta equação não possui raízes reais")
else:
    if (delta == 0):
        r = -b / (2 * a)
        print("a raiz desta equação é ", r)
    else:
        x1 = (-b + delta**0.5) / (2 * a)
        x2 = (-b - delta**0.5) / (2 * a)
        if x1 < x2:
            print("as raízes da equação são ", x1, " e ", x2)
        else:
            print("as raízes da equação são ", x2, " e ", x1)
