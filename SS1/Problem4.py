class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return str(self.getX()), str(self.getY())

    def __eq__(self):
    if self.x == self.y:
        return True

    def __repr__(self):
    return 'Coordinate(' + str(self.getX()) + ', ' + str(self.getY()) + ')'