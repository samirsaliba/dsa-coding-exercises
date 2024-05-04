# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel
# letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vows = 0
        window_vows = 0
        for i in range(k):
            if s[i] in vowels:
                window_vows += 1

        max_vows = window_vows
        for i in range(k, len(s)):
            leaving_w = s[i-k] # char that is "leaving" the window
            if leaving_w in vowels:
                window_vows -= 1
            if s[i] in vowels:
                window_vows += 1 
            if window_vows > max_vows:
                max_vows = window_vows
            
        return max_vows
