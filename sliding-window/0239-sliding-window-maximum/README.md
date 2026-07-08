# 239. Sliding Window Maximum

**Difficulty:** Hard
**Pattern:** Monotonic Deque
**Link:** https://leetcode.com/problems/sliding-window-maximum/

## Approach
Maintain a deque of indices in decreasing order of value. Remove smaller values from the back before adding a new index, and remove indices that fall outside the window from the front. The front of the deque is always the current window's maximum.

## Complexity
- Time: O(n)
- Space: O(k)