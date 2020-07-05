import turtle

# Square
qazi_turtle = turtle.Turtle()
qazi_turtle._rotate(45)
qazi_turtle.speed(10)


def square():
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)
    qazi_turtle.right(90)
    qazi_turtle.forward(100)


# square()
# qazi_turtle.forward(200)

# elephant_weight = 3000
# ant_weight = 0.1

# if True:  # elephant_weight > ant_weight
   # square()
# else:
   # qazi_turtle.forward(300)

# qazi = 'happy'
# while True:  # qazi == 'happy'
   # qazi_turtle.forward(10)

# for i in range(5):
   # print(i)

for count in range(4):
    square()
