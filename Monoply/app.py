from model import Model
from view import View
from controller import Controller
from graphics import *

class App:
    def __init__(self):
        self.win = GraphWin("Monopoly", 700, 700)
        self.win.setBackground("blue")
        self.model = Model(self.win)
        self.view = View(self.win, self)
        self.controller = Controller(self.win)
        self.isPlaying = True

        self.start()

    def start(self):
        self.initialize()
        self.run()
        self.finalize()

    def initialize(self):
        print("initializing App")
        self.model.initialize()
        self.view.initialize()
        self.controller.initialize()

    def run(self):
        print("running App")
        while(self.isPlaying == True):
            self.model.run()
            self.view.run()
            self.controller.run()

    def finalize(self):
        print("finalizing App")        
        self.model.finalize()
        self.view.finalize()
        self.controller.finalize()
