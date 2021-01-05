from math import cos, sin, pi

class Draw2DShapes():
    def circle(canvas, c, r, **kwargs): #outColor, fillColor, width):
        # because tkinter doesn't have a half decent way to draw a circle
        x = c[0]
        y = c[1]
        return canvas.create_oval(x + r, y + r, x - r, y - r, **kwargs)

    def oval(canvas, c, w, h, **kwargs):
        x = c[0]
        y = c[1]
        return canvas.create_oval(x, y, x + w, y + h, **kwargs)

    def ovalByCenter(canvas, c, w, h, **kwargs):
        x = c[0] - 0.5*w
        y = c[1] - 0.5*h
        return canvas.create_oval(x, y, x+w, y+h, **kwargs)

    def triangle(canvas, c, w, h, **kwargs):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x,y,(x - 0.5*w),(y + h), (x + 0.5*w),(y + h), **kwargs)

    def square(canvas, c, s, **kwargs ):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x, y, x +s, y, x+s, y+s, x, y+s, **kwargs)

    def squareByCenter(canvas, c, s, **kwargs):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x-0.5*s, y-0.5*s, x +0.5*s, y-0.5*s, x+0.5*s, y+0.5*s, x-0.5*s, y+0.5*s, **kwargs)

    def rectangle(canvas, c, w, h, **kwargs ):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x, y, x +w, y, x+w, y+h, x, y+h, **kwargs)

    def rectangleByCenter(canvas, c, w, h, **kwargs):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x-0.5*w, y-0.5*h, x +0.5*w, y-0.5*h, x+0.5*w, y+0.5*h, x-0.5*w, y+0.5*h, **kwargs)

    def starByCenter(canvas, c, rad, **kwargs):
        x = c[0]
        y = c[1]
        return canvas.create_polygon(x+rad*cos(9*pi/10 - pi/2), y+rad*sin(9*pi/10 - pi/2), #162
                                     x+rad*cos(pi/10 - pi/2), y+rad*sin(pi/10 - pi/2),  #18
                                     x+rad*cos(13*pi/10 - pi/2), y+rad*sin(13*pi/10 - pi/2), #234
                                     x+rad*cos(pi/2 - pi/2), y+rad*sin(pi/2 - pi/2),#90
                                     x+rad*cos(17*pi/10 - pi/2), y+rad*sin(17*pi/10 - pi/2), **kwargs) #306

    def nSidedPolygonPts(canvas, x, y, r, n, buf=0):
        # calculate and return points for a n sided figure that will encompass a circle at x,y with radius r with buffer
        # set buf == 0 to draw exactly on the circle
        rad = r + buf
        pts = []
        for i in range(0, n):
            t = 2 * pi * i / n
            x1 = (int)(x + rad * cos(t))
            y1 = (int)(y + rad * sin(t))
            pts.append([x1, y1])
        return pts

