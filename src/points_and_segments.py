# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    # sweep line algorithm
    count = [0] * len(points)
    # create temp array with label
    array = [(i, 's') for i in starts] + [(i, 'e') for i in ends] + [(i, 'p') for i in points]
    # sort array
    array = sorted(array, key=lambda element: element[0])
    counter = 0
    # linear scan
    for i in array:
        if i[1] == 's':
            counter += 1
        elif i[1] == 'e':
            counter -= 1
        else:
            y = points.index(i[0])
            count[y] = counter
    return count


def count_segments(starts, ends, pt):
    # count = [0] * len(points)
    # write your code here
    # for i in range(len(count)):
    i = 0
    if len(starts) == 1:
        if starts[0] <= pt <= ends[0]:
            i += 1
        #    count[i] += 1

    elif len(starts) > 1:
        mid = len(starts) // 2
        i += count_segments(starts[:mid], ends[:mid], pt)
        i += count_segments(starts[mid:], ends[mid:], pt)

    return i


def fast_count(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(count)):
        count[i] += count_segments(starts, ends, points[i])

    return count


def naive_count_segments(starts, ends, points):
    count = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                count[i] += 1
    return count


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n = data[0]
    m = data[1]
    start = data[2:2 * n + 2:2]
    end = data[3:2 * n + 2:2]
    point = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(start, end, point)
    for x in cnt:
        print(x, end=' ')
