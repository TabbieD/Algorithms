# Uses python3
import sys


def optimal_sequence(n):
    min_num_operations = [0] * (n + 1)
    min_num_operations[1] = 1
    for i in range(1, n+1):
        min_num_operations[i] = min_num_operations[i - 1] + 1
        if i % 2 == 0:
            num_operations = 1 + min_num_operations[i // 2]
            if num_operations < min_num_operations[i]:
                min_num_operations[i] = num_operations
        if i % 3 == 0:
            min_num_operations[i] = min(1 + min_num_operations[i // 3], min_num_operations[i])

    sequence = []
    while n > 1:
        sequence.append(n)
        if min_num_operations[n - 1] == min_num_operations[n] - 1:
            n = n - 1
        elif n % 2 == 0 and min_num_operations[n // 2] == min_num_operations[n] - 1:
            n = n // 2
        elif n % 3 == 0 and min_num_operations[n // 3] == min_num_operations[n] - 1:
            n = n // 3
    sequence.append(1)
    return reversed(sequence)


if __name__ == '__main__':
    user_input = sys.stdin.read()
    x = int(user_input)
    seq = list(optimal_sequence(x))
    print(len(seq) - 1)
    for x in seq:
        print(x, end=' ')
