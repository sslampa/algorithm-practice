import math


def merge(a, b):
    combine_list = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            combine_list.append(b[0])
            b.pop(0)
        else:
            combine_list.append(a[0])
            a.pop(0)

    while len(a) > 0:
        combine_list.append(a[0])
        a.pop(0)

    while len(b) > 0:
        combine_list.append(b[0])
        b.pop(0)

    return combine_list


def merge_sort(a):
    length = len(a)
    if length == 1:
        return a
    l1 = a[0:math.floor(length/2)]
    l2 = a[math.floor(length/2):]
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)

    return merge(l1, l2)


some_list = [5, 3, 1, 2, 7, 6, 4]

print(merge_sort(some_list))
