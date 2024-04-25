# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def _possibilities_step_n(self, n):
        if n in self._possibilities_cache: 
            return self._possibilities_cache[n]
        else:
            if n <= 2:
                res = n
            elif n == 0:
                res = 0
            else:
                res = self._possibilities_step_n(n-1) \
                    + self._possibilities_step_n(n-2)
            self._possibilities_cache[n] = res
            return res
            
    def climbStairs(self, n: int) -> int:
        self._possibilities_cache = {}
        return self._possibilities_step_n(n)
        
if __name__ == "__main__":
    s = Solution()
    examples = [
        {
            "args": {
                "n": 2,
            },
            "solution": 2
        },
        {
            "args": {
                "n": 3,
            },
            "solution": 3
        },
    ]

    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        result = s.climbStairs(n=example["args"]["n"])
        print(result)
        assert result == example["solution"], "Not the expected result"
        print()
        