# ID посылки: 141642447
import sys


def find_minimum_number_of_platforms(weights: list[int], limit: int) -> int:
    sorted_weights = sorted(weights)
    min_element, max_element = 0, len(sorted_weights) - 1
    platforms = 0

    while min_element <= max_element:
        if sorted_weights[min_element] + sorted_weights[max_element] <= limit:
            min_element += 1
        max_element -= 1
        platforms += 1

    return platforms


def main():
    weights = list(map(int, sys.stdin.readline().rstrip().split()))
    limit = int(sys.stdin.readline().rstrip())

    print(find_minimum_number_of_platforms(weights, limit))


if __name__ == '__main__':
    main()
