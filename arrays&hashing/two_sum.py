# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # my first solution its very unefficient with runtime beats only 14% developers, very good in terms of memory 
        # use cause beats 93% developers.
        # for idx,num_1 in enumerate(nums):
        #     for idx_, num_2 in enumerate(nums):
        #         if num_1 + num_2 == target and idx != idx_:
        #             return [idx,idx_]
        
        # hashmap solution
        tmp = {}
        for i, num in enumerate(nums):
            if target - num in tmp:
                return [tmp[target - num], i]
            tmp[num] = i
        return [-1, -1]
nums = [0,4,3,0]
solution = Solution()
print(solution.twoSum(nums,target=7))