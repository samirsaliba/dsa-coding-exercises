# 1657. Determine if Two Strings Are Close
# Two strings are considered close if you can attain one from the other
# using the following operations:

# Operation 1: Swap any two existing characters.
#   For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character
# into another existing character, and do the same with the other character.
#   For example, aacabb -> bbcbaa 
#   (all a's turn into b's, and all b's turn into a's)

# You can use the operations on either string as many times as necessary.
# Given two strings, word1 and word2, 
# return true if word1 and word2 are close, and false otherwise.

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # operation 1 means the order doesn't matter, just the frequencies
        # operation 2 means we can switch frequencies if we want 
        #   (transform a->b and b->a)

        def words_to_freq(word):
            letters = dict()
            for s in word:
                if s in letters:
                    letters[s] += 1
                else:
                    letters[s] = 1
            return letters
        
        letters1 = words_to_freq(word1)
        letters2 = words_to_freq(word2)

        # now we need to check two conditions
        # if they have the same letters
        # and if the frequencies match
        return (
            set(letters1.keys()) == set(letters2.keys())
            and sorted(letters1.values()) == sorted(letters2.values())
        )
        
