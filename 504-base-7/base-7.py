class Solution:
    def convertToBase7(self, num: int) -> str:

        s = ""

        if num<0:
            nu=-num
        else:
            nu = num

        while nu>0:
            remain=nu%7
            s = str(remain)+s
            nu=nu//7

        if num==0:
            return "0"
        if num<0:
            return "-" + s
        return s

        #mistake:
        # didnt consider -ve numbers
        # return '-'+ s 
