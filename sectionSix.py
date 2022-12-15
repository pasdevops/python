# FUNCTION AND KAREL

#def my_function():
  #print("Hello")
  #print("How are you today")
  #print("It will be nice to see you again")
  
  #my_function()

#def turn_around():
    #turn_left()
    #turn_left()

#def turn_right(): # my own function 
   #turn_left()
   #turn_left()
   #turn_left()
    
    
#move()
#move()
#move()
#turn_around()
#move()
#move()
#move()
#turn_around()

# Defining and Calling Python Functions

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
#Draw square    
turn_left()
move()
turn_right()
move()
turn_right
move()
turn_right()
move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # To indent a block of code CTLR []
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# jump x 6 is another method
#jump()
#jump()
#jump()
#jump()
#jump()
#jump()

# For loop and range function can be used for the code

for step in range(6):
    jump()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # To indent a block of code CTLR []
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# while loop can be used for the code
# While syntax = while
# Condition set = number_of_hurdles > 0:


number_of_hurdles = 6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)


# HURDLE CHALLENGE 2



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # To indent a block of code CTLR []
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()
    
# When to use FOR LOOP,WHILE LOOP AND INFINITE LOOP

# FOR LOOP
# Use for loop when you want to iterate over things such as LISTS

# Also do something with each thing that you are iterating over.

# Use a for-loop when you deal with an array or a list 
# or in other words when the number of repeats is know.

# for loop is used when you already know the 
# number of times you want to loop through something.

# FOR LOOP EXAMPLE
fruits = ["Apple","Pear","Orange"]
for fruit in fruits:
    print(fruit)
    
for n in range(1, 6):
    print(n)

# WHILE LOOP
# A while loop is used when you want an 
# action to repeat itself until a certain 
# condition is met.



# INFINITE LOOP

# infinite loop will run indefinitely, 
# until it is explicitly broken out of using 
# either a break, exit or raise statement.

while 5 > 3:
    print(5 > 3)
    jump()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # To indent a block of code CTLR []
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump(): # To indent a block of code CTLR []
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()


Maze Game
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()











