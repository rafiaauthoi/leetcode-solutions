# 21. Merge Two Sorted Lists

**Difficulty:** Easy
**Pattern:** Dummy node, two pointers
**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

## Approach
Use a dummy head and a tail pointer. Compare the current nodes of both lists, attach the smaller one, and advance that list. Attach whatever remains once one list is exhausted.

## Complexity
- Time: O(n + m)
- Space: O(1)