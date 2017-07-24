n = int(input("Digite um número inteiro: "))
soma = n % 10

while n > 0:
    n = n // 10
    soma = soma + (n % 10)

print(soma)
