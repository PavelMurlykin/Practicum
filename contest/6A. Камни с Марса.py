import sys


def calculate_completed_orders(orders_num, orders_weight, samples_num, samples_weight):
    sorted_orders_weight = sorted(orders_weight)
    sorted_samples_weight = sorted(samples_weight)

    completed_orders = 0
    order_index = 0
    sample_index = 0

    while order_index < orders_num and sample_index < samples_num:
        if sorted_samples_weight[sample_index] >= sorted_orders_weight[order_index]:
            completed_orders += 1
            order_index += 1
            sample_index += 1
        else:
            sample_index += 1

    return completed_orders


def main():
    orders_num = int(sys.stdin.readline().rstrip())
    orders_weight = list(map(int, sys.stdin.readline().rstrip().split()))
    samples_num = int(sys.stdin.readline().rstrip())
    samples_weight = list(map(int, sys.stdin.readline().rstrip().split()))

    print(calculate_completed_orders(orders_num, orders_weight, samples_num, samples_weight))


if __name__ == '__main__':
    main()
