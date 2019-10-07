# coding: utf-8
# question:
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''买卖股票的最佳时机II----贪心算法'''
        # 1.贪心算法，每天都买入，并将前一天的卖出；
        # 2.一开始总利润profit是0，每天买入卖出的价差可能是正的，也可能是负的，使用temp记录
        # 3.如果价差temp是负数，则不累加到总利润profit中
        # 4.当遍历完每一天后，总利润profit就是最大的，将profit输出即可
        prices_len = len(prices)
        if prices_len == 0 or prices_len == 1:
            return 0
        profit = 0
        for i in range(1, prices_len):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                profit += temp
        return profit

    # 经上分析，时间复杂度：O(n)，空间复杂度：O(1)

