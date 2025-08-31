import sys


def count_candidates(candidates, cycles):

    result = 0
    for index in range(2, candidates + 1):
        result = (result + cycles) % index

    return result + 1


def main():
    candidates = int(sys.stdin.readline().rstrip())
    cycles = int(sys.stdin.readline().rstrip())

    print(count_candidates(candidates, cycles))


if __name__ == '__main__':
    main()
