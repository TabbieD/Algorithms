# Uses python3
import sys


def get_change(n):
    # write your code here
    coins = [1, 3, 4]
    min_num_coins = [0] * (n + 1)
    for x in range(1, n + 1):
        min_num_coins[x] = n
        for coin in coins:
            if x >= coin:
                num_coins = min_num_coins[x - coin] + 1
                if num_coins < min_num_coins[x]:
                    min_num_coins[x] = num_coins
    # print(min_num_coins)
    return min_num_coins[-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
