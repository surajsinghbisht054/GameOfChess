# Putting a gif image on a canvas with Tkinter
# tested with Python24 by  vegaseat  25jun2005
from Tkinter import *
root=Tk()
# create the canvas, size in pixels
canvas = Canvas(root,width = 300, height = 200, bg = 'yellow')
# pack the canvas into a frame/form
canvas.pack(expand = YES, fill = BOTH)
# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
gif1 = PhotoImage(file = 'Icons/elephant_D.gif')
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(0, 0, image = gif1)
# run it ...
root.mainloop()
