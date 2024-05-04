# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, 
# and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def _trib_recursive(self, n):
        if n < 3:
            if n == 0: return 0
            return 1
        if n in self._cache:
            return self._cache[n]
        
        trib_n = self._trib(n-1) + self._trib(n-2) + self._trib(n-3)
        self._cache[n] = trib_n
        return trib_n

    def _trib_iter(self, n):
        trib = [0, 1, 1]
        if n<3:
            return trib[n]
        
        for i in range(3, n+1):
            trib.append(trib[i-1] + trib[i-2] + trib[i-3])
        
        return trib[-1]

    def tribonacci(self, n: int) -> int:
        return self._trib_iter(n)
