def list_superset(list_set_1, list_set_2):
    list_set_1_len = len(list_set_1)
    list_set_2_len = len(list_set_2)

    if list_set_1_len <= list_set_2_len:
        for item in list_set_1:
            if item not in list_set_2:
                return 'Супермножество не обнаружено.'
        if list_set_1_len == list_set_2_len:
            return 'Наборы равны.'
        else:
            return f'Набор {list_set_2} - супермножество.'
    else:
        for item in list_set_2:
            if item not in list_set_1:
                return 'Супермножество не обнаружено.'
        return f'Набор {list_set_1} - супермножество.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
