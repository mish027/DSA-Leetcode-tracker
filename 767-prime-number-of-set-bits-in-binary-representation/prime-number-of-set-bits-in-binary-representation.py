class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        
        countPrime=0
        for i in range(left,right+1):
            count=0
            flag=1
            n=i
            while n>0:
                if ((n&1)==1):
                    count+=1
                n=n>>1

            if count==1:
                flag=0


            for j in range(2,(count//2)+1):

                
                if (count%j)==0:
                    flag=0
                    break
            if flag==1:
                countPrime+=1
        
        return countPrime
                
                


        