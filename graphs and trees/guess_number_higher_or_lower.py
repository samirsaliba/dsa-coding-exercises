# 374. Guess Number Higher or Lower
# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked
#  is higher or lower than your guess.
# You call a pre-defined API int guess(int num), 
# which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 0, n

        while True:
            half = start + (end-start)//2
            res = guess(half)

            if (end-start) < 2:
                if guess(start) == 0: return start
                else: return end

            if res==0:
                return half
            elif res == 1:
                # guess is lower
                start = half+1
            elif res == -1:
                # guess is higher
                end = half 