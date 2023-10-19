class BackspaceStringCompare:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1

        while i >= 0 and j >= 0:
            cnt = 0
            while i >= 0:
                if s[i] == '#':
                    cnt+= 1
                else:
                    cnt -= 1
                    if cnt < 0:
                        break
                i -= 1
            
            cnt = 0
            while j >= 0:
                if t[j] == '#':
                    cnt += 1
                else:
                    cnt -= 1
                    if cnt < 0:
                        break
                j -= 1
            
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            
            if (i >= 0 and j < 0) or (i < 0 and j >= 0):
                return False
            
            i -= 1
            j -= 1
        
        cnt = 0
        while i >= 0:
            if s[i] == '#':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    break
            i -= 1
        
        cnt = 0 
        while j >= 0:
            if t[j] == '#':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    break
            j -= 1
        
        return i < 0 and j < 0
