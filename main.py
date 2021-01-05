from viewer import Viewer
import time


def main():
    v = Viewer()
    while True: #this while loop replaces v.mainloop()
        v.update()
        v.run()
        time.sleep(0.5)


if __name__ == '__main__':
    main()



