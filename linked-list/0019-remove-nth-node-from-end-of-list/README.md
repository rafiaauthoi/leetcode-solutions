# 19. Remove Nth Node From End of List

**Difficulty:** Medium
**Pattern:** Two pointers with a fixed gap
**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Approach
Advance fast n steps ahead, then move slow and fast together until fast reaches the last node. Slow ends up right before the node to remove.

## Complexity
- Time: O(n)
- Space: O(1)