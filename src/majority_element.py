# Uses python3
import sys


def merge(_arr, l_, m, r):

    n1 = m - l_ + 1
    n2 = r - m

    # create temp arrays
    _l = [0] * n1
    _r = [0] * n2

    for i in range(n1):
        _l[i] = _arr[l_ + i]

    for j in range(n2):
        _r[j] = _arr[m + 1 + j]

    i, j, k = 0, 0, l_

    while i < n1 and j < n2:
        if _l[i] <= _r[j]:
            _arr[k] = _l[i]
            i += 1
        else:
            _arr[k] = _r[j]
            j += 1
        k += 1

    while i < n1:
        _arr[k] = _l[i]
        i += 1
        k += 1

    while j < n2:
        _arr[k] = _r[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    # right = len(arr) - 1
    if left < right:
        # write your code here
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def get_majority_element(arr, left, right):
    # right = len(arr)
    merge_sort(arr, left, right - 1)
    i = 1
    count, maxseen = 0, 0
    for element in arr[:right-1]:
        if element == arr[i]:
            count += 1
        if maxseen <= count:
            maxseen = count + 1
        if element != arr[i]:
            count = 0
        i += 1

    if maxseen > right // 2:
        return maxseen
    else:
        return -1


if __name__ == '__main__':
    user = sys.stdin.read()
    n, *a = list(map(int, user.split()))
    result = get_majority_element(a, 0, n)
    if result != -1:
        print(1)
    else:
        print(0)
