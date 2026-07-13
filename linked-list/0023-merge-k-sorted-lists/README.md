# 23. Merge k Sorted Lists

**Difficulty:** Hard
**Pattern:** Min-heap
**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

## Approach
Push the head of every list onto a min-heap keyed by value. Repeatedly pop the smallest node, attach it to the result, and push its next node onto the heap if one exists.

## Complexity
- Time: O(n log k)
- Space: O(k)