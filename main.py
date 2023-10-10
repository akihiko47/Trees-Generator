import turtle
from random import randint


"""basic settings"""
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.pencolor('black')
pen.hideturtle()
position = []
size = []

"""moving to start position"""
pen.penup()
pen.setposition(0, -300)
pen.setheading(90)
pen.pendown()

"""SETTINGS"""
end_gen = 11
angle = 15
rand_angle_max = 13
thick = 16
dist = 10
pen.pensize(thick)

"""commands"""
start = '2222220'
trans = {'0': '1[20]20',
         '1': '21',
         '[': '[',
         ']': ']',
         '2': '2'
         }


def make_line():
    line = start
    for _ in range(end_gen):
        new = ''
        for ch in line:
            new += trans[ch]
        line = new
    return line


def save_pos():
    global position
    position.append([pen.heading(), pen.position()[0], pen.position()[1]])


def load_pos():
    pen.penup()
    new_pos = position.pop()
    pen.setheading(new_pos[0])
    pen.setposition(new_pos[1], new_pos[2])
    pen.pendown()


def make_leaf():
    size.append(pen.pensize())
    pen.pensize(4)
    r = randint(0, 9)
    if r == 0 or r == 1:
        pen.pencolor('#f2c318')
    elif r == 2 or r == 3:
        pen.pencolor('#e0b102')
    elif r == 4 or r == 5:
        pen.pencolor('#e09d02')
    elif r == 6 or r == 7:
        pen.pencolor('#e08f02')
    elif r == 8 or r == 9:
        pen.pencolor('#e07802')
    pen.forward(dist - 2)
    pen.pensize(size.pop())
    pen.pencolor('black')


def make_action(line):
    global thick
    for ch in line:
        if ch == '0':
            make_leaf()
        elif ch == '1':
            pen.forward(dist)
        elif ch == '2':
            if randint(0, 10) > 4:
                pen.forward(dist)
        elif ch == '[':
            thick = thick * 0.75
            pen.pensize(thick)
            size.append(thick)
            save_pos()
            pen.left(angle - randint(-rand_angle_max, rand_angle_max))
        elif ch == ']':
            load_pos()
            thick = size.pop()
            pen.pensize(thick)
            pen.right(angle - randint(-rand_angle_max, rand_angle_max))


def main():
    make_action(make_line())
    window.mainloop()


if __name__ == '__main__':
    main()
