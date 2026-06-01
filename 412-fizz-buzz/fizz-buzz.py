class Solution(object):
    def fizzBuzz(self, n):
        x=[]
        for i in range(n):
            if (i+1)%15==0:
                m="FizzBuzz"
                x.append(m)
            elif (i+1)%5==0:
                m="Buzz"
                x.append(m)
            elif (i+1)%3==0:
                m="Fizz"
                x.append(m)
            else:
                m=str(i+1)
                x.append(m)
        return(x)
        