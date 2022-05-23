from itertools import permutations

def solution(numbers):
    lst = list(map(str, numbers))
    n = len(lst)
    cases = permutations(lst, n)
    case_lst = []
    for case in cases:
        case_lst.append(int(''.join(case)))
    case_lst.sort()
    max_case = case_lst.pop()
    return str(max_case)


print(type(solution([3, 30, 34, 5, 9])))