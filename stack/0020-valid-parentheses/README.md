# 20. Valid Parentheses

**Difficulty:** Easy
**Pattern:** Stack
**Link:** https://leetcode.com/problems/valid-parentheses/

## Approach
Push opening brackets onto a stack. On a closing bracket, check that it matches the top of the stack, then pop. Valid only if the stack is empty at the end.

## Complexity
- Time: O(n)
- Space: O(n)