# 141. Linked List Cycle

**Difficulty:** Easy
**Pattern:** Fast and slow pointers (Floyd's cycle detection)
**Link:** https://leetcode.com/problems/linked-list-cycle/

## Approach
Move slow one step and fast two steps at a time. If there is a cycle, fast eventually laps slow and they land on the same node. If not, fast reaches None first.

## Complexity
- Time: O(n)
- Space: O(1)