class Point:
    def __init__(self, x,y):
        self.coordX = x
        self.coordY = y

    def __iter__(self):
        yield (self.coordX, self.coordY)

    def checkOrigin(self):
        if self.coordX == 0 and self.coordY == 0:
            return True
        else:
            return False

    

class Line:
    def __init__(self, p1, p2):
        if isinstance(p1, Point) == True:
            self.point1 = p1
        else:
            self.point1 = Point(p1[0],p1[1])
        if isinstance(p2, Point) == True:
            self.point2 = p2
        else:
            self.point2 = Point(p2[0],p2[1])

    def __iter__(self):
        yield (self.point1,self.point2)

    def exists(self):
        if self.point1.coordX == self.point2.coordX and self.point1.coordY == self.point2.coordY:
            return False
        else:
            return True

    def slope(self):
        if self.exists() == True:
            if self.point1.coordX == self.point2.coordX:
                return 'infinity'
            else:
                return (self.point2.coordY - self.point1.coordY)/(self.point2.coordX - self.point1.coordX)
        else:
            return 'points overlap, no line formed'
            
