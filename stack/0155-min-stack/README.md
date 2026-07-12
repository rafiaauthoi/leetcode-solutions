# 155. Min Stack

**Difficulty:** Medium
**Pattern:** Stack (auxiliary min-tracking stack)
**Link:** https://leetcode.com/problems/min-stack/

## Approach
Maintain a second stack alongside the main one, tracking the minimum value at each point in time. Push and pop from both stacks together so the min stack always reflects the correct minimum after removals.

## Complexity
- Time: O(1) for all operations
- Space: O(n)