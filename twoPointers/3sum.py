# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
from typing import List
class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # our aim is to return a list of numbers that adds up to 0, so if the first element is already bigger than 0 and the list is sorted its impossible to return a sum of three numbers which will be equal to zero
            if a > 0:
                break
            # we dont want to cause compare  -indexes so we skip 0
            # and because the list is sorted we can have same values next to each other, there we use that fact to skip same values because we dont want duplicates in our solution
            if i > 0 and a == nums[i - 1]:
                continue
            
            # we will always operate on the piece of array after i, because we want our iterations number as small as possible.
            l, r = i + 1, len(nums) - 1
            # we want to iterate as long as l != r
            while l < r:
                threeSum = a + nums[l] + nums[r]
                # the list is already sorted so if the threesum is bigger than 0 we need to decrease r pointer to the left to have smaller total value
                if threeSum > 0:
                    r -= 1
                # opposite operation, we want our threesum to be bigger therefore we gonna increment l point by 1
                elif threeSum < 0:
                    l += 1
                # if we go into else this means that we have matched 0 and we will append the result
                else:
                    res.append([a, nums[l], nums[r]])
                    # i dont get it from that point, tell me why we increase l pointer, not decrease r pointer
                    l += 1
                    # so here we want to switch to another unique element
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
                

nums = [0,2,0,3,1,0,1,3,2,1]
solution = Solution()
print(solution.trap(nums))