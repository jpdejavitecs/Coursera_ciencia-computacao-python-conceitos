def remove_repetidos(lista):
    i = 0
    while i < len(lista):
        ctrl = -len(lista) + (i + 1)
        if lista[i] in lista[ctrl:-1]:
            del lista[i]
            i -= 1
        i += 1
    return sorted(lista)