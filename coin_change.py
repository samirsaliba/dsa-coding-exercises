# 322. Coin Change

# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

import math
class Solution:
    def _eval_amount(self, n):
        if n in self._cache:
            return self._cache[n]

        coins_n = math.inf
        for coin in self._coins:
            if n == coin:
                coins_n = 1
                break
            if n-coin <= 0:
                continue
            coins_n = min(coins_n, self._eval_amount(n-coin) + 1)
            
        self._cache[n] = coins_n
        return coins_n


    def coinChange(self, coins, amount):
        self._cache = {}
        self._coins = coins
        if amount == 0: 
            return 0
        result = self._eval_amount(n=amount)

        if result == math.inf:
            return -1
        return result


if __name__ == "__main__":
    s = Solution()

    examples = [
        {
            "args": {
                "coins": [1,2,5],
                "amount": 11
            },
            "solution": 3
        },
            {
            "args": {
                "coins": [2],
                "amount": 3
            },
            "solution": -1
        },
            {
            "args": {
                "coins": [1],
                "amount": 0
            },
            "solution": 0
        }
    ]


    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        result = s.coinChange(**example["args"])
        print(result)
        assert result == example["solution"], "Not the expected result"
        print()
    
    