#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 15:18
# @Author  : Jack
class Heap(object):
    """heap"""
    def __init__(self, capacity):
        self.capacity = capacity    # the capacity of heap
        self._heap = []             # the array holding the heap
        self.index_last_elem = 0    # the index of the last elem

    def insert(self, item):
        """
        insert an elem at the end of the heap
        :param item: the elem to be inserted
        :return: none
        """
        # 1. judge whether the heap is full
        if self.capacity == self.index_last_elem: return
        # 2. insert the item
        self.index_last_elem += 1
        self._heap[self.index_last_elem] = item
        # 3. heapify
        i = self.index_last_elem
        # 3.1 parent node is at most the root and parent node greater than item
        while i // 2 > 0 and self._heap[i//2] > item:
            self._heap[i//2], self[i] = self._heap[i], self._heap[i//2]
            i = i // 2

    def remove_max(self):
        """
        remove the top elem from the heap
        :return: none
        """
        # 1. judge whether the heap is empty
        if self.index_last_elem == 0: return
        # 2. cover the top elem
        self._heap[1] = self._heap[self.index_last_elem]
        self.index_last_elem -= 1
        # 3. heapify from top to bottom
        self._heapify(1)

    def _heapify(self, i=1):
        """
        heapify from top to bottom from a node
        :param i: the index of the node
        :return: none
        """
        while True:
            max_pos = i  # make a label for the max node
            if i * 2 <= self.index_last_elem and self._heap[i*2] > self._heap[max_pos]:
                max_pos = i * 2
            if i * 2 + 1 <= self.index_last_elem and self._heap[i*2+1] > self._heap[max_pos]:
                max_pos = i * 2 + 1
            if max_pos == i: break  # if the current node is max, jump out from cycle
            self._heap[i], self._heap[max_pos] = self._heap[max_pos], self._heap[i]
            i = max_pos





