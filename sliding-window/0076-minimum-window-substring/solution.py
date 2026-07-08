class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        have = {}
        required = len(need)
        formed = 0

        left = 0
        best_len = float("inf")
        best_left, best_right = 0, 0

        for right in range(len(s)):
            char = s[right]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                formed += 1

            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left, best_right = left, right

                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return s[best_left:best_right + 1] if best_len != float("inf") else ""