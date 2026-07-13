# 206. Reverse Linked List

**Difficulty:** Easy
**Pattern:** Iterative pointer reversal
**Link:** https://leetcode.com/problems/reverse-linked-list/

## Approach
Walk the list one node at a time, flipping each node's next pointer to point backward instead of forward. Track prev, curr, and a temp variable to save curr.next before overwriting it.

## Complexity
- Time: O(n)
- Space: O(1)