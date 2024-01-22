# Escaping the maze (Final Exercise for Day 6)

def vertjump():
    while True:
        if right_is_clear()== False:
            move()
        else:
            turn_right()
            move()
            vertdown()
            break

def vertdown():
    turn_right()
    move()
    while True:
        if wall_in_front() == True:
            turn_left()
            break
        else:
            move()
    
def jump():
    turn_left()
    move()
    vertjump()

def turn_right():
    for i in range (0,3,1):
        turn_left()

def main():
    while True:
        if at_goal() == True:
            break
        if wall_on_right() == False:
            turn_right()
            move()
        elif front_is_clear() == True:
           move()
        else:
            if wall_on_right() == False:
                turn_right()
                move()
            else:
                turn_left()
                main()
main()