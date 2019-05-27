from typing import List
from random import randrange
def merge_sort(list_: List) -> List:
    """ Sorts given list in O(nlogn) time, returns sorted list """
    # base case 
    if len(list_) <= 1:
        return list_
    else:
        a = merge_sort(list_[0:len(list_)//2])
        b = merge_sort(list_[len(list_)//2:])
        return merge(a,b)
        

def merge(a: List, b: List) -> List:
    """ Precondition that a and b are sorted """
    loc_a = 0
    loc_b = 0
    result = []
    while loc_a < len(a) or loc_b < len(b):
        if loc_a == len(a):
            result.append(b[loc_b])
            loc_b += 1
        elif loc_b == len(b):
            result.append(a[loc_a])
            loc_a += 1
        else:
            # both lists have elements remaining, find smallest
            if a[loc_a] < b[loc_b]:
                result.append(a[loc_a])
                loc_a += 1
            else:
                result.append(b[loc_b])
                loc_b += 1
    return result

def pivot_sort(list_: List) -> List:
    # base case
    if len(list_) <=1:
        return list_
    # recursive
    smaller = []
    larger = []
    equals = []
    loc_pivot = randrange(0,len(list_))
    pivot = list_[loc_pivot]
    for i in range(len(list_)):
        if i == loc_pivot:
            continue
        if list_[i] < pivot:
            smaller.append(list_[i])
        elif list_[i] == pivot:
            equals.append(list_[i])
        else:
            # larger
            larger.append(list_[i])
    smaller.append(pivot)
    smaller = pivot_sort(smaller)
    smaller.extend(equals)
    larger = pivot_sort(larger)
    result = merge(smaller,larger)
    return result
