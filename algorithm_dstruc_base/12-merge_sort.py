# coding:utf-8

def merge_sort(alist):
    '''并归排序-稳定排序-时间复杂度为线性对数阶'''
    if len(alist) <= 1:
        return alist
    alist_len = len(alist)
    mid = alist_len // 2

    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_list) and right_pointer < len(right_list):
        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    return result


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    ret = merge_sort(alist)
    print(alist)
    print(ret)