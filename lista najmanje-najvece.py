def sortiraj(lista):
    lista = lista[:]   
    for i in range(len(lista)):
        min_index = najmanji(lista, i, len(lista)-1)
        zamijeni(lista, i, min_index)
    return lista