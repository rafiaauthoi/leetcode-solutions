# 2. Add Two Numbers

**Difficulty:** Medium
**Pattern:** Simulated digit addition with carry
**Link:** https://leetcode.com/problems/add-two-numbers/

## Approach
Walk both lists simultaneously, adding corresponding digits plus carry from the previous step. New digit is total % 10, new carry is total // 10. Continue until both lists and carry are exhausted.

## Complexity
- Time: O(max(n, m))
- Space: O(max(n, m))