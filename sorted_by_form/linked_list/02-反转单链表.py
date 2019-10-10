# coding:utf-8

def reverse_single_list(head):
    '''反转一个单链表----双指针--easy'''
    # 1.定义两个指针：prev和cur，一前一后，从第一个节点开始，遍历每一个节点，
    # 2.在cur.next改变指向前，先把cur.next保存到next_temp中
    # 3.在cur指向next_temp前，先把prev指向cur
    prev = None
    cur = head
    while cur != None:
        next_temp = cur.next
        cur.next = prev
        prev = cur
        cur = next_temp

    return prev
