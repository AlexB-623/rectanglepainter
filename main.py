from classes import Canvas, Rectangle

def int_validator(type, max):
    """
    :parameter type is the type of integer being validated
    :parameter max is the max value for the integer
    you pass that to the function and we ask the user the value for that

    """
    while True:
        user_input = input(f"Enter a value for {type} (max={max}): ")
        if type == "the number of shapes to make":
            grammar = "many shapes"
        else:
            grammar = "large"
        try:
            user_input = int(user_input)
            if user_input < 0:
                user_input *= -1
                print(f"You probably meant {user_input}. I removed the negative..")
            if user_input > max:
                print(f"Too {grammar}, please keep it under {max}")
                continue
            return user_input
        except ValueError:
            print("Please enter a whole number")


def color_picker():
    """feeds rgb color to the int_validator function, returns a list with red, green, blue"""
    print("You will be asked to provide Red/Green/Blue colors. Please see: https://rgbcolorpicker.com/ for inspiration")
    red = int_validator("red", 255)
    green = int_validator("green", 255)
    blue = int_validator("blue", 255)
    return [red, green, blue]


def how_many_shapes():
    """
    determine the number of shapes to make
    """
    num_shapes = int_validator("the number of shapes to make", 10)
    print(f"Okay, we'll make {num_shapes} shapes.")
    return num_shapes


def make_shapes(num_shapes):
    """
    loop through the num of shapes and ask the user about each shape
    :param num_shapes: number of shapes returned from how_many_shapes()
    :return:
    """
    loop_count = 0
    while num_shapes > 0:
        if loop_count == 0:
            print("First, we'll set up the canvas (the background). I recommend 600x900:")
            canvas_height = int_validator("Height", 600)
            canvas_width = int_validator("Width", 900)
            canvas_color = color_picker()
            canvas = Canvas(canvas_height, canvas_width, canvas_color)

            loop_count += 1
            continue
        print(f"Shape #{loop_count}:")
        #starting position for the height
        rect_start_height = int_validator(f"rectangle {loop_count}'s starting height (distance from top)",
                                          canvas.height)
        rect_total_height = int_validator(f"rectangle {loop_count}'s total height (min=1)",
                                          canvas.height)
        # to prevent invalid shapes, we will programmatically
        # set the end positions by asking the overall height and doing the math
        rect_end_height = rect_start_height + rect_total_height
        # starting position for the width
        rect_start_width = int_validator(f"rectangle {loop_count}'s starting width (distance from left)",
                                         canvas.width)
        rect_total_width = int_validator(f"rectangle {loop_count}'s total width (min=1)",
                                         canvas.width)
        # to prevent invalid shapes, we will programmatically
        # set the end positions by asking the overall width and doing the math
        rect_end_width = rect_start_width + rect_total_width
        # ask user for color
        rect_color = color_picker()
        # instantiate the rectangle
        rect_instance = Rectangle(rect_start_height, rect_end_height, rect_start_width, rect_end_width, rect_color)
        #add rectangle to canvas
        canvas.add_rectangle(rect_instance)
        #control the loop
        loop_count += 1
        num_shapes -= 1
        #check to see if we've done all the shapes and if yes, finish
        if num_shapes == 0:
            canvas.finish()

#call functions to execute
num_shapes = how_many_shapes()
make_shapes(num_shapes)
