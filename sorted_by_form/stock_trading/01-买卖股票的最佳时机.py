# coding: utf-8
import numpy as np
# question:
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''买卖股票的最佳时机----动态规划'''
        # 1.状态：数组长度为 i 时，买卖股票的最大利润
        if prices == []:
            return 0
        prices_len = len(prices)
        dp = np.zeros(prices_len)
        dp[0] = 0
        dp[1] = max(prices[1]-prices[0], 0)


