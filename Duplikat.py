def je_duplikat(lista, element):
    return lista.count(element) > 1

def ukloni_duplikate(lista):
    nova_lista = []
    for element in lista:
        if not je_duplikat(lista, element) or element not in nova_lista:
            nova_lista.append(element)
    return nova_lista

# Primjer korištenja
lista = [1,2,2,3,4,4,5,6,6,6,7,8,9]
rezultat = ukloni_duplikate(lista)
print(rezultat)  # Output: [1, 3, 5]
