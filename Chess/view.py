#!/usr/bin/python

# ---------------- READ ME ---------------------------------------------
# This Script is Created Only For Practise And Educational Purpose Only
# This Script Is Created For http://bitforestinfo.blogspot.com
# This Script is Written By
#
#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/

    Note: We Feel Proud To Be Indian
######################################################
'''
import Tkinter
from configurations import *
import managements as mg
from PIL import ImageTk, Image

def get_color(n):
    if n%2 == 0:
        return BOARD_COLOR_1
    else:
        return BOARD_COLOR_2

def get_image_handle(x1,y1,tag):
    get_link = mg.playing_warriors[tag]
    if get_link:
        f = Image.open(get_link)
        f=f.resize((64,64))
        StoreImg = ImageTk.PhotoImage(f)
        return (StoreImg, get_link)
    else:
        return 

class ChessView(Tkinter.Tk):
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        self.imgstore = []
        self.create_playground_canvas()
        self.create_squares_on_ground()
        self.ground.bind("<Button-1>",self.mouse_clicked_player)
    
    def player_available_ways(self, t,c):
        imgid = t[2]
        self.get_blank_box(mg.attacks_rule[imgid],c,t)
        return

    def get_blank_box(self, direction,c,t):
        ['A','B','C','D','E','F','G','H']
        range(0,8)
        print c
        if direction[0]==n:
            pass

        return

    def mouse_clicked_player(self, event):
        c, t = self.return_chess_box_coords()
        for i in self.ground.find_withtag("chessbox"):
            color = self.ground.gettags(i)[1]
            self.ground.itemconfig(i, fill=color)

        if t[0]=="image":
            obj = self.ground.find_withtag("{},{},{},{}".format(*c))
            self.ground.itemconfig("{},{},{},{}".format(*c), fill='blue')
            self.player_available_ways(t,c)
        return

    def return_chess_box_coords(self):
        store = self.ground.find_withtag(Tkinter.CURRENT)
        obj = self.ground.gettags(store)
        if "image" in obj:
            m,n = self.ground.coords(store)
            x1,y1,x2,y2 = m-32,n-32,m+32,n+32
            return ((x1,y1,x2,y2), obj)
        else:
            return ((self.ground.coords(store)), obj)

    def create_squares_on_ground(self):
        v=0
        for i,a in enumerate(['A','B','C','D','E','F','G','H']):
            v=v+1
            for n in range(0,8):
                color = get_color(v)
                v=v+1
                (x1,y1,x2,y2) = (n*64,i*64,n*64+64,i*64+64)
                self.ground.create_rectangle(x1,y1,x2,y2, fill=color, tags=("chessbox", color, "{}{}".format(a,n), "{}.0,{}.0,{}.0,{}.0".format(x1,y1,x2,y2)))
                img = get_image_handle(x1,y1,"{}{}".format(a,n))
                if img:
                    self.ground.create_image(x1+32,y1+32, image=img[0], tags=("image",img[1].split("/")[1].split(".")[0],"img-{}{}".format(a,n)))
        
                    self.imgstore.append(img)
        return



    def create_playground_canvas(self):
        self.ground = Tkinter.Canvas(self, bg="white", width=600, height=600)
        self.ground.pack()
        return



def main():
    ChessView(className = " Chess Game. By Bitforestinfo").mainloop()
    return


if __name__ == '__main__':
    main()