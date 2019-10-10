# coding: utf-8
# question:
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''买卖股票的最佳时机II----动态规划(一维DP)--easy'''
        # 1.状态：第几天的时候，已交易了多少次，是否持有
        # 注意：由于可以交易无限次，所以交易的次数并不影响，可以不用考虑
        # 2.状态转移：
        # 未持有=前一天未持有且不买 or 前一天持有但卖出
        # 持有=前一天持有但不卖 or 前一天未持有但买入
        # 3.base case：
        # 第一天未持有且不买，利润为 0
        # 第一天未持有但买入，利润为 -prices[0]
        if prices == []:
            return 0
        prices_len = len(prices)
        dp_0 = 0
        dp_1 = -prices[0]
        for i in range(1, prices_len):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, dp_0 - prices[i])  # 前一天的状态的总利润 - 当天买入的股票价格
        return dp_0

    # 经上分析，时间复杂度：O(n)，空间复杂度：O(1)
    # 该题也可以用贪心算法做，时间和空间差不多，但是贪心的思路更清晰一些

