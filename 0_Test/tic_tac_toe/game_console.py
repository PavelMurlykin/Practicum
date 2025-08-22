from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(text):
    with open('0_Test/tic_tac_toe/results.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Пожалуйста, введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        # После каждого хода надо делать проверку на победу и на ничью.
        if game.check_win(current_player):
            game_result = f'Победили {current_player}.'
            print(game_result)
            running = False
            save_result(game_result)
        elif game.is_board_full():
            game_result = f'Победили {current_player}.'
            print(game_result)
            running = False
            save_result(game_result)

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
