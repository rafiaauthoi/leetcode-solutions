# 424. Longest Repeating Character Replacement

**Difficulty:** Medium
**Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/longest-repeating-character-replacement/

## Approach
Track character frequency and the max frequency of any single character in the current window. If (window size - max frequency) exceeds k, shrink the window from the left.

## Complexity
- Time: O(n)
- Space: O(1), fixed alphabet size