# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=daily-question&envId=2023-10-30 

class SortIntegersByTheNumberOf1Bits_1356:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = sorted(arr, key=lambda x : (x.bit_count(), x))
        return res
