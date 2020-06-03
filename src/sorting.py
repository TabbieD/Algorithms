# Uses python3
import sys
import random


def partition3(a, l_, r):
    # write your code here
    x = a[l_]
    m1 = l_
    m2 = m1
    for i in range(l_ + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m1] = a[m1], a[i]

        elif a[i] == x:
            m2 += 1
            a[i], a[m1+1] = a[m1+1], a[i]
    a[l_], a[m1] = a[m1], a[l_]
    if m2 == r:
        m2 = m1 + 1
    return m1, m2


def partition2(a, l_, r):
    x = a[l_]
    j = l_
    for i in range(l_ + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l_], a[j] = a[j], a[l_]
    return j


def randomized_quick_sort(a, l_, r):
    if l_ >= r:
        return
    k = random.randint(l_, r)
    a[l_], a[k] = a[k], a[l_]
    # use partition3
    # m = partition2(a, l_, r)
    m1, m2 = partition3(a, l_, r)
    randomized_quick_sort(a, l_, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    user_input = sys.stdin.read()
    n, *arr = list(map(int, user_input.split()))
    randomized_quick_sort(arr, 0, n - 1)
    # result = partition3(arr, 0, n-1)
    for y in arr:
        print(y, end=' ')
