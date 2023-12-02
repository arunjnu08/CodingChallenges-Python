# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=daily-question&envId=2023-12-02

class FindWordsThatCanBeFormedByCharacters_1160:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq = Counter(chars)
        ans = 0
        for word in words:
            freq = Counter(word)
            flag = True
            for ch in freq:
                if freq[ch] > char_freq[ch]:
                    flag = False
                    break
            ans += len(word) if flag else 0
        return ans
