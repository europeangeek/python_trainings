# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
from collections import defaultdict
# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
# Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # new_nums = sorted(nums)
        # consecutive_elements= []
        # for el in range(len(new_nums)):
        #     if el == 0:
        #         consecutive_elements.append(new_nums[el])
        #         continue
        #     if new_nums[el -1] + 1 == new_nums[el]:
        #         consecutive_elements.append(new_nums[el])
        # return len(consecutive_elements)
        # sequences = defaultdict(set)
        # set_nums = sorted(set(nums))
        # if len(set_nums) == 0:
        #     return 0
        # num_of_sequence = 0
        # for el in range(len(set_nums)):
        #     if el == 0:
        #         sequences[num_of_sequence].add(set_nums[el])
        #         continue
        #     if set_nums[el -1] + 1 == set_nums[el]:
        #         sequences[num_of_sequence].add(set_nums[el])
        #     else:
        #         num_of_sequence += 1
        #         sequences[num_of_sequence].add(set_nums[el])
        # return max([len(sequences[el]) for el in range(len(sequences))])
        # numSet = set(nums)
        # longest_sequence = 0
        # for n in nums:
        #     # check if its start of a sequence
        #     if n - 1 not in numSet:
        #         length = 0
        #         while (n + length) in numSet:
        #             length += 1
        #         if length > longest_sequence:
        #             longest_sequence = length
        # return longest_sequence
        numSet = set(nums)
        longest_sequence = 0
        for n in numSet:
            # check if its start of a sequence
            if n - 1 not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence

solution = Solution()
# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100, 4, 200, 1, 3, 2]
nums = [9,1,4,7,3,-1,0,5,8,-1,6]

print(solution.longestConsecutive(nums))