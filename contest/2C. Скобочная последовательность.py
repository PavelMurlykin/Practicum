import sys


def is_correct_bracket_seq(sequence: str) -> bool:
    if len(sequence) == 0:
        return True

    stack = []
    brackets_mapping = {')': '(', '}': '{', ']': '['}

    for bracket in sequence:
        if bracket in brackets_mapping.values():
            stack.append(bracket)
        elif bracket in brackets_mapping:
            if not stack or stack[-1] != brackets_mapping[bracket]:
                return False
            stack.pop()

    return len(stack) == 0


def main():
    sequence = sys.stdin.readline().rstrip()

    print(is_correct_bracket_seq(sequence))


if __name__ == '__main__':
    main()
