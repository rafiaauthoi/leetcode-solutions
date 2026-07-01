# 128. Longest Consecutive Sequence

**Difficulty:** Medium
**Pattern:** Hash Set (sequence start detection)
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

## Approach
Store all numbers in a set. Only start counting a sequence from numbers that are a true sequence start (num - 1 not in the set), then count upward while the next number exists in the set. This avoids recounting the same sequence multiple times, keeping the algorithm O(n) overall.

## Complexity
- Time: O(n)
- Space: O(n)