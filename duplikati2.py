def ukloni_duplikate(lista):
    nova_lista = []
    for element in lista:
        if element not in nova_lista:
            nova_lista.append(element)
    return nova_lista

# Primjer korištenja
lista = [1, 2, 2, 3, 4, 4, 5]
rezultat = ukloni_duplikate(lista)
print(rezultat)