# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include 
# letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_letters = string.ascii_letters + string.digits
        print(valid_letters)
        cleared_s = "".join([letter for letter in s if letter in valid_letters]).lower()
        reversed_s = cleared_s[::-1]
        return cleared_s == reversed_s

palindrome = "A man, a plan, a canal: Panama"
# palindrome = "0P"
solution = Solution()
print(solution.isPalindrome(palindrome))