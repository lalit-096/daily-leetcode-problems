from typing import List

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Build run-length blocks: (char, start, end, length)
        blocks, i = [], 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            blocks.append((s[i], i, j - 1, j - i))
            i = j
        m = len(blocks)
        
        # Map each position → its block index
        blk = [0] * n
        for bi in range(m):
            _, st, en, _ = blocks[bi]
            for p in range(st, en + 1):
                blk[p] = bi
        
        total_ones = s.count('1')
        
        # val[k] = gain for interior 1-block k = left_0_len + right_0_len
        val = [-1] * m
        for k in range(1, m - 1):
            if blocks[k][0] == '1':
                val[k] = blocks[k - 1][3] + blocks[k + 1][3]
        
        # Sparse table for O(1) range max
        sparse, j = [val[:]], 1
        while (1 << j) <= m:
            prev, half, cur = sparse[-1], 1 << (j - 1), [-1] * m
            for i in range(m - (1 << j) + 1):
                cur[i] = max(prev[i], prev[i + half])
            sparse.append(cur)
            j += 1
        
        def range_max(l, r):
            if l > r: return -1
            l, r = max(l, 0), min(r, m - 1)
            if l > r: return -1
            k = (r - l + 1).bit_length() - 1
            return max(sparse[k][l], sparse[k][r - (1 << k) + 1])
        
        results = []
        for ql, qr in queries:
            lb, rb = blk[ql], blk[qr]
            
            # Valid range for candidate 1-blocks
            k_min = lb + 2 if blocks[lb][0] == '1' else lb + 1
            k_max = rb - 2 if blocks[rb][0] == '1' else rb - 1
            
            if k_min > k_max:
                results.append(total_ones)
                continue
            
            max_gain = 0
            
            # 1) Interior candidates (both neighboring 0-blocks fully inside)
            g = range_max(lb + 2, rb - 2)
            if g > max_gain: max_gain = g
            
            # 2) Left boundary: k = lb+1 (left 0-block truncated by ql)
            if blocks[lb][0] == '0':
                k = lb + 1
                if k <= k_max and k < m:
                    left_size = blocks[lb][2] - ql + 1  # truncated
                    kp1 = lb + 2
                    if kp1 < m and kp1 <= rb:
                        right_size = (qr - blocks[rb][1] + 1) if kp1 == rb else blocks[kp1][3]
                        if left_size + right_size > max_gain:
                            max_gain = left_size + right_size
            
            # 3) Right boundary: k = rb-1 (right 0-block truncated by qr)
            if blocks[rb][0] == '0':
                k = rb - 1
                if k >= k_min and k >= 0:
                    right_size = qr - blocks[rb][1] + 1  # truncated
                    km1 = rb - 2
                    if km1 >= 0 and km1 >= lb:
                        left_size = (blocks[lb][2] - ql + 1) if km1 == lb else blocks[km1][3]
                        if left_size + right_size > max_gain:
                            max_gain = left_size + right_size
            
            results.append(total_ones + max_gain)
        
        return results