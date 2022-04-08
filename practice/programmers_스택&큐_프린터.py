priorities = [
    [2,1,3,2],
    [1,1,9,1,1,1],
]
locations = [
    2,
    0
]

def solution(priority, location):
    loc_list = list(range(len(priority)))
    order = 0
    c_priority = priority.copy()
    while c_priority:
        highest = max(c_priority)
        present = loc_list.pop(0)
        prior = c_priority.pop(0)
        if priority[present] < highest:
            loc_list.append(present)
            c_priority.append(prior)
        else:
            order += 1
            if present == location:
                return order
    return order

print(solution(priorities[1], locations[1]))