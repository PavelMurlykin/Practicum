import sys


def sort_by_template(array, templates):
    order_map = {}
    for idx, num in enumerate(templates):
        order_map[num] = idx

    in_list = []
    out_list = []

    for num in array:
        if num in order_map:
            in_list.append(num)
        else:
            out_list.append(num)

    in_list.sort(key=lambda x: order_map[x])
    out_list.sort()

    result = in_list + out_list

    return result


def main():
    array_num = int(sys.stdin.readline().rstrip())
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    templates_num = int(sys.stdin.readline().rstrip())
    templates = list(map(int, sys.stdin.readline().rstrip().split()))

    print(*sort_by_template(array, templates))


if __name__ == '__main__':
    main()
