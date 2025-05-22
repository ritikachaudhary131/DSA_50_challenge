class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        lst = []

        for i in operations:
            if i == 'C': #cancel toh pop out krdo last mai s
                lst.pop()
            elif i == 'D':
                lst.append(lst[-1]*2)#last element ko double krke list m add krdo

            elif i == '+':
                lst.append(lst[-1]+lst[-2])#score add krke show krdo 
            else:
                lst.append(int(i))#string ko int m convert krke chrd do
        return sum(lst)
