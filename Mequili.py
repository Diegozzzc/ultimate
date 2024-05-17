def balanced_merge_sort(data):
    if len(data) <= 1:
        return data

    # Dividir la lista en dos mitades
    mid = len(data) // 2
    left_half = balanced_merge_sort(data[:mid])
    right_half = balanced_merge_sort(data[mid:])

    # Mezclar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Comparar los elementos de las dos listas y combinarlos en orden
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Añadir los elementos restantes, si los hay
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

def main():
    # Pedir al usuario que ingrese una lista de números
    user_input = input("Ingrese una lista de números separados por espacios: ")
    data = list(map(int, user_input.split()))

    print("Datos originales:", data)

    # Ordenar la lista usando el método de ordenamiento de mezclas equilibradas
    sorted_data = balanced_merge_sort(data)

    print("Datos ordenados:", sorted_data)

if __name__ == "__main__":
    main()
