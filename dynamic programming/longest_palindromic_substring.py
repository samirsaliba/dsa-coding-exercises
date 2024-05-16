# 5. Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_palindrome = (0, 0)

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_palindrome = (i, i + 1)

        
        for diff in range(2, n):
            # we keep growing palindrome sizes from 2 to n (diff)

            for i in range(n-diff):
                # all possible starts for current diff
                j = i + diff

                # now i,j is a palindrome if they are equal
                # and the elements between them also form a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_palindrome = (i,j)
                    # since we grow palindromes this is the biggest one yet
                    

        # max palindrome holds the max bounds
        i,j = max_palindrome
        return s[i : j+1]
        