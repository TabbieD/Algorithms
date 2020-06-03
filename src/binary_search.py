# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here
    if right < left:
        return -1
    mid = left + (right - left) // 2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search(a[mid + 1:], x)
    else:
        return binary_search(a[:mid], x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n = data[0]
    m = data[n + 1]
    b = data[1: n + 1]
    for y in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(b, y), end=' ')
