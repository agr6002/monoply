from graphics import *
class View:
    def __init__(self, win, app):
        self.win = win
        self.app = app
        
    def drawBoard(self):
        for i in range(40):
            self.app.model.boxes[i].draw()  
            #print(i)     

    def initialize(self):
        print("  initializing View")

    def run(self):
        #print("  running View")
        self.drawBoard()

    def finalize(self):
        print("  finalizing View")    