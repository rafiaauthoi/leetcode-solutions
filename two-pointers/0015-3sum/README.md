# 15. 3Sum

**Difficulty:** Medium
**Pattern:** Two Pointers (sorted array)
**Link:** https://leetcode.com/problems/3sum/

## Approach
Sort the array first. Fix one number with an outer loop, then use two pointers to find the remaining pair that sums to its negative. Skip duplicate values at both the outer loop and inner pointers to avoid duplicate triplets.

## Complexity
- Time: O(n^2)
- Space: O(1) extra space (not counting sort)