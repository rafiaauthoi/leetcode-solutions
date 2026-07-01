# 220. Contains Duplicate III

**Difficulty:** Hard
**Pattern:** Bucketing / Sliding Window
**Link:** https://leetcode.com/problems/contains-duplicate-iii/

## Approach
Group numbers into buckets sized valueDiff + 1. Check the number's own bucket and neighboring buckets for a close match. Maintain a sliding window of size indexDiff by removing outdated numbers.

## Complexity
- Time: O(n)
- Space: O(min(n, indexDiff))