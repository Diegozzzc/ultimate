def merge_sort(lista):
    # Si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Encuentra el punto medio de la lista
    medio = len(lista) // 2

    # Divide la lista en dos mitades
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Llama recursivamente a merge_sort en cada mitad
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # Intercala las dos mitades ordenadas
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Compara los elementos de las dos listas y agrégalos en orden al resultado
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Si quedan elementos en la lista izquierda, agrégalos al resultado
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i += 1

    # Si quedan elementos en la lista derecha, agrégalos al resultado
    while j < len(derecha):
        resultado.append(derecha[j])
        j += 1

    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    lista = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista)
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)
