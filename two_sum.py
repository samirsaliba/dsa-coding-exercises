# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution:
    def _merge(self, a, b):
        i, j = 0, 0
        res = []

        while( i<len(a) and j<len(b) ):
            if a[i] <= b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        
        while i<len(a):
            res.append(a[i])
            i+=1

        while j<len(b):
            res.append(b[j])
            j+=1

        return res

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        if len(arr) == 2:
            if (arr[0] <= arr[1]): return arr
            return [arr[1], arr[0]]

        half = len(arr)//2
        a = self.merge_sort(arr[:half])
        b = self.merge_sort(arr[half:])
        return self._merge(a,b)

    def _get_original_indexes(self, nums, a, b):
        indexes = []        
        for idx, value in enumerate(nums):
            if a==value or b==value:
                indexes.append(idx)

            if len(indexes)==2:
                break
        return indexes
        

    def twoSum(self, nums, target):

        sorted_nums = self.merge_sort(nums)

        left, right = 0, len(sorted_nums)-1

        while left < right:
            value_a, value_b = sorted_nums[left], sorted_nums[right]
            lr_sum = value_a + value_b 
            
            if lr_sum == target:
                print(nums)
                return self._get_original_indexes(nums, value_a, value_b)
            
            if lr_sum > target:
                right -= 1
            
            if lr_sum < target:
                left += 1

if __name__ == "__main__":
    s = Solution()

    examples = [
        {
            "nums": [2,7,11,15],
            "target": 9
        },
        {
            "nums": [3,2,4],
            "target": 6
        },
        {
            "nums": [3,3],
            "target": 6
        },
    ]

    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        print(s.twoSum(**example))
        print()
    
    