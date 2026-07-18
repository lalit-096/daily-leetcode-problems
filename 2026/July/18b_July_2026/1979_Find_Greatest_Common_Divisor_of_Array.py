from math import gcd
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
        
        
solution = Solution()
print(solution.findGCD([2, 5, 6, 9, 10]))  # Output: 2
print(solution.findGCD([7,5,6,8,3]))  # Output: 1
print(solution.findGCD([3,3]))  # Output: 3