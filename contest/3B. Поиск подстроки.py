import sys


def longest_unique_substring(string: str) -> int:
    left = 0
    max_len = 0
    last_occurrence = {}

    for right, char in enumerate(string):
        if char in last_occurrence and last_occurrence[char] >= left:
            left = last_occurrence[char] + 1
        last_occurrence[char] = right
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len


def main():
    string = sys.stdin.readline().rstrip()

    print(longest_unique_substring(string))


if __name__ == '__main__':
    main()
