import sys


def main():
    elements_count = int(sys.stdin.readline().rstrip())

    # numbers = [None] * elements_count
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    unique_number = []
    place_holders = []

    # for index in range(elements_count):
    #     numbers[index] = sys.stdin.readline().rstrip()

    for number in numbers:
        if number not in (unique_number):
            unique_number.append(number)
        else:
            place_holders.append('_')

    numbers = unique_number + place_holders

    print(*numbers)


if __name__ == '__main__':
    main()
