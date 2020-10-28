# Uses python3
# import sys
import time
from collections import namedtuple
# from operator import attrgetter
import random

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    point = []
    # result = []

    line = [[pt for pt in range(s.start, s.end + 1)] for s in segments]
    line = sorted(list(line), key=lambda x: x[0])

    i = 0

    while i < len(line):
        if i != len(line) - 1:
            if len(set(line[i]) & set(line[i + 1])) != 0:
                point.append(max(set(line[i]) & set(line[i + 1])))
                i += 2

            else:
                point.append(max(line[i]))
                i += 1
        else:
            if point[-1] in line[i]:
                break
            else:
                point.append(max(line[i]))
                i += 1

    return set(point)


def stress_test():
    while True:
        l = random.randint(1, 100)
        a = [random.randint(0, 100000) for i in range(l + 1)]
        b = [random.randint(a[i], 100000) for i in range(l + 1)]
        segments = list(map(lambda x: Segment(x[0], x[1]), zip(a, b)))
        start = time.time()

        result, end = optimal_points(segments), time.time() - start
        result
        if end <= 5:
            print(l, "OK")
        else:
            print(l, 'BAD')
            break


if __name__ == '__main__':
    # user = sys.stdin.read()
    # n, *data = map(int, user.split())
    # segment = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # points = optimal_points(segment)
    # print(len(points))
    # for p in points:
    #    print(p, end=' ')
    stress_test()
