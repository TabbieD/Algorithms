# python3
import numpy as np


def max_pairwise_product(numbers):
    n = len(numbers)
    first = 0
    for i in range(1, n):
        if numbers[i] > numbers[first]:
            first = i
    numbers[-1] = numbers[first]
    second = 0
    for i in range(1, n - 1):
        if numbers[i] > numbers[second]:
            second = i

    return numbers[-1] * numbers[second]


def max_pairwise_product_fast(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


def stress_test(x, y):
    while True:
        n = int(np.random.randint(2, x, 1))
        array = np.random.randint(0, y, n)

        result1 = max_pairwise_product(array)
        result2 = max_pairwise_product_fast(array)

        print(array)
        if result1 == result2:
            print('OK')
        else:
            print(result1, result2)
            break


if __name__ == '__main__':
    # import timeit

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # input_numbers = [i for i in range(1, 200001)]
    # print(timeit.timeit("max_pairwise_product_fast(input_numbers)", globals=globals()))
    # print(max_pairwise_product_fast(input_numbers))
    print(max_pairwise_product(input_numbers))
    # print(stress_test(11, 50))
