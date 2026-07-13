# 146. LRU Cache

**Difficulty:** Medium
**Pattern:** Hash map plus doubly linked list
**Link:** https://leetcode.com/problems/lru-cache/

## Approach
Use a hash map for O(1) key lookup and a doubly linked list to track usage order, with dummy nodes marking the LRU and MRU ends. Every get or put moves the accessed node to the MRU end. Evict from the LRU end when capacity is exceeded.

## Complexity
- Time: O(1) average for get and put
- Space: O(capacity)