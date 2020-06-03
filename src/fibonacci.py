# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib_fast(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        new_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(new_fib)
    return fib_list[-1]


def calc_fib_fast2(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    # import timeit

    number = int(input())
    # print(timeit.timeit("calc_fib_fast(number)", globals=globals()), calc_fib_fast(number))
    print(calc_fib_fast2(number))
