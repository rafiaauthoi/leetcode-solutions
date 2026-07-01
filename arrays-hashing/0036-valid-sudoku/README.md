# 36. Valid Sudoku

**Difficulty:** Medium
**Pattern:** Hash Set (multiple grouped sets)
**Link:** https://leetcode.com/problems/valid-sudoku/

## Approach
Track seen digits with separate sets for each row, column, and 3x3 box. Box identity is computed as (row // 3, col // 3). For each filled cell, check all three sets before adding the digit to each.

## Complexity
- Time: O(1), fixed 9x9 board size
- Space: O(1), fixed number of sets