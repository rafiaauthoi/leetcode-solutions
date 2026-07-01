# 242. Valid Anagram

**Difficulty:** Easy
**Pattern:** Hash Map (frequency count)
**Link:** https://leetcode.com/problems/valid-anagram/

## Approach
Compare lengths first as a quick exit. Then build a frequency count (dictionary) of letters for each string and compare the two dictionaries directly.

## Complexity
- Time: O(n)
- Space: O(n)