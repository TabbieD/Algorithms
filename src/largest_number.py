#Uses python3
import sys


def largest_number(a):
    # write your code here
    res = ""
    a.sort(key=lambda x: len(x), reverse=True)
    a.sort(key=lambda x: x[0], reverse=True)

    i = 0
    n = len(a)
    while i < n:
        if i < n-1:
            if (len(a[i]) != len(a[i+1])) or (len(a[i]) and len(a[i+1])) > 1 and a[i][0] == a[i+1][0]:
                temp1 = int(a[i] + a[i+1])
                temp2 = int(a[i+1] + a[i])
                res = res + str(max(temp1, temp2))
                i += 2

            else:
                res = res + a[i]
                i += 1
        else:
            res = res + a[i]
            i += 1

    return res


if __name__ == '__main__':
    import time

    user_input = sys.stdin.read()
    data = user_input.split()
    a = data[1:]
    start = time.time()
    print(largest_number(a), time.time() - start)
