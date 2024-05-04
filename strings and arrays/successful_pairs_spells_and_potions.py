from math import ceil
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """Derived from @paramkumar1"""
        
        potions, m = sorted(potions), len(potions)
        pairs = []
        for spell in spells:
            min_strength_needed = ceil(success / spell)
            j = bisect.bisect_left(potions, min_strength_needed)
            pairs.append(m-j)
        
        return pairs
