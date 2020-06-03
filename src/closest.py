# Uses python3
import sys
import math


def euclidean_distance(P1, P2):
    return math.sqrt(math.pow(P1[0] - P2[0], 2) + math.pow(P1[1] - P2[1], 2))


def brute_distance(points):
    d = euclidean_distance(points[0], points[1])
    if len(points) == 2:
        return euclidean_distance(points[0], points[1])
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < d:
                d = dist

    return d


def smallest_distance(points_x, points_y):
    if len(points_x) <= 3:
        return brute_distance(points_x)

    mid = len(points_x) // 2
    midpoint = points_x[mid]
    Lx = points_x[:mid]
    Rx = points_y[mid:]
    Ly, Ry = [], []
    for point in points_y:
        if point[0] < midpoint[0]:
            Ly.append(point)
        else:
            Ry.append(point)
    d_left = smallest_distance(Lx, Ly)
    # print(points[:mid], d_left)
    d_right = smallest_distance(Rx, Ry)
    # print(points[mid:], d_right)
    min_distance = min(d_left, d_right)
    # print(d)
    x_bar = Lx[-1][0]
    strip = []
    for y in points_y:
        if x_bar - min_distance < y[0] < x_bar + min_distance:
            strip.append(y)

    for i in range(len(strip) - 1):
        for j in range(i + 1, min(i + 7, len(strip))):
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_distance:
                min_distance = dist

    return min_distance


def minimum_distance(x, y):
    # write your code here
    points_x = sorted(list(zip(x, y)), key=lambda element: element[0])
    points_y = sorted(list(zip(x, y)), key=lambda element: element[0])

    return smallest_distance(points_x, points_y)


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n = data[0]
    a = data[1::2]
    b = data[2::2]
    print("{0:.4f}".format(minimum_distance(a, b)))
