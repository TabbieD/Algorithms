# Uses python3
# import sys
import random
import numpy as np
import time


def max_dot_product(c, d):
    # write your code here
    c.sort()
    d.sort()

    res = sum([c[i] * d[i] for i in range(len(c))])

    return res


def stress_test():
    while True:
        start = time.time()
        x = random.randint(1, 1000)
        y = np.random.randint(-100000, 100000, x)
        z = np.random.randint(-100000, 100000, x)

        result, end = max_dot_product(y, z), time.time() - start

        if end <= 5:
            print(x, "OK")
        else:
            print(x, 'Bad')
            break


if __name__ == '__main__':
    # user_input = sys.stdin.read()
    # data = list(map(int, user_input.split()))
    # n = data[0]
    # a = data[1:(n + 1)]
    # b = data[(n + 1):]
    # print(max_dot_product(a, b))
    stress_test()
