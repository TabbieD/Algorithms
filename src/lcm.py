# Uses python3
import sys


def lcm_naive(a, b):
    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            return i

    return a * b


def gcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd(b, a_prime)


def fast_lcm(a, b):
    result = int((a*b) / gcd(a, b))
    return result


if __name__ == '__main__':
    import time

    x = time.time()
    user = input()
    c, d = map(int, user.split())
    print(fast_lcm(c, d), time.time() - x)
