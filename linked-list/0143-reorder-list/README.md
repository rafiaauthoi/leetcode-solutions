# 143. Reorder List

**Difficulty:** Medium
**Pattern:** Find middle, reverse second half, merge
**Link:** https://leetcode.com/problems/reorder-list/

## Approach
Find the middle with fast and slow pointers, reverse the second half, then merge the two halves by alternating nodes from each.

## Complexity
- Time: O(n)
- Space: O(1)