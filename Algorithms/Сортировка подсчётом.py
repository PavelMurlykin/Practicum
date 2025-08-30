def counting_sort(array, maximum):
    # Создаём массив для подсчёта вхождений каждого значения.
    count = [0] * (maximum + 1)
    # Перебираем массив по элементам.
    for item in array:
        # Для каждого значения массива array увеличиваем счётчик
        # в соответствующей ячейке массива count.
        # Например, увидели в array значение 2 - добавляем единицу к значению count[2].
        count[item] += 1

    # Объявляем результирующий список:
    sorted_array = []
    # Перебираем все уникальные элементы в списке count.
    for item in range(maximum + 1):
        # Добавляем в sorted_array уникальный элемент столько раз,
        # сколько он встретился в исходном массиве.
        sorted_array += [item] * count[item]
    return sorted_array


arr = [8, 1, 4, 10, 4, 1, 4, 7, 6, 8, 6, 4, 5, 10, 1, 0, 5, 4, 9, 7]
result = counting_sort(arr, 10)
print(result)