from collections import defaultdict, Counter
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word 
# or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? 
# How would you adapt your solution to such a case?

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # my first simple solution, its very slow in runtime but good in memory efficiency.
        # if len(s) == len(t):
        #     for letter in t:
        #         if letter not in s or s.count(letter) != t.count(letter):
        #             return False
        #     return True
        # return False
        
        # solution based on default dict, very good in terms of runtime and memory.
        # if len(s) == len(t):
        #     chars = defaultdict(int)
        #     for l in s:
        #         chars[l] += 1
            
        #     for l in t:
        #         chars[l] -= 1
            
        #     return all(v == 0 for v in chars.values())

        # return False

        # Another simple solution using standardlibrary, seen as the most pythonic and friendly for an interview
        # return Counter(s) == Counter(t)

        # solution with normal dictionary
        # if len(s) != len(t):
        #     return False
        
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = countS.get(s[i],0) + 1
        #     countT[t[i]] = countS.get(t[i],0) + 1
        
        # for c in countS:
        #     if countS[c] != countT.get(c,0):    
        #         return False
        
        # return True

        # solution based on buildin sorted function
        return sorted(s) == sorted(t)
    
        # Manual dictionary solution (uncomment to use, ensure only one isAnagram is active)
        # if len(s) != len(t):
        #     return False
        # anagramDict = {}
        # for letter in s:
        #     if letter in anagramDict:
        #         anagramDict[letter] += 1
        #     else:
        #         anagramDict[letter] = 0
        # for letter in t:
        #     if letter in anagramDict:
        #         anagramDict[letter] -= 1
        #     else:
        #         return False
        # return True

solution = Solution()
print(solution.isAnagram("aacc","ccac"))