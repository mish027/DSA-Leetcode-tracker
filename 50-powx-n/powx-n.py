class Solution:
    def myPow(self, x: float, n: int) -> float:

        def powerFun(x,n):
                if n==0:
                    return 1
                half = powerFun(x,n//2)
                
                if n%2==0:
                    return half*half
                else:
                    return x*half*half     
        if n<0:
            x=1/x
            n=-n
        return powerFun(x,n)

        

        