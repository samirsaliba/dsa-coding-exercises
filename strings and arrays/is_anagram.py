# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise. An Anagram is a word or phrase formed by
# rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = dict()

        for c in s:
            chars[c] = chars.get(c, 0) + 1
        
        for c in t:
            char_count = chars.get(c, 0)
            if char_count > 0:
                chars[c] = char_count - 1
                if char_count == 1:
                    del chars[c]
            else:
                return False
        
        if len(chars) > 0:
            return False
        return True