# 49. Group Anagrams

**Difficulty:** Medium
**Pattern:** Hash Map (sorted string as key)
**Link:** https://leetcode.com/problems/group-anagrams/

## Approach
Sort the letters of each word to create a label that's identical for all anagrams of that word. Use that label as a dictionary key, grouping original words into lists under matching labels.

## Complexity
- Time: O(n * k log k), where n is the number of words and k is the max word length (sorting each word)
- Space: O(n * k)