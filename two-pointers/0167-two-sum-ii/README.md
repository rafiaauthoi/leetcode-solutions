# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Medium
**Pattern:** Two Pointers
**Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

## Approach
Since the array is sorted, use two pointers from both ends. Move left forward if the sum is too small, move right backward if too big.

## Complexity
- Time: O(n)
- Space: O(1)