# 875. Koko Eating Bananas

**Difficulty:** Medium
**Pattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/koko-eating-bananas/

## Approach
Binary search over possible eating speeds instead of array indices. For each candidate speed, calculate total hours needed using ceiling division, and narrow toward the minimum speed that still finishes in time.

## Complexity
- Time: O(n log m), where m is the max pile size
- Space: O(1)