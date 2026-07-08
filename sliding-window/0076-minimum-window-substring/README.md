# 76. Minimum Window Substring

**Difficulty:** Hard
**Pattern:** Variable-Size Sliding Window
**Link:** https://leetcode.com/problems/minimum-window-substring/

## Approach
Expand the window until all required characters (with correct counts) are present, tracked via a formed/required counter. Then shrink from the left as much as possible while staying valid, recording the smallest valid window found.

## Complexity
- Time: O(n + m)
- Space: O(n + m)