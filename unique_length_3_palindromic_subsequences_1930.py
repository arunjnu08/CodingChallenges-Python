# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2023-11-14

class UniqueLength_3PalindromicSubsequences_1930:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            inx = ord(s[i]) - ord('a')
            if first[inx] == -1:
                first[inx] = i
            last[inx] = i
        
        count = 0
        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i] + 1, last[i]):
                between.add(s[j])
            count += len(between)
        
        return count
