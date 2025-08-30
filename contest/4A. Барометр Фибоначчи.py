import sys


def get_fibonacci_result(generation):

    if generation in [0, 1]:
        return 1
    else:
        return get_fibonacci_result(generation - 1) + get_fibonacci_result(generation - 2)


def main():
    generation = int(sys.stdin.readline().rstrip())

    print(get_fibonacci_result(generation))


if __name__ == '__main__':
    main()
