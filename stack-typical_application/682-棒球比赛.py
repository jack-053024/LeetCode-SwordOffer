# 给定一个字符串列表，每个字符串可以是以下四种类型之一：
# 1.整数（一轮的得分）：直接表示您在本轮中获得的积分数。
# 2. "+"（一轮的得分）：表示本轮获得的得分是前两轮有效 回合得分的总和。
# 3. "D"（一轮的得分）：表示本轮获得的得分是前一轮有效 回合得分的两倍。
# 4. "C"（一个操作，这不是一个回合的分数）：表示您获得的最后一个有效 回合的分数是无效的，应该被移除。
# 每一轮的操作都是永久性的，可能会对前一轮和后一轮产生影响。
# 你需要返回你在所有回合中得分的总和。
# Difficulty: easy
class Solution:
    '''stack'''
    def calPoints(self, ops) -> int:
        scores_stack = []
        for elem in ops:
            if elem == 'C':
                scores_stack.pop()
            elif elem == '+':
                scores_stack.append(scores_stack[-1] + scores_stack[-2])
            elif elem == 'D':
                scores_stack.append(scores_stack[-1] * 2)
            else:  # 其他的就都是实际的分数了；需要注意的是，"-2".isdigit() 会返回 False
                scores_stack.append(int(elem))
        return sum(scores_stack)
    # analyse: time complexity: O(n); space complexity: O(n)

if __name__ == "__main__":
    solu = Solution()
    alist = ["5","-2","4","C","D","9","+","+"]
    print(solu.calPoints(alist))

