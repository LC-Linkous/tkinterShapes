from viewer import Viewer
#from threading import Thread
from multiprocessing import Process
#from tkinter import *
#root = Tk()
import time

if __name__ == '__main__':
    v = Viewer()
    #v.mainloop()
    while True: #this while loop replaces v.mainloop()
        v.update()
        v.run()
        time.sleep(0.5)

    sys.exit(_main(sys.argv[1:]))


