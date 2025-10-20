class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]

        for operation in operations:

            if operation[0]=='-':
                res.append(-int(operation[1:]))
            elif operation.isnumeric():
                res.append(int(operation))
            elif operation=='C':
                res.pop()
            elif operation=='D':
                res.append(2*(res[-1]))
            else:
                res.append(sum(res[-2:]))
        return sum(res)