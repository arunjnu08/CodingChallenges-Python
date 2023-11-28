# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description/?envType=daily-question&envId=2023-11-28

class NumberOfWaysToDivideALongCorridor_2147:
    def numberOfWays(self, corridor: str) -> int:
        s, s_cnt, n = 0, 0, len(corridor)
        while s < n and s_cnt != 2:
            if corridor[s] == 'S':
                s_cnt += 1
            s += 1
        
        if s_cnt != 2:
            return 0
        if s == n:
            return 1
        
        mod = 1000000007
        ans = 1

        while s < n:
            s_cnt, p_cnt = 0, 0
            while s < n and corridor[s] == 'P':
                p_cnt += 1
                s += 1
            if s == n:
                break
            
            ans = (ans * (p_cnt + 1)) % mod
            while s < n and s_cnt != 2:
                if corridor[s] == 'S':
                    s_cnt += 1
                s += 1
            if s_cnt != 2:
                return 0
        
        return ans
