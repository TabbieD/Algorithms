# Uses python3


def get_change(m):
    # write your code here
    count = 0
    while m > 0:
        if m >= 10:
            count += m // 10
            m %= 10
        elif m >= 5:
            count += m // 5
            m %= 5
        else:
            count += m
            break

    return count


if __name__ == '__main__':
    x = int(input())
    print(get_change(x))
