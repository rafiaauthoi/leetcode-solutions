# 125. Valid Palindrome

**Difficulty:** Easy
**Pattern:** Two Pointers
**Link:** https://leetcode.com/problems/valid-palindrome/

## Approach
Use two pointers starting from both ends of the string, moving inward. Skip non-alphanumeric characters on either side, then compare remaining characters case-insensitively. Return False on the first mismatch.

## Complexity
- Time: O(n)
- Space: O(1)