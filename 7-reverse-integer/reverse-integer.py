class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
            """
            phele int ko string m convert krke, negative s postive bnao ,then reverse ,waps s usko integer bnake negative bnado by *-1 """
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
            """32 bits ki range m exist krna chahiye"""
        
        return res  