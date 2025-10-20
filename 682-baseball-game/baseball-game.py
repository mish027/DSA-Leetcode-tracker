class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]

        for operation in operations:

            if operation[0]=='-': #isnumeric() works only for positive digits,negatives fail.
                res.append(-int(operation[1:])) #For negatives:convert string after '-' to int, then negate.
            elif operation.isnumeric(): 
                res.append(int(operation))
            elif operation=='C':
                res.pop()
            elif operation=='D':
                res.append(2*(res[-1]))
            else:
                res.append(sum(res[-2:]))
        return sum(res)