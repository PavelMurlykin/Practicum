class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(
        self,
        # Текст по умолчанию.
        message='Введено значение за границами игрового поля!'
    ):
        super().__init__(message)


class CellOccupiedError(Exception):
    def __init__(
        self,
        message='Попытка изменить занятую ячейку'
    ):

        super().__init__(message)
