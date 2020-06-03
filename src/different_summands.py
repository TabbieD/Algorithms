# Uses python3
import random
# import sys
import time


def optimal_summands(n):
    k = []
    # write your code here
    i = 1
    while n > 0:
        if n - i > i:
            n -= i
            k.append(i)
            i += 1
        else:
            k.append(n)
            break

    return k


def stress_test():
    while True:
        number = random.randint(1, 1000000000)
        start = time.time()

        result, end = optimal_summands(number), time.time() - start

        if end <= 5:
            print(number, "->", len(result), result)
        else:
            print(number, "Bad")
            break


if __name__ == '__main__':
    # user_input = sys.stdin.read()
    # n = int(user_input)
    # summands = optimal_summands(n)
    # print(len(summands))
    # for x in summands:
    #    print(x, end=' ')
    stress_test()
