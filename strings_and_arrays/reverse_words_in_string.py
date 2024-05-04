# 151. Reverse Words in a String
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or 
# multiple spaces between two words.
# The returned string should only have a single space separating the words. 
# Do not include any extra spaces.

class Solution:        
    def reverseWords(self, s: str) -> str:
        start = None
        words = []

        for i, char in enumerate(s):
            if char == ' ':
                # probable endword
                if start is not None:
                    words.append(s[start:i])
                    start = None
            else:
                if start is None:
                    start = i
        
        if start is not None:
            words.append(s[start:i+1])

        return " ".join(reversed(words))
                    

