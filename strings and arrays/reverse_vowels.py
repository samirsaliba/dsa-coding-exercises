# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', 
# and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        seen_vowels = []
        s = list(s)
        for c in s:
            if c in vowels:
                seen_vowels.append(c)
        
        # could use a stack and just pop from it but a list will do
        i = len(seen_vowels)-1
        out = ''
        for j, c in enumerate(s):
            if c in vowels:
                out += seen_vowels[i]
                i -= 1
            else:
                out += c

        return out
