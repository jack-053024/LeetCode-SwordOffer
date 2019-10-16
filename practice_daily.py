# coding:utf-8

def quick_sort(alist, start, end):
    '''quick sortion'''
    if start > end:
        return
    mid_val = alist[start]
    low = start
    high = end
    while low < high:
        while low < high and alist[high] >= mid_val:
            high -= 1
        alist[low] = alist[high]
        while low < high and alist[low] < mid_val:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_val
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    alist_len = len(alist)
    print(alist)
    quick_sort(alist, 0, alist_len-1)
    print(alist)
