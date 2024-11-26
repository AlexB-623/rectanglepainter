import numpy as np
from PIL import Image

class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
        self.state = self.make()

    def make(self):
        base_canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        base_canvas[:] = self.color
        return base_canvas

    def add_rectangle(self, Rectangle):
        #add a rectangle on top of canvas
        working_canvas = self.state
        working_canvas[Rectangle.x_start:Rectangle.x_end, Rectangle.y_start:Rectangle.y_end] = Rectangle.color
        self.state = working_canvas


    def finish(self):
        #finalize the canvas
        img = Image.fromarray(self.state, 'RGB')
        img.save('filled_canvas.png')

# test = Canvas(600, 900, [0, 0, 0])
# test.make()


class Rectangle:
    def __init__(self, x_start, x_end, y_start, y_end, color):
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.color = color



# rect1 = Rectangle(200, 1000, 300, 700, color=[255, 255, 0])
# test.add_rectangle(rect1)
# test.finish()
