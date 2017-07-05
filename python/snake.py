# SNEK GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

def game():
    
    key = KEY_RIGHT                                                    # Initializing values
    score = 0

    snake = [[4,10], [4,8], [4,6]]                                     # Initial snake co-ordinates
    food = [10, 20]                                                     # First food co-ordinates
    foods = [food] 
    win.addstr(food[0], food[1], 'O', curses.color_pair(2))                                   # Prints the food
    
    while key != 27:                                                   # While Esc key is not pressed
        win.border(0)
        win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
        win.addstr(0, 27, ' SNEK ')                                   # 'SNAKE' strings
        win.timeout(150 - len(snake) % 120)
        
        prevKey = key                                                  # Previous key pressed
        event = win.getch()
        key = key if event == -1 else event 
    
    
        if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
            key = -1                                                   # one (Pause/Resume)
            while key != ord(' '):
                key = win.getch()
            key = prevKey
            continue
    
        if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
            key = prevKey
        # can't go backwards
        if key == KEY_LEFT and prevKey == KEY_RIGHT:
            key = prevKey
        if key == KEY_RIGHT and prevKey == KEY_LEFT:
            key = prevKey
        if key == KEY_UP and prevKey == KEY_DOWN:
            key = prevKey
        if key == KEY_DOWN and prevKey == KEY_UP:
            key = prevKey

        # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
        # This is taken care of later at [1].
        snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -2) + (key == KEY_RIGHT and 2)])
    
        # Exit if snake crosses the boundaries
        if snake[0][0] == 0 or snake[0][0] == height-1 or snake[0][1] == 0 or snake[0][1] == width-1: break
    
        # If snake runs over itself
        if snake[0] in snake[1:]: break
    
        
        if snake[0] == food:                                            # When snake eats the food
            food = []
            score += 1
            r = randint(0, (height - 2) * (width // 2 - 2) - len(snake))
            c = 0
            fr = 1
            fc = 2
            while c < r:
                if fr < height - 2:
                    fr += 1
                else:
                    fr = 1
                    fc += 2
                if [fr, fc] not in snake:
                    c += 1
            food = [fr, fc]
            foods.append(food)
            win.addstr(food[0], food[1], 'O', curses.color_pair(2))
        else:    
            last = snake.pop()                                          # [1] If it does not eat the food, length decreases
            win.addch(last[0], last[1], ' ')
        win.addstr(snake[0][0], snake[0][1], '#', curses.color_pair(1))

    win.timeout(-1)
    win.addstr(1, 1, "GAME OVER", curses.color_pair(2))
    c = win.getch()
    while c != ord('\n'):
        c = win.getch()
    win.clear()
    win.addstr(0, 0, "Score: " + str(score))
    curses.echo()
    win.addstr(2, 0, "Name: ")
    name = win.getstr(2, 6, 10)
    name = name.decode("utf-8")
    win.addstr(4, 0, name + " " + str(score))
    win.getch()

    #return to normal
    curses.nocbreak()
    win.keypad(False)
    curses.echo()
    curses.endwin()

# start screen
curses.initscr()
# screen sizes 
height = curses.LINES // 2
width = curses.COLS // 3
if width % 2 == 0:
    width += 1
start_row = curses.LINES // 2 - height // 2
start_col = curses.COLS // 2 -  width // 2
# colors
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
# window
win = curses.newwin(height, width, start_row, start_col)
win.keypad(True)
curses.noecho()
curses.curs_set(0)
curses.cbreak()

game()
end()
