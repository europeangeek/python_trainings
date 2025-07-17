# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closeToOpen = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        # This version is slightly better because works as well when inside are other unrelated strings
        for c in s:
            if c in closeToOpen.values():
                stack.append(c)
            elif c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
        return not stack 
    
s = "([)]{}"
sample_expression = "([a+b]{c+d})"
bad_expression = "([a+b]{c+d}))"
solution = Solution().isValid(s)
print(solution)
solution = Solution().isValid(sample_expression)
print(solution)
solution = Solution().isValid(bad_expression)
print(solution)

