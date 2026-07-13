# 25. Reverse Nodes in k-Group

**Difficulty:** Hard
**Pattern:** Bounded iterative reversal, repeated per group
**Link:** https://leetcode.com/problems/reverse-nodes-in-k-group/

## Approach
For each group, first check that at least k nodes remain. Reverse exactly k nodes using the standard iterative reversal, then reconnect the reversed group to the previous group's tail and the next group's head.

## Complexity
- Time: O(n)
- Space: O(1)