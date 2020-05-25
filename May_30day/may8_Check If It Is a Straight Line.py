class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 0:
            return True
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y2 - y1) * (x - x2) == (y - y2) * (x2 - x1):
                return True
            else:
                return False