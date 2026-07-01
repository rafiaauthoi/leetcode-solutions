# 238. Product of Array Except Self

**Difficulty:** Medium
**Pattern:** Prefix / Suffix Products
**Link:** https://leetcode.com/problems/product-of-array-except-self/

## Approach
Build the result in two passes without division. First pass stores the product of all elements before each index (prefix). Second pass multiplies in the product of all elements after each index (suffix).

## Complexity
- Time: O(n)
- Space: O(1) extra space, not counting the output array