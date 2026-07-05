# 42. Trapping Rain Water

**Difficulty:** Hard
**Pattern:** Two Pointers
**Link:** https://leetcode.com/problems/trapping-rain-water/

## Approach
Track the max height seen so far from both the left and right sides using two pointers. Always process the side with the smaller max, since that side's water level is already certain, regardless of what's on the other side.

## Complexity
- Time: O(n)
- Space: O(1)