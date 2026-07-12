# 981. Time Based Key-Value Store

**Difficulty:** Medium
**Pattern:** Binary Search + Hash Map
**Link:** https://leetcode.com/problems/time-based-key-value-store/

## Approach
Store timestamp/value pairs per key in an append-only list, naturally sorted since timestamps are strictly increasing. Binary search each key's list to find the largest timestamp that is still less than or equal to the query.

## Complexity
- Time: O(log n) per get, O(1) per set
- Space: O(n)