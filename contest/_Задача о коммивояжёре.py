from itertools import permutations
from sys import maxsize


def travel_salesman_problem(places, distances):
    movements = len(places) - 1
    # Вводим переменную для хранения самого короткого маршрута.
    min_path = None
    min_path_length = maxsize
    for current_path in permutations(places):
        current_path_length = 0
        for movement_index in range(movements):
            current_place = current_path[movement_index]
            next_place = current_path[movement_index + 1]
            current_place_index = places.index(current_place)
            next_place_index = places.index(next_place)
            distance = distances[current_place_index][next_place_index]
            current_path_length += distance
        # Если полученное расстояние меньше самого короткого пути...
        if current_path_length < min_path_length:
            # ...назначаем полученное расстояние самым коротким.
            min_path_length = current_path_length
            # Запоминаем самый короткий маршрут.
            min_path = current_path
    # Вместо одного значения возвращаем кортеж с двумя значениями:
    # расстоянием и самым коротким маршрутом.
    return min_path_length, min_path


if __name__ == '__main__':
    places_example = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
    distances_example = (
        (0, 3570, 2230, 6430, 600),
        (3570, 0, 5280, 4530, 3315),
        (2230, 5280, 0, 6715, 2540),
        (6430, 4530, 6715, 0, 6400),
        (600, 3315, 2540, 6400, 0),
    )
    min_path_length_example, min_path_example = travel_salesman_problem(
        places_example, distances_example
    )
    print(min_path_length_example, min_path_example)
