# coding:utf-8

def merge_two_single_list(sl_01, sl_02):
    '''合并两个有序的单链表'''
    # 使用递归，操作头结点
    # 1.如果两条链表存在一条为空，则直接return l1 or l2返回其中一条不为空的链表
    # 2.如果两条链表都不为空，则判断了l1链表的头结点中的val是否比l2的小
    # 如果比l2的大，则交换l1和l2的引用指向，把l1的头结点的val值确定为最小的
    # 3.使用递归，调用函数本身，将l1.next和l2传入，然后将返回值用l1.next接住，串起来
    if sl_01 and sl_02:
        if sl_01.val < sl_02:
            sl_01.next = merge_two_single_list(sl_01.next, sl_02)
    return sl_01 or sl_02
