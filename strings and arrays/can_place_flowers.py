# 605. Can Place Flowers
# You have a long flowerbed in which some of the plots are planted,
# and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed
#  without violating the no-adjacent-flowers rule and false otherwise.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        vacant_plots = 0

        # address only one element
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                vacant_plots += 1
            return vacant_plots>=n

        # address left corner
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            vacant_plots+=1

        i = 1
        while i < len(flowerbed)-2:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                print(i)
                vacant_plots += 1
                flowerbed[i] = 1
                i+=1 # can jump one since we set i=1
            i+=1

        # address right corner
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            vacant_plots += 1

        
        return vacant_plots>=n

        