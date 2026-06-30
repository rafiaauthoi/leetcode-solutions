# 1. Two Sum

**Difficulty:** Easy
**Pattern:** Brute Force (nested loop)
**Link:** https://leetcode.com/problems/two-sum/

## Approach
Check every possible pair of numbers in the list. For each number, look at every number after it and see if the two add up to the target. Return their indices as soon as a match is found.

## Complexity
- Time: O(n²) — nested loop checks every pair
- Space: O(1) — no extra data structures used

## Notes
This is the brute force solution. A faster O(n) approach using a hash map is possible by storing seen numbers and their indices as you go, instead of checking every pair.