from configurations import *
import controller, model
try:
        import Tkinter
except:
        import tkinter as Tkinter

class PlayerPosition:
        def  __init__(self, MainBox=None):
                mapping=MainBox.map
                canvas=MainBox.canvas
                st=Tkinter.PhotoImage(file='Icons/elephant_D.gif')
                p,q,r,s,t=(0,0,0,0,0)#mapping['A1']
                print p,q,r,s,t
                MainBox.canvas.create_image(80,90, image=st)
                canvas.create_rectangle(0,0,64,64,fill='yellow')
                
class Model(Tkinter.Tk):
        def __init__(self):
                Tkinter.Tk.__init__(self, className='Suraj')
                # Design Map of Base
                self.map={}
                # Creating Base
                self.create_chess_base()

                


        # Function For Creating Chess Base
        def create_chess_base(self):
                self.create_menu()
                self.create_canvas()
                #self.draw_board()
                #self.touch_detector()
                PlayerPosition(MainBox=self)

        # Mouse Touch Detector
        def touch_detector(self):
                self.canvas.bind("<Button-1>", self.on_square_clicked)
        # Mouse Touch Coordinates Finder
        def on_square_clicked(self,event):
                #print 'Row : {}, Column : {}'.format(event.y/DIMENSION_OF_EACH_SQUARE+1,event.x/DIMENSION_OF_EACH_SQUARE+1)
                y=event.y/DIMENSION_OF_EACH_SQUARE+1
                y=y*64
                x=event.x/DIMENSION_OF_EACH_SQUARE+1
                x=x*64
                #print y,x
                for i in self.area:
                        a,b,c,d=i
                        if y==d and x==c:
                                return {'square':(event.y/DIMENSION_OF_EACH_SQUARE+1,event.x/DIMENSION_OF_EACH_SQUARE+1),'area':i}
        # Function For Drawing Base Color and Square        
        def draw_board(self):
                self.area=[]
                x1=0
                y1=0
                x2=DIMENSION_OF_EACH_SQUARE
                y2=DIMENSION_OF_EACH_SQUARE
                color=self.color_changer(color=None)
                # Mapping Machanizim
                map_of_row={
                        0:'A',
                        1:'B',
                        2:'C',
                        3:'D',
                        4:'E',
                        5:'F',
                        6:'G',
                        7:'H',
                        8:'I',
                        9:'J'}
                map_of_column=range(1,10)
                for i in range(NUMBER_OF_ROWS):
                        self.canvas.create_rectangle(x1,y1,x2,y2,fill=color)
                        X1=0
                        Y1=y1
                        X2=DIMENSION_OF_EACH_SQUARE
                        Y2=y2
                        for s in range(NUMBER_OF_COLUMNS):
                                self.canvas.create_rectangle(X1,Y1,X2,Y2,fill=color)
                                self.area.append((X1,Y1,X2,Y2))
                                self.map[str(map_of_row[i])+str(map_of_column[s])]=(X1,Y1,X2,Y2, color)
                                X1=X1+DIMENSION_OF_EACH_SQUARE
                                X2=X2+DIMENSION_OF_EACH_SQUARE
                                color=self.color_changer(color=color)
                        y1=y1+DIMENSION_OF_EACH_SQUARE
                        y2=y2+DIMENSION_OF_EACH_SQUARE
                        color=self.color_changer(color=color)
                #print self.map
        # Function for creating Canvas
        def create_canvas(self):
                canvas_width = NUMBER_OF_COLUMNS *DIMENSION_OF_EACH_SQUARE
                canvas_height = NUMBER_OF_ROWS * DIMENSION_OF_EACH_SQUARE
                self.canvas = Tkinter.Canvas(self, width=canvas_width, height=canvas_height)
                self.canvas.pack(padx=10,pady=10)
        def color_changer(self, color=None):
                if color==BOARD_COLOR_1:
                        return BOARD_COLOR_2
                else:
                        return BOARD_COLOR_1
        def create_menu(self):
                # Main Menu Bar
                storeobj=Tkinter.Menu(self)

                # [Menu] Window Bar
                menu_bar=Tkinter.Menu(self, tearoff=0)
                menu_bar.add_command(label='New')
                menu_bar.add_separator()
                menu_bar.add_command(label='Exit', command=lambda:self.destroy())
                menu_bar1=Tkinter.Menu(self, tearoff=0)
                menu_bar1.add_command(label='System')
                menu_bar1.add_separator()
                menu_bar1.add_command(label='Color')
                menu_bar2=Tkinter.Menu(self, tearoff=0)
                menu_bar2.add_command(label='Help')
                menu_bar2.add_separator()
                menu_bar2.add_command(label='About')

                # [Main Label Bar]
                storeobj.add_cascade(label='Menu', menu=menu_bar)
                storeobj.add_cascade(label='Edit', menu=menu_bar1)
                storeobj.add_cascade(label='About', menu=menu_bar2)

                
                self.config(menu=storeobj)

if __name__=='__main__':
        Model().mainloop()


class View():
	def __init__(self):
		pass


