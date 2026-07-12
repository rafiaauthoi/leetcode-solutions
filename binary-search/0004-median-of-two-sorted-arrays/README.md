# 4. Median of Two Sorted Arrays

**Difficulty:** Hard
**Pattern:** Binary Search (partitioning)
**Link:** https://leetcode.com/problems/median-of-two-sorted-arrays/

## Approach
Binary search on how many elements to take from the smaller array, calculating the matching partition point in the other array so both combined halves are balanced. Adjust the partition until every element on the left side is less than or equal to every element on the right side.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)