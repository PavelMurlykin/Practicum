# Импортируйте нужную библиотеку.
from datetime import datetime

date_format = '%d.%m.%Y'


class Store:
    def __init__(self, address):
        self.address: str = address

    def __is_open(self, date) -> bool:
        # Метод __is_open() в родительском классе всегда возвращает False,
        # это "код-заглушка", метод, предназначенный для переопределения
        # в дочерних классах.
        # Не переопределяйте содержимое этого метода.
        return False

    def get_info(self, text_date) -> str:
        # С помощью шаблона даты преобразуйте строку date_str в объект даты:
        date_object = datetime.strptime(text_date, date_format)

        # Передайте в метод __is_open() объект даты date_object и определите,
        # работает ли магазин в указанную дату.
        # В зависимости от результата будет выбрано значение
        # для переменной info.
        if self.__is_open(date_object):
            info = 'работает'
        else:
            info = 'не работает'
        return f'Магазин по адресу {self.address} {text_date} {info}'


class MiniStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() not in (5, 6):
            return True
        else:
            return False


class WeekendStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        if date.weekday() in (5, 6):
            return True
        else:
            return False


class NonStopStore(Store):
    # Переопределите метод __is_open().
    # Обратите внимание на имя метода/name mangling
    def _Store__is_open(self, date: datetime) -> bool:
        return True


mini_store = MiniStore('Улица Немига, 57')
print(mini_store.get_info('29.03.2024'))
print(mini_store.get_info('30.03.2024'))

weekend_store = WeekendStore('Улица Толе би, 321')
print(weekend_store.get_info('29.03.2024'))
print(weekend_store.get_info('30.03.2024'))

non_stop_store = NonStopStore('Улица Арбат, 60')
print(non_stop_store.get_info('29.03.2024'))
print(non_stop_store.get_info('30.03.2024'))
