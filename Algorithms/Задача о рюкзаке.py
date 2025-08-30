from pprint import pprint


def backpack_problem_solution(
        tools: list[tuple[str, int, int]], capacity: int
) -> str:
    # Сохраняем количество приборов в переменную.
    items_count = len(tools)
    # Создаём таблицу. В каждой ячейке должны храниться число и список:
    # количество экспериментов и список приборов. Для простоты подсчётов
    # добавим строку с отсутствием рассматриваемых приборов
    # и столбец с нулевой вместимостью контейнера.
    table = [
        [[0, []] for _ in range(capacity + 1)] for _ in range(items_count + 1)
    ]
    # Для каждого прибора:
    for row_number in range(1, items_count + 1):
        # Распаковываем кортеж с данными о приборе.
        name, mass, experiments = tools[row_number - 1]
        # Для контейнера вместимостью от 1 и до максимальной вместимости:
        for volume in range(1, capacity + 1):
            # Если вес прибора меньше или равен
            # вместимости рассматриваемого контейнера.
            if mass <= volume:
                # Считаем количество экспериментов для текущего прибора
                # плюс наилучшее решение для оставшейся вместимости
                # из предыдущей строки.
                total_experiments_with_current_tool = (
                    experiments + table[row_number - 1][volume - mass][0]
                )
                # Количество экспериментов
                # в текущей колонке на предыдущей строке:
                previous_result = table[row_number - 1][volume][0]
                # Если результат с текущим прибором лучше:
                if total_experiments_with_current_tool > previous_result:
                    # Записываем количество экспериментов.
                    table[row_number][volume][0] = (
                        total_experiments_with_current_tool
                    )
                    # Копируем список приборов из предыдущей строки
                    # из ячейки, равной оставшейся вместимости.
                    table[row_number][volume][1] = list.copy(
                        table[row_number - 1][volume - mass][1]
                    )
                    # Добавляем к списку приборов
                    # имя текущего прибора.
                    table[row_number][volume][1].append(name)
                else:
                    # Если результат с рассматриваемым прибором
                    # хуже или такой же -
                    # переносим результат с предыдущей строки.
                    table[row_number][volume] = table[row_number - 1][volume]
            else:
                # Если масса рассматриваемого прибора
                # больше вместимости ячейки -
                # переносим результат с предыдущей строки.
                table[row_number][volume] = table[row_number - 1][volume]
    # Распечатываем таблицу для проверки.
    pprint(table)
    # Возвращаем строку с названиями приборов
    # из нижней правой ячейки таблицы, через запятую.
    return ', '.join(table[-1][-1][-1])


if __name__ == '__main__':
    # [('название прибора', масса, количество экспериментов)]
    tools = [
        ('гигрометр', 1, 3),
        ('масс-спектрометр', 4, 6),
        ('нивелир', 3, 4),
        ('интерферометр', 1, 4)
    ]
    result = backpack_problem_solution(tools, 4)
    print(result)
