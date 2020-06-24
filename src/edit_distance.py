# Uses python3
def edit_distance(s, t):
    # write your code here
    n, m = len(s) + 1, len(t) + 1
    memory = [[0 for x in range(m)] for x in range(n)]

    for i in range(0, n):
        for j in range(0, m):
            if i == 0:
                memory[i][j] = j
            elif j == 0:
                memory[i][j] = i

            elif s[i - 1] == t[j - 1]:
                memory[i][j] = memory[i - 1][j - 1]
            else:
                insert = memory[i][j - 1] + 1
                delete = memory[i - 1][j] + 1
                mismatch = memory[i - 1][j - 1] + 1
                memory[i][j] = min(insert, delete, mismatch)

    return memory[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
