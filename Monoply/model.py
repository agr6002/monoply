from box import Box
class Model:
    def __init__(self, win):
        self.win = win
        self.boxes = []
        for i in range(40):
            self.boxes.append(Box(self.win))
        self.boxes[0].x = 654
        self.boxes[0].y = 654
        self.boxes[0].pic = "big-box.png"
        self.boxes[10].x = 47
        self.boxes[10].y = 654
        self.boxes[10].pic = "big-box.png"
        self.boxes[20].x = 47
        self.boxes[20].y = 47
        self.boxes[20].pic = "big-box.png"
        self.boxes[30].x = 654
        self.boxes[30].y = 47
        self.boxes[30].pic = "big-box.png"

        a = 0
        for i in range(9):
            a += 1
            self.boxes[a].x = (i)* 57 + 123 
            self.boxes[a].y = 654
            self.boxes[a].pic = "small-box-updown.png"

        b = 10
        for i in range(9):
            b += 1
            self.boxes[b].x = 47
            self.boxes[b].y = (i) * 57 + 123
            self.boxes[b].pic ="small-box-leftright.png"  
        
        c = 20
        for i in range(9):
            c += 1
            self.boxes[c].x = (i) * 57 + 123   
            self.boxes[c].y = 47
            self.boxes[c].pic = 'small-box-updown.png'  
            print(c)  

        d = 30
        for i in range(9):
            d += 1
            self.boxes[d].x = 654
            self.boxes[d].y = (i) * 57 + 123
            self.boxes[d].pic = "small-box-leftright.png"   


    def initialize(self):
        print("  initializing Model")

    def run(self):
        #print("  running Model")
        return

    def finalize(self):
        print("  finalizing Model")    