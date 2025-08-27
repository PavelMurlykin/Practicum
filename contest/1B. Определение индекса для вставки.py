import sys


def index_seek(numbers, element):

    for index, number in enumerate(numbers):
        if number >= element:
            return index

    return index + 1


def main():
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    element = int(sys.stdin.readline().rstrip())

    print(index_seek(numbers, element))


if __name__ == '__main__':
    main()
