# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

from collections import defaultdict, Counter
# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# My first solutiojn works but extremly slow. doesnt pass the efficiency tests.
class Solution(object):
    def anagram_checker(self, word1, word2):
        chars = defaultdict(int)
        for l in word1:
            chars[l] += 1
    
        for l in word2:
            chars[l] -= 1
        
        return all(v == 0 for v in chars.values())
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lst = []
        for idx_1, word_1 in enumerate(strs):
            lst_of_anagrams = [word_1]
            for idx_2, word_2 in enumerate(strs):
                if idx_1 != idx_2:
                     check_if_anagram = self.anagram_checker(word_1, word_2)
                     if check_if_anagram:
                          lst_of_anagrams.append(word_2)
                     continue
            lst_of_anagrams.sort()
            if lst_of_anagrams not in lst:
                lst.append(lst_of_anagrams)
        return lst
# clever solution from leetcode
class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)
        return list(letters_to_words.values())

# very fast and efficient in memory and speed solution
class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in h:
                h[sortedWord] = [word]
            else:
                h[sortedWord].append(word)
        final = []
        for value in h.values():
            final.append(value)
        return final

strs = ["eat","tea","tan","ate","nat","bat"]

solution = Solution()
print(solution.groupAnagrams(strs))


