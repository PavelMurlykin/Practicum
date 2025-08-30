# ID посылки: 141665082
import sys

BASE = 10
"""Основание системы счисления для преобразования цифр в число."""


def decode_instruction(instruction: str) -> str:
    def decode(index: int) -> tuple[str, int]:
        result = ''
        number = 0
        while index < len(instruction):
            if instruction[index].isdigit():
                number = number * BASE + int(instruction[index])
            elif instruction[index] == '[':
                sub_string, new_index = decode(index + 1)
                result += sub_string * number
                number = 0
                index = new_index
            elif instruction[index] == ']':
                return result, index
            else:
                result += instruction[index]
            index += 1
        return result, index

    decoded_instruction, _ = decode(0)
    return decoded_instruction


def main():
    instruction = sys.stdin.readline().rstrip()

    print(decode_instruction(instruction))


if __name__ == '__main__':
    main()
