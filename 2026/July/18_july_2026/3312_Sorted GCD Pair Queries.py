from typing import List
from math import gcd

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        gcdPairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                gcdPairs.append(gcd(nums[i], nums[j]))

        gcdPairs.sort()
        
        return [gcdPairs[q] for q in queries]




solution = Solution()
print(solution.gcdValues([2, 3, 4], [0, 2, 4]))