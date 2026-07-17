from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        # Frequency of each number
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1

        # divisible[g] = how many numbers are divisible by g
        divisible = [0] * (max_val + 1)

        for g in range(1, max_val + 1):
            for multiple in range(g, max_val + 1, g):
                divisible[g] += freq[multiple]

        # pairs[g] = number of pairs whose gcd is exactly g
        pairs = [0] * (max_val + 1)

        for g in range(max_val, 0, -1):
            cnt = divisible[g]
            pairs[g] = cnt * (cnt - 1) // 2

            for multiple in range(2 * g, max_val + 1, g):
                pairs[g] -= pairs[multiple]

        # Prefix sums over gcd values
        prefix = []
        gcd_values = []

        running = 0
        for g in range(1, max_val + 1):
            if pairs[g]:
                running += pairs[g]
                prefix.append(running)
                gcd_values.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(gcd_values[idx])

        return ans




solution = Solution()
print(solution.gcdValues([2, 3, 4], [0, 2, 4]))