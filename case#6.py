from ru_local import *
import math
import turtle

def get_num_hexagons():
    '''Input validation for number hexagons'''
    while True:
        n = input(NUMBER_INPUT)
        if not n.isdigit():
            print(REWRITE_NUMBER)
        elif int(n) < 4 or int(n) > 20:
            print(REWRITE_NUMBER)
        else:
            break
    return int(n)

def get_color_choice():
    '''Input validation for selected color'''
    color = input(COLOR_INPUT)
    color_list = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]
    if color.lower() == RED:
        color = 'red'
    elif color.lower() == BLUE:
        color = 'blue'
    elif color.lower() == GREEN:
        color = 'green'
    elif color.lower() == YELLOW:
        color = 'yellow'
    elif color.lower() == ORANGE:
        color = 'orange'
    elif color.lower() == PURPLE:
        color = 'purple'
    elif color.lower() == PINK:
        color = 'pink'
    else:
        while True:
            color = input("'" + color + "'" + REWRITE_COLOR).lower()
            if color in color_list:
                break

    return color

def draw_hexagon(x, y, side_len, color):
    '''Drawing hexagon'''
    turtle.begin_fill()
    for _ in range(6):
        turtle.forward(side_len)
        turtle.right(60)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.end_fill()

def alternation_colors(count, color_1, color_2):
    '''Selection of color of each hexagon'''
    if count % 2 == 0:
        color = color_1
    else:
        color = color_2
    return color


def tesellation(number, color_1, color_2):
    '''Tiling'''
    y = 250
    x = -250
    diag = int(500/number)
    side_len = diag/math.sqrt(3)
    count = 1
    i = 1
    turtle.left(30)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for _ in range(number):
        if i%2 == 1:
            for _ in range(number):
                x += diag
                count += 1
                color = alternation_colors(count, color_1, color_2)
                draw_hexagon(x, y, side_len, color)
            i += 1
            y -= side_len * 1.5
            x -= diag/2
            turtle.up()
            turtle.goto(x, y)
            turtle.down()
        else:
            for _ in range(number):
                x -= diag
                count += 1
                color = alternation_colors(count, color_1, color_2)
                draw_hexagon(x, y, side_len, color)
            count += 1
            i += 1
            y -=side_len * 1.5
            x += diag/2
            turtle.up()
            turtle.goto(x, y)
            turtle.down()


def main():
    print(COLOR_LIST)
    for i in [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, PINK]:
        print('', i)
    color_1 = get_color_choice()
    color_2 = get_color_choice()
    num = get_num_hexagons()
    turtle.setup = 500, 500
    tesellation(num, color_1, color_2)
    turtle.done()

if __name__ == '__main__':
    main()
