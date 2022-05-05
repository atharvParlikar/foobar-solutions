import os
import time


def check_sides(map, index):
    numbers = []
    if index[0] - 1 >= 0 and map[index[0] - 1][index[1]] != 1:
        numbers.append([index[0] - 1, index[1]])
    if index[0] + 1 < len(map) and map[index[0] + 1][index[1]] != 1:
        numbers.append([index[0] + 1, index[1]])
    if index[1] - 1 >= 0 and map[index[0]][index[1] - 1] != 1:
        numbers.append([index[0], index[1] - 1])
    if index[1] + 1 < len(map[index[0]]) and map[index[0]][index[1] + 1] != 1:
        numbers.append([index[0], index[1] + 1])

    return numbers


def solve(map):
    visited = []
    last_length = 0
    target = [len(map) - 1, len(map[0]) - 1]
    counter = 0
    to_visit = [[0, 0]]
    while target not in visited:
        os.system("clear")
        last_length = len(visited)
        for i in to_visit:
            for j in check_sides(map, i):
                if j not in visited:
                    visited.append(j)
        to_visit = visited[last_length:]
        counter += 1
        for i in visited:
            map[i[0]][i[1]] = '*'
        draw(map)
        time.sleep(0.3)


def draw(map):
    for i in map:
        str_ = ""
        for j in i:
            str_ += str(j) + " "
        print(str_)


def solution(map):
    ones = []
    lengths = [solve(map)]
    for i, list_ in enumerate(map):
        for j, number in enumerate(list_):
            if number == 1:
                ones.append([i, j])
    for i in ones:
        map_ = [[y for y in x] for x in map]
        map_[i[0]][i[1]] = 0
        lengths.append(solve(map_))
    return lengths


solve([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [
    0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
