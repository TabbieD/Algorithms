# Uses python3


def fibonacci_partial_sum_naive(from_, to):
    total = 0

    current = 0
    next_ = 1

    for i in range(to + 1):
        if i >= from_:
            total += current

        current, next_ = next_, current + next_

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


def fibonacci_partial_sum_fast(m, n):
    # Partial sum of Fib series from m to n = F(n+2) - F(m+1)
    if n == m:
        return get_fibonacci_huge_fast(n, 10)
    last_digit_fib_n_plus2 = get_fibonacci_huge_fast(n+2, 10)
    last_digit_fib_m_minus1 = get_fibonacci_huge_fast(m+1, 10)

    if last_digit_fib_n_plus2 < last_digit_fib_m_minus1:
        return (last_digit_fib_n_plus2 + 10) - last_digit_fib_m_minus1

    else:
        return last_digit_fib_n_plus2 - last_digit_fib_m_minus1


if __name__ == '__main__':
    inp = input()
    frm, t = map(int, inp.split())
    print(fibonacci_partial_sum_fast(frm, t))