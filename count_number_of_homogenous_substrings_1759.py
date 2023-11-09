# https://leetcode.com/problems/count-number-of-homogenous-substrings/description/?envType=daily-question&envId=2023-11-09

class CountNumberOfHomogenousSubstrings_1759:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        total = 0
        mod = int(1e+9 + 7)
        inx = 0

        while inx < n:
            same_char_cnt = 0
            while inx + same_char_cnt < n and s[inx] == s[inx + same_char_cnt]:
                same_char_cnt += 1
            total += same_char_cnt * (same_char_cnt + 1) // 2
            inx += same_char_cnt
        return total % mod
