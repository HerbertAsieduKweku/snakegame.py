import turtle
import random
tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.bgcolor('black')
turtle.colormode(255)
tim.speed('fastest')
def random_color():
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    random_color = (r,g,b)
    return random_color
def draw_spirograph(size_of_graph):
    for i in range(int(360/size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.heading()
        tim.setheading(tim.heading()+ 10)
draw_spirograph(2)
my_screen.exitonclick()
def fibonacci(num_of_series):
    a = 0
    for i in range(num_of_series):
        b = a + i
        print(b)
        a = b
fibonacci(30)
