from turtle import Screen, Turtle
import random

class Tile:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)  
        self.tiles = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,None]]
        self.lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.sshuffle()
        self.t = Turtle()
        self.t.hideturtle()
        self.screen.title("15puzzle Game")
        self.screen.setup(width=600, height=400)
        self.draw_tiles()
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")

    def draw_tiles(self): 
        self.t.speed(0)
        self.t.pu()
        self.t.goto(-80, 80)
        for r in range(4):
            for c in range(4):
                num = self.tiles[r][c]
                if num is not None:
                    self.t.pu()
                    self.t.goto(c * 40 - 80, 80 - r * 40)
                    self.t.pd()
                    self.t.write(str(num), align='center', font=('Arial', 16, 'normal'))
    
            
    def find_none_index(self):
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[r])):
                if self.tiles[r][c] is None:
                    return r, c
 
    def down(self):
        self.none = self.find_none_index()
        if self.none[0] == 0:
            pass
        else:
            self.none = self.find_none_index()
            num = self.tiles[self.none[0]-1][self.none[1]]
            self.tiles[self.none[0]-1][self.none[1]] = None
            self.tiles[self.none[0]][self.none[1]] = num
            self.t.clear()
            self.draw_tiles()


    def up(self):
        self.none = self.find_none_index()
        if self.none[0] == 3:
            pass
        else:
            num = self.tiles[self.none[0]+1][self.none[1]]
            self.tiles[self.none[0]+1][self.none[1]] = None
            self.tiles[self.none[0]][self.none[1]] = num
            self.t.clear()
            self.draw_tiles()

    def left(self):
        self.none = self.find_none_index()
        if self.none[1] == 3:
                    pass
        else:
            num = self.tiles[self.none[0]][self.none[1]+1]
            self.tiles[self.none[0]][self.none[1]+1] = None
            self.tiles[self.none[0]][self.none[1]] = num
            self.t.clear()
            self.draw_tiles()

    def right(self):
        self.none = self.find_none_index()
        if self.none[1] == 0:
            pass
        else:
            num = self.tiles[self.none[0]][self.none[1]-1]
            self.tiles[self.none[0]][self.none[1]-1] = None
            self.tiles[self.none[0]][self.none[1]] = num
            self.t.clear()
            self.draw_tiles()

    def invertion(self):
        count = 0
        a = self.lis[:]
        for i in self.lis:
            a = a[1:]
            for u in a:
                if i > u:
                    count+=1
        return count
    
    def sshuffle(self):
        while True:
            random.shuffle(self.lis)
            if self.invertion() %2 ==1 :
                break
        random_index = random.randint(0, len(self.lis))
        self.lis.insert(random_index, None)
        self.tiles[0] = self.lis[:4]
        self.tiles[1] = self.lis[7:3:-1]
        self.tiles[2] = self.lis[8:12]
        self.tiles[3] = self.lis[15:7:-1]
        