def merge_sort(array):
    # Сохраняем длину массива в переменную, чтобы не считать её каждый раз.
    len_array = len(array)
    # Базовый случай рекурсии.
    if len_array <= 1:
        return array

    # Рекурсивный разбор массива в левой половине:
    # передаём в merge_sort() левую половину полученного на вход массива.
    left = merge_sort(array[0: len_array // 2])

    # Рекурсивный разбор массива в правой половине:
    # передаём в merge_sort() правую половину полученного на вход массива.
    right = merge_sort(array[len_array // 2: len_array])

    return merge(left, right)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)

    while left_idx < len_left and right_idx < len_right:
        # Сравниваем:
        if left[left_idx] <= right[right_idx]:
            # Добавляем в result:
            result.append(left[left_idx])
            # Сдвигаем указатель:
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    return result + left[left_idx:] + right[right_idx:]


test_array = [5, 4, 9, 10, 8, 3, 11, 1, 7, 6, 2]
print(merge_sort(test_array))