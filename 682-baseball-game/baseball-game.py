class Solution:
    def calPoints(self, operations=list[int])->int:

        lst=[]

        for i in operations:
          if i=="+":
             lst.append(lst[-1]+lst[-2])#add
          elif i=="C":
             lst.pop()#delete
          elif i=="D":
              lst.append(lst[-1]*2)#double
          else :
            lst.append(int(i))#last m convert string to int agr bch raha h kch
        return sum(lst)#sbka sum 
