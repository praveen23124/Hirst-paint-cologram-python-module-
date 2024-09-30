import turtle as t
tommy = t.Turtle()
t.colormode(255)
import random
# import colorgram
# # Extract 6 colors from the image
# colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
# # Print the RGB values of the extracted colors
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
color_list = [(198, 13, 32),(248, 236, 25),(40, 76, 188),(39, 216, 69),(238, 227, 5),(227, 159, 49),(29, 40, 154),(212, 76, 15),(17, 153, 17),(241, 36, 161),(195, 16, 12),(223, 21, 120),(68, 10, 31),(61, 15, 8),(11, 97, 62)]
print(tommy.xcor(),tommy.ycor())
tommy.penup()
tommy.setheading(225)
tommy.forward(250)
tommy.setheading(0)
tommy.speed(1000)
def hirst_paint(x,y):
    print(x,y)
    x_car = x
    y_car = y
    rows = 10
    columns = 10
    for _ in range(rows):
        for _  in range(columns):
         tommy.color(random.choice(color_list))
         tommy.goto(y_car,x_car)
         tommy.dot(20)
         tommy.penup()
         y_car=y_car+50
        x_car = x_car + 50
        y_car = y

print(tommy.xcor(),tommy.ycor())
hirst_paint(tommy.ycor(),tommy.ycor())


screen = t.Screen()
screen.exitonclick()
