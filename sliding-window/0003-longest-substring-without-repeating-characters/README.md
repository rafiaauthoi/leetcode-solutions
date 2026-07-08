# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Approach
Expand the window with a right pointer, tracking characters in a set. When a duplicate is found, shrink from the left until it's removed. Track the max window size seen.

## Complexity
- Time: O(n)
- Space: O(min(n, charset size))