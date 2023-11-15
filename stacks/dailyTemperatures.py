# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #TODO: Solution with O(n2) time complexity:
        # daysToWait = []
        # for id, temp in enumerate(temperatures):
        #     dist = 1
        #     for idx, nextTemp in enumerate(temperatures[id + 1:]):
        #         if temp < nextTemp:
        #             daysToWait.append(dist)
        #             break
        #         else:
        #             dist += 1
        #     if len(daysToWait) == id:
        #         daysToWait.append(0)
        #     dist = 1
        # return daysToWait
        #TODO: solution with 0(n) time complexity
        res = [0] * len(temperatures)
        stack = [] # pair [temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
        

temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))
        
                    