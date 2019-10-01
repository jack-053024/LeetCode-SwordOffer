# coding:utf-8

def insert_sort(alist):
    '''插入排序'''
    # alist_len = len(alist)
    # for i in range(1, alist_len):
    #     for j in range(i, 0, -1):
    #         if alist[j] < alist[j-1]:
    #             alist[j], alist[j-1] = alist[j-1], alist[j]
    alist_len = len(alist)
    for j in range(1, alist_len):
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


if __name__ == '__main__':
    alist = [54,226,93,17,77,31,44,55,20]
    print(alist)
    insert_sort(alist)
    print(alist)