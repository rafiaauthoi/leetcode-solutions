# 11. Container With Most Water

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** https://leetcode.com/problems/container-with-most-water/

## Approach
Start with pointers at both ends (widest container). Always move the pointer at the shorter line inward, since it's the bottleneck limiting the water level. Track the max area seen.

## Complexity
- Time: O(n)
- Space: O(1)