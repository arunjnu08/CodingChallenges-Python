# https://leetcode.com/problems/longest-palindromic-substring/?envType=daily-question&envId=2023-10-27

class LongestPalindromicSubstring_5:
    def longestPalindrome(self, s: str) -> str:
        min_left, max_right, max_len = -1, -1, 0
        n = len(s)
        def check(left: int, right: int):
            nonlocal min_left, max_right, max_len
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            palin_len = right - left - 1
            if palin_len > max_len:
                min_left, max_right, max_len = left, right, palin_len
        
        for i in range(n):
            check(i, i)
            check(i - 1, i)
        return s[min_left + 1 : max_right]
