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
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.isAlfaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlfaNumeric(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    def isAlfaNumeric(self, key):
        return (ord('A') <= ord(key) <= ord('Z') or
                ord('a') <= ord(key) <= ord('z') or
                ord('0') <= ord(key) <= ord('9')
                )
                    


palindrome = "abba"
# palindrome = "0P"
solution = Solution()
print(solution.isPalindrome(palindrome))