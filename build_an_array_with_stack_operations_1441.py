# https://leetcode.com/problems/build-an-array-with-stack-operations/description/?envType=daily-question&envId=2023-11-03

class BuildAnArrayWithStackOperations_1441:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        num = 1
        for x in target:
            while True:
                res.append("Push")
                if num == x:
                    break;
                else:
                    res.append("Pop")
                num += 1
            num += 1
        return res    
