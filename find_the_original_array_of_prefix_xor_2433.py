# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/submissions/1088045086/?envType=daily-question&envId=2023-10-31

class FindTheOriginalArrayOfPrefixXor_2433:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = []
        pre = 0
        for x in pref:
            arr.append(x ^ pre)
            pre = x
        return arr
