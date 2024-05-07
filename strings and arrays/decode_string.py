# 394. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; 
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain 
# any digits and that digits are only for those repeat numbers, k. 
# For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.

class Solution: 
    def _get_integer(self, s, i):
        val = ''
        while(s[i] != '['): # could check isdigit as well
            val+=s[i]
            i+=1

        return int(val), i+1 # +1 for bracket

    def decode_inner_string(self, s, i):
        output = ''
        j = i
        while j < len(s):
            if s[j].isdigit():
                # 1) get number k 
                k, jump = self._get_integer(s, j)
                j = jump 

                # 2) get the string between brackets
                inner_string, jump = self.decode_inner_string(s, j)
                output += k * inner_string
                j = jump

            elif s[j].isalpha():
                output += s[j]
                j += 1

            elif s[j] == ']':
                # we have decoded the inner string succesfully
                return output, j+1

        return output, j

    def decodeString(self, s: str) -> str:
        output, j = self.decode_inner_string(s, i=0)

        # the decode_inner_string returns when seeing the last ]
        # there might be some chars after that, we should add them
        if j < len(s)-1:
            output += s[j:]

        return output
