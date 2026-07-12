# 33. Search in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search (rotated array)
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Approach
At each step, determine which half of the array is properly sorted, then check whether the target falls within that half's range to decide which side to search next.

## Complexity
- Time: O(log n)
- Space: O(1)