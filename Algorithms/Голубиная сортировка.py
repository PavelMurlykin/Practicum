from collections import defaultdict


def counting_sort(array, rating_max):
    # Шаг 1. Создаем словарь со значением по умолчанию: пустой список.
    rating_players = defaultdict(list)

    # Шаг 2. Раскладываем игроков в словарь, где ключами служат рейтинги,
    # а в качестве значений - списки игроков с таким рейтингом.
    for player, rating in array:
        rating_players[rating].append((player, rating))

    # Собираем отсортированный массив, перебирая рейтинги в порядке убывания.
    sorted_array = []
    for rating in range(rating_max, 0, -1):
        # Если в словаре рассматриваемый рейтинг непустой, то все шахматисты
        # с этим рейтингом добавляются в итоговый результат.
        if rating_players[rating]:
            sorted_array.extend(rating_players[rating])

    return sorted_array


chess_players = [
    ('Гукеш Доммараджу', 2758),
    ('Фабиано Каруана', 2786),
    ('Уэсли Со', 2753),
    ('Магнус Карлсен', 2839),
    ('Дин Лижэнь', 2780),
    ('Ян Непомнящий', 2771),
    ('Аниш Гири', 2760),
    ('Вишванатан Ананд', 2754),
    ('Алиреза Фирузджа', 2777),
    ('Хикару Накамура', 2780),
]
result = counting_sort(chess_players, 3000)
print(result)