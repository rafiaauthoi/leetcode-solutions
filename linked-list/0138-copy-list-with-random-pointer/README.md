# 138. Copy List with Random Pointer

**Difficulty:** Medium
**Pattern:** Hash map for old-to-new node mapping
**Link:** https://leetcode.com/problems/copy-list-with-random-pointer/

## Approach
First pass, create a copy of every node and store an original-to-copy mapping in a dictionary. Second pass, use the mapping to wire up each copy's next and random pointers.

## Complexity
- Time: O(n)
- Space: O(n)