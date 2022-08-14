def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_lef(): 
    turn_right()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()