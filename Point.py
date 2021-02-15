class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get(self):
        xy_list = (self.x,self.y)
        return xy_list
    def move(self,dx,dy):
        self.x += dx
        self.y += dy
