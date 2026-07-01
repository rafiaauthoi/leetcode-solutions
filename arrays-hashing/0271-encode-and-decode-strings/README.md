# 271. Encode and Decode Strings

**Difficulty:** Medium
**Pattern:** String manipulation (length-prefixed encoding)
**Link:** https://neetcode.io/problems/string-encode-and-decode

## Approach
Prefix each string with its length followed by a delimiter (#) before concatenating. When decoding, read the length before each delimiter to know exactly how many characters to extract next, avoiding ambiguity from characters inside the strings themselves.

## Complexity
- Time: O(n), where n is the total number of characters across all strings
- Space: O(n)