def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
def pathfind():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
            
while not at_goal():
    pathfind() 
