# 287. Find the Duplicate Number

**Difficulty:** Medium
**Pattern:** Floyd's cycle detection on an array
**Link:** https://leetcode.com/problems/find-the-duplicate-number/

## Approach
Treat each index as a node and nums[i] as a pointer to the next node. The duplicate value creates a cycle. Use fast and slow pointers to find a meeting point, then reset one pointer to the start and advance both one step at a time to find the cycle entrance, which is the duplicate.

## Complexity
- Time: O(n)
- Space: O(1)