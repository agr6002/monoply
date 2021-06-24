from graphics import *
class Box:
    def __init__(self, win):
        self.win = win

    def draw(self):
        self.img = Image(Point(self.x, self.y), self.pic)
        self.img.draw(self.win)