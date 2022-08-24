import colorgram
import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
screen = turtle_module.Screen()
screen.setworldcoordinates(-50,-50,500,500)
tim.up()
tim.speed('fastest')
tim.hideturtle()

hurst_colors = colorgram.extract('image.jpg', 30)

def get_rgb(cg_colors):
    colors = []

    for color in cg_colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors.append(color_tuple)

    return colors
 
def draw_row(row_len):
    for i in range(row_len):
        tim.dot(20, random.choice(get_rgb(hurst_colors)))
        if i < row_len - 1: 
            tim.forward(50)

for c in range(10):
    if c == 0:
        draw_row(10)
    else:
        if tim.xcor() > 0:
            tim.left(90)
            tim.forward(50)
            tim.left(90)    
            draw_row(10)
        else:
            tim.right(90)
            tim.forward(50)
            tim.right(90)
            draw_row(10)

screen.exitonclick()
