# 219. Contains Duplicate II

**Difficulty:** Easy
**Pattern:** Hash Map (index tracking)
**Link:** https://leetcode.com/problems/contains-duplicate-ii/

## Approach
Track the last seen index of each number in a dictionary. If a number repeats within k indices of its last occurrence, return True.

## Complexity
- Time: O(n)
- Space: O(n)