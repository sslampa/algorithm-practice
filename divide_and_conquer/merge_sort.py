import math


def merge(a, b):
    combine_list = []
    start = 0
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            combine_list.append(b[0])
            b.pop(0)
            start += len(a)
        else:
            combine_list.append(a[0])
            a.pop(0)

    while len(a) > 0:
        combine_list.append(a[0])
        a.pop(0)

    while len(b) > 0:
        combine_list.append(b[0])
        b.pop(0)

    return combine_list, start


def merge_sort(a):
    length = len(a)
    if length == 1:
        return a, 0
    l1 = a[0:math.floor(length/2)]
    l2 = a[math.floor(length/2):]
    l1, x = merge_sort(l1)
    l2, y = merge_sort(l2)
    result, z = merge(l1, l2)

    return result, (x + y + z)


def answer(f):
    values = open(f, 'r')
    test = []
    for line in values:
        tmp = line.split('\n')
        test.append(int(tmp[0]))
    values.close()

    sorted_list, inversions = merge_sort(test)
    print(inversions)


answer('IntegerArray.txt')
