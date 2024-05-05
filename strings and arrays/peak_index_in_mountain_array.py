# 852. Peak Index in a Mountain Array
# An array arr is a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
# You must solve it in O(log(arr.length)) time complexity.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # we're guaranteed that the array is a mountain
        # that is, there is a global maximum
        # there's also no possible local maxima
        # since a[0] < a[1] ... a[i-1] < a[i] > a[i+1]  ... > a[n-1] > a[n]
        # we can binary search the array, which was hinted by the constraint
        
        j = len(arr)-1
        i = 0        
        
        while i <= j:
            mid = (j-i)//2 + i 
            
            left = arr[mid-1]
            right = arr[mid+1]

            if arr[mid] > left and arr[mid] > right:
                # peak found
                return mid 

            elif arr[mid] < right:
                # right is larger, we should search
                # the right half of the array
                i = mid + 1

            else:
                # left is larger, we should search
                # the left half of the array
                j = mid - 1