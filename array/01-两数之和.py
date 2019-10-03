# coding:utf-8

# question:
# 给定一个整数数组 nums 和一个目标值 target，
# 请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
def two_sum(nums, target):
    '''nums中两数之和等于target，返回这两个数的下标'''
    # 使用哈希表
    # 1.从nums中任取一个数a，则只需要判断target - a是否在nums中就可以了
    # for a in nums:
    #     if (target-a) in nums:
    #         if a != (target - a):
    #             return nums.index(a), nums.index(target-a)      O(n)
    # 2.为了最后能够过去下标，同时不影响时间复杂度，可以采用字典，将序列转化为映射，用enumerate
    a_dict = {}
    for i, num in enumerate(nums):
        a_dict[num] = i
    for j, num in enumerate(nums):
        if (target-num) in a_dict and j != a_dict[target-num]:
            return [j, a_dict[target-num]]
