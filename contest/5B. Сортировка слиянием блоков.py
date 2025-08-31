import sys


def sort_by_blocks(array_num, array):
    count = 0
    current_max = 0
    for i in range(array_num):
        current_max = max(current_max, array[i])
        if current_max == i:
            count += 1

    return count


def main():
    array_num = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))

    print(sort_by_blocks(array_num, array))


if __name__ == '__main__':
    main()
