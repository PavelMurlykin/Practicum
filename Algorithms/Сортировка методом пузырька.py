example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    last_index = len(data) - 1
    swapped = True
    while swapped:
        for item_index in range(last_index):
            swapped = False
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True

        last_index -= 1

    return data


print(bubble_sort(example_array))
