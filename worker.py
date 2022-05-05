def solution(x, y):
    return getNumber((2 * x - 1) + (y - x)) + (x - 1)


def getNumber(x):
    return ((x ** 2) - x + 2) / 2


print(solution(3, 2))
