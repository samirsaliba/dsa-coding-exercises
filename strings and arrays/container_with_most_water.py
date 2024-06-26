# 11. Container With Most Water
# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        max_vol = (0, (left, right))
        
        while left < right:
            hl, hr = height[left], height[right]
            volume =  min(hl, hr) * (right - left)
            
            if volume > max_vol[0]:
                max_vol = (volume, (left, right))
            
            elif hl > hr:
                right -= 1
            
            else:
                left += 1
        
        return max_vol[0]
            
                
        