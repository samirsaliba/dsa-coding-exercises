# 1071. Greatest Common Divisor of Strings
# For two strings s and t, we say "t divides s" 
# if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x 
# such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def _is_div(s, t):
            if len(s) == 0:
                return False

            n = len(s) // len(t)
            if t * n == s:
                return True
            return False

        divisor = ''
        i = 0
        while i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                return ''

            curr_t = str1[:i+1]
            if _is_div(str1, curr_t) and _is_div(str2, curr_t):
                divisor = curr_t
            i+=1

        return divisor