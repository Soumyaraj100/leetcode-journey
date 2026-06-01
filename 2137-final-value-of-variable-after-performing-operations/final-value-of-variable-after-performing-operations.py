class Solution(object):
    def finalValueAfterOperations(self, operations):
        X=0
        m=[]
        for i in range(len(operations)):
            if operations[i]=="--X" or operations[i]=="X--":
                m.append(-1)
            elif operations[i]=="++X" or operations[i]=="X++":
                m.append(+1)
        n=sum(m)
        return n
        