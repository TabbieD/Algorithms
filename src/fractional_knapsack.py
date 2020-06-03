# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    value_per_unit = [x / y for x in values for y in weights]
    sack = list(zip(weights, values, value_per_unit))
    sorted_sack = sorted(sack, key=lambda knapsack: knapsack[2])

    i = n-1
    while capacity > 0 and i >= 0:
        w = sorted_sack[i][0]
        if w <= capacity:
            value += sorted_sack[i][1]
            capacity -= w
            # print(value)
        else:
            value += (capacity * sorted_sack[i][1]) / sorted_sack[i][0]
            capacity = 0
        i -= 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, cap = data[0:2]
    array_values = data[2:(2 * n + 2):2]
    array_weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(cap, array_weights, array_values)
    print("{:.4f}".format(opt_value))
