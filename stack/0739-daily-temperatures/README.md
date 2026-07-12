# 739. Daily Temperatures

**Difficulty:** Medium
**Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/daily-temperatures/

## Approach
Maintain a stack of indices with decreasing temperatures. When a warmer day is found, pop indices off the stack and record the day difference as the answer for each.

## Complexity
- Time: O(n)
- Space: O(n)