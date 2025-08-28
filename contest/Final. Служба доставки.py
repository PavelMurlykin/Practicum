# ID посылки: 141630116
import sys


def min_platforms(weights: list[int], limit: int) -> int:
    weights.sort()
    min_element, max_element = 0, len(weights) - 1
    platforms = 0

    while min_element <= max_element:
        if weights[min_element] + weights[max_element] <= limit:
            min_element += 1
        max_element -= 1
        platforms += 1

    return platforms


def main():
    weights = list(map(int, sys.stdin.readline().rstrip().split()))
    limit = int(sys.stdin.readline().rstrip())

    print(min_platforms(weights, limit))


if __name__ == '__main__':
    main()
