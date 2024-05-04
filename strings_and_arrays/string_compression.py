# 443. String Compression
# Given an array of characters chars, 
# compress it using the following algorithm:
# Begin with an empty string s. 
# For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, 
# but instead, be stored in the input character array chars. 
# Note that group lengths that are 10 or longer 
# will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_char = None
        consecutive_num = 1
        i = 0
        for c in chars:
            if c == curr_char:
                consecutive_num += 1
            
            elif curr_char is not None:
                # end of sequence
                chars[i] = curr_char
                i+=1
                if consecutive_num > 1:
                    for x in str(consecutive_num):
                        chars[i] = x
                        i+=1
                curr_char, consecutive_num = c, 1

            else:
                curr_char = c
            
         
        if curr_char is not None:
            chars[i] = curr_char
            i+=1
            if consecutive_num > 1:
                for x in str(consecutive_num):
                    chars[i] = x
                    i+=1
        return i