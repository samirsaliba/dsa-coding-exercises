# 322. Coin Change

# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def _eval_amount(self, n):
        if n in self._cache:
            return self._cache[n]
            
        possibilities_for_n = []
        for coin in self._coins:
            
            if n-coin <= 0:
                continue
            value, num_of_coins = self._eval_amount(n-coin)
            if num_of_coins != -1:
                possibilities_for_n.append((n, num_of_coins+1))

        if len(possibilities_for_n) == 0:
            # Cannot find solution for this amount
            result = (-1, -1)
        else:
            result = min(possibilities_for_n, key = lambda x: x[1])
            
        self._cache[n] = result
        return result


    def _init_cache(self):
        self._cache = {}
        for coin in self._coins:
            number_of_coins = 1
            value = coin
            self._cache[coin] = (value, number_of_coins)

    def coinChange(self, coins, amount):
        if amount==0: return 0
        self._coins = coins
        self._init_cache()
        result = self._eval_amount(n=amount)
        return result[1]


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
    
    