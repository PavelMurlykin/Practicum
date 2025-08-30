import sys


def get_smaller_numbers(numbers):

    number_of_numbers = [None] * len(numbers)

    for index, number in enumerate(numbers):
        count = 0
        for cmp_index, cmp_number in enumerate(numbers):
            if numbers[index] != numbers[cmp_index] and cmp_number < number:
                count += 1
        number_of_numbers[index] = count

    return number_of_numbers


def main():
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    print(*get_smaller_numbers(numbers))


if __name__ == '__main__':
    main()
