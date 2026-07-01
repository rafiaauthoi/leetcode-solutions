# 347. Top K Frequent Elements

**Difficulty:** Medium
**Pattern:** Hash Map + Bucket Sort
**Link:** https://leetcode.com/problems/top-k-frequent-elements/

## Approach
Count frequency of each number with a dictionary. Place numbers into buckets indexed by frequency (bucket sort). Walk backward from the highest frequency bucket, collecting numbers until k are found.

## Complexity
- Time: O(n)
- Space: O(n)