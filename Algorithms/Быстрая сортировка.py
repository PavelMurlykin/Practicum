def quicksort(array):
    """Быстрая сортировка."""
    len_array = len(array)

    # Базовый случай рекурсии.
    if len_array <= 1:
        return array
    # Определяем индекс опорного элемента.
    middle_element_index = len_array // 2
    # Получаем опорный элемент:
    pivot = array[middle_element_index]
    # Передаём в функцию partition() массив и опорный элемент.
    left, center, right = partition(array, pivot)
    
    # L - список left, C - center, R - right.
    # print(f'L{left} + C{center} + R{right}')

    # Рекурсивно вызываем quicksort() для левого и правого списков,
    # а затем соединяем все три списка в один.
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    """
    Разбивает массив на три разных массива относительно опорного элемента.
    """
    # Создаём три пустых списка.
    left, center, right = [], [], []
    # Раскладываем элементы по спискам.
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    # Возвращаем кортеж с тремя списками.
    return left, center, right


arr = [44, 60, 10, 61, 60, 2, 62, 18, 2, 69]
result = quicksort(arr)
print(result)