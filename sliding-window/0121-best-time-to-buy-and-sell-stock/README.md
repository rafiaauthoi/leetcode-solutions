# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**Pattern:** Sliding Window (single pass)
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Approach
Track the lowest price seen so far while scanning once. At each day, either update the minimum or check if selling today beats the best profit found so far.

## Complexity
- Time: O(n)
- Space: O(1)