# 84. Largest Rectangle in Histogram

**Difficulty:** Hard
**Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## Approach
Maintain a stack of (start_index, height) pairs in increasing height order. When a shorter bar appears, pop taller bars and calculate their max rectangle area using the current position as the right boundary. Remaining bars on the stack at the end extend to the array's edge.

## Complexity
- Time: O(n)
- Space: O(n)