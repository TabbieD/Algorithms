# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    total = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total += current * current

    return total % 10


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(n, m):
    period = pisano_period(m)

    n = n % period
    previous, current = 0, 1
    for i in range(n-1):
        previous, current = current, previous + current
    return current % m


def fibonacci_sum_squares_fast(n):
    # Sum of squares pf Fib series = F(n) * F(n+1)

    last_digit_fib_n = get_fibonacci_huge_fast(n, 10)
    last_digit_fib_n_plus1 = get_fibonacci_huge_fast(n+1, 10)

    return (last_digit_fib_n * last_digit_fib_n_plus1) % 10


if __name__ == '__main__':
    a = int(input())
    print(fibonacci_sum_squares_fast(a))
