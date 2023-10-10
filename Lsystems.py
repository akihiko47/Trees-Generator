import turtle
from time import sleep


window = turtle.Screen()
font = ("Arial", 8, 'normal', 'bold', 'italic', 'underline')
pen = turtle.Turtle()
pen.pensize(2)
pen.speed('fastest')
pen.isvisible()
pen.pencolor('green')
pen.setposition(0, -300)
pen.setheading(90)

line = 'X'
position = []
dist = 5
end_gen = 6
trans = {'X': 'F-[[X]+X]+F[+FX]-X',
         'F': 'FF',
         '+': '+',
         '-': '-',
         '[': '[',
         ']': ']',
         }


def new_line(line):
    new = ''
    for ch in line:
        new += trans[ch]
    return new


def save_pos():
    global position
    position.append([pen.heading(), pen.position()[0], pen.position()[1]])


def load_pos():
    pen.penup()
    new_pos = position.pop(-1)
    pen.setposition(new_pos[1], new_pos[2])
    pen.down()
    pen.setheading(new_pos[0])


def make_action(line):
    for ch in line:
        if ch == '+':
            pen.right(25)
        elif ch == '-':
            pen.left(25)
        elif ch == 'F':
            pen.forward(dist)
        elif ch == '[':
            save_pos()
        elif ch == ']':
            load_pos()


generation = 0
while True:
    generation += 1
    print(f'Generation number {generation}')

    line = new_line(line)

    if generation == end_gen:
        make_action(line)
        sleep(100)
