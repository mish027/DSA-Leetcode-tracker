class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''y3-y2 = y2-y1
        x3-x2   x2-x1'''  
        if len(coordinates)==2:
            return True

        for x in range(2,len(coordinates)):
            if (coordinates[x][1]-coordinates[x-1][1])*(coordinates[x-1][0]-coordinates[x-2][0])!=(coordinates[x][0]-coordinates[x-1][0])*(coordinates[x-1][1]-coordinates[x-2][1]):
                return False
        return True


