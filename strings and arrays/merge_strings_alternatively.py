# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
# Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = ''
        while i < len(word1) and i < len(word2):
            out += word1[i] + word2[i]
            i+=1

        if i < len(word1):
            # add remaining of word1
            out += word1[i:]

        else:
            # add remaining of word2
            out += word2[i:]
        
        return out