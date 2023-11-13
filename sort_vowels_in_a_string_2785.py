# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2023-11-13

class SortVowelsInAString_2785:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        vowels_cnts = {vowel: 0 for vowel in vowels}
        for ch in s:
            if ch in vowels_cnts:
                vowels_cnts[ch] += 1
        res = list(s)
        inx = 0
        for i in range(len(res)):
            if res[i] in vowels_cnts:
                while inx < len(vowels) and vowels_cnts[vowels[inx]] == 0:
                    inx += 1
                res[i] = vowels[inx]
                vowels_cnts[vowels[inx]] -= 1
        return ''.join(res)
