# 3501. Maximize Active Section with Trade II

**Difficulty:** Hard

## Problem Description

You are given a binary string `s` of length `n`, where:

- `'1'` represents an active section.
- `'0'` represents an inactive section.

You can perform at most one trade to maximize the number of active sections in `s`. In a trade, you:

1. Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all `'0'`s.
2. Afterward, convert a contiguous block of `'0'`s that is surrounded by `'1'`s to all `'1'`s.

Additionally, you are given a 2D array `queries`, where `queries[i] = [li, ri]` represents a substring `s[li...ri]`.

For each query, determine the maximum possible number of active sections in `s` after making the optimal trade on the substring `s[li...ri]`.

Return an array `answer`, where `answer[i]` is the result for `queries[i]`.

> Note: For each query, treat `s[li...ri]` as if it is augmented with a `'1'` at both ends, forming `t = '1' + s[li...ri] + '1'`. The augmented `'1'`s do not contribute to the final count.

## Examples

### Example 1

**Input:** `s = "01", queries = [[0,1]]`

**Output:** `[1]`

**Explanation:**
- There is no block of `'1'`s surrounded by `'0'`s, so no valid trade is possible.
- The maximum number of active sections is `1`.

### Example 2

**Input:** `s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]`

**Output:** `[4,3,1,1]`

**Explanation:**
- Query `[0,3]` → substring `"0100"` → augmented to `"101001"`
- Choose `"0100"`, convert it to `"0000"`, then to `"1111"`
- The final string without augmentation is `"1111"`, so the maximum number of active sections is `4`
- Query `[0,2]` → optimal result is `3`
- Query `[1,3]` → no valid trade is possible, so the result is `1`
- Query `[2,3]` → no valid trade is possible, so the result is `1`

### Example 3

**Input:** `s = "1000100", queries = [[1,5],[0,6],[0,4]]`

**Output:** `[6,7,2]`

**Explanation:**
- Query `[1,5]` → substring `"00010"` → augmented to `"1000101"`
- Choose `"00010"`, convert it to `"00000"`, then to `"11111"`
- The final string without augmentation is `"1111110"`, so the maximum number of active sections is `6`
- Query `[0,6]` → optimal result is `7`
- Query `[0,4]` → no valid trade is possible, so the result is `2`

### Example 4

**Input:** `s = "01010", queries = [[0,3],[1,4],[1,3]]`

**Output:** `[4,4,2]`

**Explanation:**
- Query `[0,3]` → optimal result is `4`
- Query `[1,4]` → optimal result is `4`
- Query `[1,3]` → no valid trade is possible, so the result is `2`

## Constraints

- `1 <= n == s.length <= 10^5`
- `1 <= queries.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`
- `queries[i] = [li, ri]`
- `0 <= li <= ri < n`