# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Testcases
# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # set_of_nums = set(nums)
        # if len(nums) != len(set_of_nums):
        #     return True
        # else:
        #     return False

        return len(nums) != len(set(nums))

        # hset = set()
        # for idx in nums:
        #     if idx in hset:
        #         return True
        #     else:
        #         hset.add(idx)

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums)) 


        