class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def GetX(self):
        return self.x

    def GetY(self):
        return self.y

    def DistancefromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5
     
    def DistanceFromPoint(self,target):
        return ((self.x-target.x)**2+(self.y-target.y**2)) ** 0.5
    
    def Reflect_x(self):
        self.y = -(self.y)
    
    def SlopefromOrigin(self):
        if self.x == 0:
            return None
        else:
            return(self.y/self.x)

    def GetLineTo(self, pts):
        m = (self.y - pts.y)/(self.x - pts.x)
        c = self.y - (self.x) * m
        return m, c
    
    def Move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self.x , self.y
    
    def __str__(self):
        return str(self.x) + "," + str(self.y)
    
    def Halfway(self, pts):
        mx = (self.x + pts.x) / 2
        my = (self.y + pts.y) / 2
        return Point(mx, my)
    
    def PBi(pts,secpts):
        h = pts.halfway(secpts)
        line = pts.get_line_to(secpts)
        m = -(1 / line[0])
        c = h.y - m * (h.x)
        return (m,c)
    
    def Mid(self, pts, secpts):
        self.x = (self.x + pts.x) / 2
        self.y = (self.y + pts.y) / 2
        secpts.x = (secpts.x + pts.x) / 2
        secpts.y = (secpts.y + pts.y) / 2
    
    def find_circle(pts,secpts,thipts):
        h1 = PBi(pts,secpts)
        h2 = PBi(secpts,thipts)
        c = find_intersect(h1,h2)
        return (c , c.distanceFromPoint(h1))
