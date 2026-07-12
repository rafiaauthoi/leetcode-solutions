# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Pattern:** Stack
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Approach
Push numbers onto a stack. On an operator, pop the top two values, apply the operator, and push the result back. The final value left in the stack is the answer.

## Complexity
- Time: O(n)
- Space: O(n)