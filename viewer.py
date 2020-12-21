from tkinter import *
from draw2Dpolygons import Draw2DShapes
from colorList import *
# viewer.py constants
window_width = 900
window_height = 800
sidebar_width = 200
canvas_width = window_width - sidebar_width
canvas_height = window_height

root = Tk()

leftFrame = Frame(root, width=canvas_width, height=window_height)
rightFrame = Frame(root, width=sidebar_width, height=window_height)
w = Canvas(leftFrame,
           width=canvas_width,
           height=canvas_height,
           bg="white",
           relief=RIDGE)  # modified by several functions


class Viewer(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master.title("Tkinter Shape Example")
        self.pack(fill=BOTH, expand=1)

        leftFrame.pack(side=LEFT, expand=True, fill=BOTH)
        w.pack(side=LEFT, fill=BOTH, expand=True)

        self.draw(w)
        print("Starting Window")
        self.draw(w)

    def run(self):
        self.draw(w)

    def draw(self, w):
        self.fb = [0,0, 50,50, 40,80, 0,0]  #create_polygon = (x0,y0,x1,y1,...options))
        self.ob = [70,70]
        w.create_polygon(self.fb, outline=colorList.red, fill="", width=1)
        Draw2DShapes.circle(w, [self.ob[0], self.ob[1]], 10, outline=colorList.agua, width=2)

        Draw2DShapes.rectangleByCenter(w, [100,100], 25, 40, outline=colorList.orange, fill="", width=2)
        Draw2DShapes.circle(w, [500, 500], 4, outline=colorList.green4, width=2)
        Draw2DShapes.square(w, [200,200], 20,outline=colorList.orchid, fill="", width=1)
