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

        return len(nums) != len(set(nums))

        hset = set()
        for n in nums:
            if n in hset:
                return True
            else:
                hset.add(n)
        return False

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums)) 


        