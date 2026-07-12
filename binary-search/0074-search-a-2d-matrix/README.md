# 74. Search a 2D Matrix

**Difficulty:** Medium
**Pattern:** Binary Search (flattened index)
**Link:** https://leetcode.com/problems/search-a-2d-matrix/

## Approach
Treat the matrix as a single sorted array. Convert the binary search midpoint into a row and column using integer division and modulo.

## Complexity
- Time: O(log(m*n))
- Space: O(1)