class Solution:
    def convertToBase7(self, num: int) -> str:

        if num==0:
            return "0"
        s = ""

        nu = abs(num)

        while nu>0:
            remain=nu%7
            s = str(remain)+s
            nu=nu//7

        
        if num<0:
            return "-" + s
        return s

        #mistake:
        # didnt consider -ve numbers
        # return '-'+ s  only when num<0
        # cleaner version to use abs() instead of 
        '''if num<0:
            nu=-num
        else:
            nu = num'''
        # add 0 case in the first
