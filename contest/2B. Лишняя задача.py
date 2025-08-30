# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    if node is None:
        return None

    current_node = node
    if idx == 0:
        node = node.next_item
    else:
        idx_counter = 0
        while idx_counter < idx:
            idx_counter += 1
            previous_node = current_node
            current_node = current_node.next_item
            if node is None:
                return None
        previous_node.next_item = current_node.next_item

    del current_node
    return node


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
