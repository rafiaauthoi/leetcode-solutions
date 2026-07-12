# 853. Car Fleet

**Difficulty:** Medium
**Pattern:** Stack (sorted processing)
**Link:** https://leetcode.com/problems/car-fleet/

## Approach
Calculate each car's time to reach the target alone. Process cars from closest to target to farthest. A car merges into the fleet ahead if its time is less than or equal to the time on top of the stack; otherwise it forms a new fleet.

## Complexity
- Time: O(n log n)
- Space: O(n)