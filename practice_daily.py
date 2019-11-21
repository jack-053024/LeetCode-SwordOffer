def merge_sort(alist):
    """merge sort"""
    alist_len = len(alist)
    if alist_len <= 1:
        return alist
    mid_index = alist_len // 2
    left_list = merge_sort(alist[:mid_index])
    right_list = merge_sort(alist[mid_index:])

    left_p, right_p = 0, 0
    res = []
    while left_p < len(left_list) and right_p < len(right_list):
        if left_list[left_p] <= right_list[right_p]:
            res.append(left_list[left_p])
            left_p += 1
        else:
            res.append(right_list[right_p])
            right_p += 1
    res += left_list[left_p:]
    res += right_list[right_p:]
    return res


if __name__ == '__main__':
    alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    alist = merge_sort(alist)
    print(alist)
