import sys


def valid_mountain_array(mountain_peaks):

    number_of_peaks = len(mountain_peaks)
    if number_of_peaks < 3:
        return False

    index = 0

    while (index < number_of_peaks - 1 and
           mountain_peaks[index] < mountain_peaks[index + 1]):
        index += 1

    if index == 0 or index == number_of_peaks - 1:
        return False

    while (index < number_of_peaks - 1 and
           mountain_peaks[index] > mountain_peaks[index + 1]):
        index += 1

    return index == number_of_peaks - 1


def main():
    mountain_peaks = list(map(int, sys.stdin.readline().rstrip().split()))

    print(valid_mountain_array(mountain_peaks))


if __name__ == '__main__':
    main()
