largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

print(largura * '#')

altura -= 2

while altura > 0:
    print('#' + ((largura - 2) * ' ') + '#')
    altura -= 1
    
print(largura * '#')
