from viewer import Viewer
import time

if __name__ == '__main__':
    v = Viewer()
    while True: #this while loop replaces v.mainloop()
        v.update()
        v.run()
        time.sleep(0.5)

    sys.exit(_main(sys.argv[1:]))


