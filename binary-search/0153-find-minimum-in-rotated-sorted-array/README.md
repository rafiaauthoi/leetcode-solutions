# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**Pattern:** Binary Search (rotated array)
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Approach
Compare the middle element to the rightmost element to determine which half is sorted and which contains the rotation point, narrowing toward the minimum.

## Complexity
- Time: O(log n)
- Space: O(1)