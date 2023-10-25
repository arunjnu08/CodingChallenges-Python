# https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/1083695051/?envType=daily-question&envId=2023-10-25

class KthSymbolInGrammar_779:
    def kthGrammar(self, n: int, k: int) -> int:
        while k > 2 and n > 2:
            half_len = (1 << (n - 2))
            if k > half_len:
                k -= half_len
                one_4th_len = (half_len >> 1)
                if k > one_4th_len:
                    k -= one_4th_len
                else:
                    k += one_4th_len
            n -= 1
        return k - 1
