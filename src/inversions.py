# Uses python3
import sys


def merge(_arr, b, l_, m, r):
    number_of_inversions = 0
    n1 = m - l_ + 1
    n2 = r - m
    # create temp array
    i, j, k = 0, 0, l_

    while i < n1 and j < n2:
        if _arr[l_ + i] <= _arr[m + 1 + j]:
            b[k] = _arr[l_ + i]
            i += 1
        else:
            b[k] = _arr[m + 1 + j]
            j += 1
            number_of_inversions += m - i
        k += 1

    while i < n1:
        b[k] = _arr[l_ + i]
        i += 1
        k += 1

    while j < n2:
        b[k] = _arr[m + 1 + j]
        j += 1
        k += 1
    return number_of_inversions


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if left < right:
        # write your code here
        mid = left + (right - left) // 2
        number_of_inversions += get_number_of_inversions(a, b, left, mid)
        number_of_inversions += get_number_of_inversions(a, b, mid + 1, right)

        # n1 = mid
        # n2 = right
        # create temp array
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if a[i] <= a[j]:
                b[k] = a[i]
                i += 1
            else:
                b[k] = a[j]
                j += 1
                number_of_inversions += mid - i + 1
            k += 1

        while i <= mid:
            b[k] = a[i]
            i += 1
            k += 1

        while j <= right:
            b[k] = a[j]
            j += 1
            k += 1
        for i in range(right + 1):
            a[i] = b[i]
    return number_of_inversions


if __name__ == '__main__':
    user_input = sys.stdin.read()
    n, *c = list(map(int, user_input.split()))
    d = n * [0]
    print(get_number_of_inversions(c, d, 0, len(c)-1))
