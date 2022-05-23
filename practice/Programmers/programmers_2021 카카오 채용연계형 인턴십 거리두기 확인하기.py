from itertools import combinations

places = [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
         ]


def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def coordinate(place):
    coordinates = []
    partitions = []
    for i, row in enumerate(place):
        for j, col in enumerate(row):
            if col == 'P':
                coordinates.append((i, j))
            elif col == 'X':
                partitions.append((i, j))
    return coordinates, partitions


def distance_check(cases, partitions):
    for case in cases:
        x1, y1, x2, y2 = case[0][0], case[0][1], case[1][0], case[1][1]
        if abs(x1 - x2) <= 2 and abs(y1 - y2) <= 2:
            distance = manhattan(x1, y1, x2, y2)
            if distance == 2:
                if x1 == x2:
                    min_y = min(y1, y2)
                    if (x1, min_y + 1) not in partitions:
                        return 0

                elif y1 == y2:
                    min_x = min(x1, x2)
                    if (min_x + 1, y1) not in partitions:
                        return 0

                else:
                    if (x1, y2) not in partitions and (x2, y1) not in partitions:
                        return 0

            elif distance == 1:
                return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        coordinates, partitions = coordinate(place)
        if len(coordinates) < 2:
            answer.append(1)
        else:
            cases = combinations(coordinates, 2)

            result = distance_check(cases, partitions)
            answer.append(result)

    return answer


print(solution(places))