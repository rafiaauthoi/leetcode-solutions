# 567. Permutation in String

**Difficulty:** Medium
**Pattern:** Fixed-Size Sliding Window
**Link:** https://leetcode.com/problems/permutation-in-string/

## Approach
Compare letter frequency counts between s1 and a fixed-size window in s2. Slide the window one step at a time, updating counts incrementally instead of recomputing from scratch.

## Complexity
- Time: O(n)
- Space: O(1), fixed alphabet size