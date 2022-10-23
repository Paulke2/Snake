from designer import *
from random import randint
import random
World = {
    "snake": DesignerObject,
    "snake speed":int,
    "snake up speed":int,
    "food":DesignerObject,
    'score':int,
    'snake segments':[DesignerObject],
    'time':int,
    "message": DesignerObject,
    'seconds':int,
    'score':int
}

def create_the_world() -> World:
    '''
    This function creates all the objects in the world and returns a dictionary
    containing all of the objects in the World dictionary definition.
    '''
    return { 
    "snake": rectangle('green',30,30),
    "snake speed":SNAKE_SPEED,
    "snake up speed":SNAKE_UP_SPEED,
    "food" : rectangle("red", 15, 15,randint(0,get_width()),randint(0,get_height())),
    'score' : 0,
    'snake segments':[],
    "message": text("black", "time:  "+'score:'),
    'time':0,
    'seconds':0
    }
############moving alog x axis############
SNAKE_SPEED = 0
SNAKE_UP_SPEED = 0
def move_snake(world:World):
    '''
    consumes the world dictionary type and changes the values stored in
    some of the world definitions.
    first, it takes the world variable 'time', and if modula 5 of time is 0,
    the world designer object 'snake' x and y position move.
    '''
    if world['time']%5==0:
        world['snake']['x'] += world['snake speed']
        world['snake']['y'] += world['snake up speed']
def move_left(world: World):
    '''
    consumes a dictionary type World and returns a changed version of that world
    
    first, the variable 'snake speed', which is the direction the 'snake'
    moves on the x axis, has a constant subracted the x position(35). Also the
    x axis of the snake is fliped to change the direction when the function is
    called. This function also sets the 'snake up speed' to 0 to stop it from
    moving on the y-axis.
    '''
    world['snake speed'] = -SNAKE_SPEED -35
    world['snake']['flip_x'] = True
    world['snake up speed'] = 0
def move_right(world: World):
    '''
    consumes a dictionary type World and returns a changed version of that world
    
    first, the variable 'snake speed', which is the direction the 'snake'
    moves on the x axis, has a constant added to the x position(35). Also the
    x axis of the snake is fliped to change the direction when the function is
    called. This function also sets the 'snake up speed' to 0 to stop it from
    moving on the y-axis.
    '''
    world['snake speed'] = SNAKE_SPEED +35
    world['snake']['flip_x'] = False
    world['snake up speed'] = 0
def move_x_axis(world: World, key: str):
    '''
    consumes a world(World dictionary type) aswell as a key(str). if the
    user inputs 'left' on their keyboard, the move_left function is called.
    if the user inputs 'right' on their keyboard, the move_right function is
    called and changes the snakes position in the world
    
    '''
    if key == 'left':
        move_left(world)
        
    elif key == 'right':
        move_right(world)
        
when('typing', move_x_axis)
####################moving y axis#########

    
def move_up(world: World):
    '''
    consumes a dictionary type World and returns a changed version of that world
    
    first, the variable 'snake up speed', which is the direction the 'snake'
    moves on the y axis, has a constant subracted the y position(35). Also the
    y axis of the snake is fliped to change the direction when the function is
    called. This function also sets the 'snake up speed' to 0 to stop it from
    moving on the x axis.
    '''
    world['snake up speed'] = -SNAKE_UP_SPEED -35
    world['snake']['flip_y'] = True
    world['snake speed'] = 0
def move_down(world: World):
    '''
    consumes a dictionary type World and returns a changed version of that world
    
    first, the variable 'snake up speed', which is the direction the 'snake'
    moves on the y axis, has a constant added the y position(35). Also the
    y axis of the snake is fliped to change the direction when the function is
    called. This function also sets the 'snake up speed' to 0 to stop it from
    moving on the x axis.
    '''
    world['snake up speed'] = SNAKE_UP_SPEED +35
    world['snake']['flip_y'] = False
    world['snake speed'] = 0
def move_y_axis(world: World, key: str):
    '''
    consumes a world(World dictionary type) aswell as a key(str). if the
    user inputs 'up' on their keyboard, the move_up function is called.
    if the user inputs 'down' on their keyboard, the move_down function is
    called and changes the snakes position in the world
    
    '''
    if key == 'up':
     
        move_up(world)
    elif key == 'down':
        
        move_down(world)

when('typing', move_y_axis)
when("starting", create_the_world)
when('updating', move_snake)


#####################Phase 2############

def teleport_food(world):
    '''
    consumes a world. when the function is called, the designer object 'food'
    has its x and y position randomized by the randint function.
    '''
    world['food']['x'] = random.randint(0, get_width())
    world['food']['y'] = random.randint(0, get_height())
def where_food(world:World):
    '''
    consumes a dictionary of the type World. then it finds the x value
    of the desinger object 'food' and if it is out of bounds of the designer game
    window, the designer object 'food' is teleported somewhere else. Same thing
    happens with the y axis. If the object 'food' y axis is out of bounds, the
    object 'food' is told to teleport.
    '''
    if world['food']['x'] >= get_width() -5 or world['food']['x'] <= 5:
        world['food']['x'] = random.randint(0, get_width())
        world['food']['y'] = random.randint(0, get_height())
    elif world['food']['y'] >= get_height() -5 or world['food']['y'] <= 5:
        world['food']['x'] = random.randint(0, get_width())
        world['food']['y'] = random.randint(0, get_height())
    
    
def eating_food(world:World):
    '''
    Consumes a world dictionary type, then, if the designer object 'snake' is colliding with the other
    designer object 'food', the 'food' object has its x and y position changed to a random spotk inside
    the window of the designer class. Also, when the of statment is true, the world 'score' variable
    has 10 added to it to track the users score.
    '''
    if colliding(world['snake'], world['food']):
        world['food']['x'] = random.randint(0, get_width())
        world['food']['y'] = random.randint(0, get_height())
        world['score'] = world['score'] +10

def create_snake_segment() -> DesignerObject:
    '''
    consumes nothing but returns a designer object which is the same size as the designer object
    'snake'. snake_body is the designer object that will be returned and is first declared as
    invisible to ensure that the snake does not colide with the snake_body when it is first spawned in.
    '''
    snake_body = rectangle('green',30,30)
    snake_body['visible'] = False
    return snake_body

    
def add_segment(world:World):
    '''
    Consumes a World dictonary type. first, if the designer object 'snake' is coliding with
    the object 'food' new_segmnt is created by setting i equal to the create_snake_segment
    function whch makes new_segmet a designer object. This new object is then appended to a list in
    the world definition. A new object is created each time 'snake' and 'food' collide.
    '''
    if colliding(world['snake'], world['food']):
        new_segment = create_snake_segment()
        ###############################################################
        #follow_snake(new_segment, world['snake'])
        world['snake segments'].append(new_segment)
        
def body_snake(world:World):
    '''
    first, a World is consumed, then the local variabes head, bodies, old_x, and old_y are created
    head is equal to the desiner object 'snake'. bodies is set equal to the world dictionary
    'snake segments' which is a list of designer objects. old_x is set to the 'snake' x position.
    old_y is set to the 'snake' y position. then, if the int 'time' is divided by 5 and the remainder is
    0, for each object in bodies, a new tem_x and temp_y are set to the new 'snake' x and y pos
    and each body in the bodies list are iterated over and gived the old vaulues of the segment infront
    of it. Finaly, each segment, once moved is made visible.
    '''
    head = world['snake']
    bodies = world['snake segments']
    old_x = head['x'] 
    old_y = head['y']
    
    if world['time']%5 ==0:
        for body in bodies:
            temp_x = body['x']
            body['x'] = old_x 
            old_x = temp_x 
            ####y_axis##################
            temp_y = body['y']
            body['y'] = old_y 
            old_y = temp_y
            
            body['visible'] = True

            
def timer(world:World):
    '''
    consumes a World dictionary type. the local variables time and seconds are created. time is
    set to the world value of 'time' and seconds is set to the world value of 'seconds'. if the
    time is equal or greater than 0, 1 is added to the world value of 'time'. this will always add
    1 to 'time' since it will always be greater than 1.
    then, because the designer class has a fps cap at 30, when it updates 30 times, that will be
    a second so if time is equal to 30, 1 will be added to the world value of 'seconds' and 'time'
    will be set equal to 0 to reset the timer. Also, in the if statment that calculates seconds
    aswell as time have a message shown on screen to show the current score as well as the string
    values of time and seconds using the str() function.
    '''
    time = world['time']
    seconds = world['seconds']
    
    if time >= 0:
        world['time'] += 1
        world['message']['text'] = "time: " + str(seconds)+':'+str(world['time']) +'  score:'+ str(world['score'])  
    if time ==30:
        world['time'] = 0
        world['seconds'] += 1
        world['message']['text'] = "time: " + str(seconds)+':'+str(world['time']) +'  score:'+ str(world['score'])
    
def body_colide(world:World):
    '''
    consumes a World dictionary type and the world list is iterated through and if the segment, which
    represents a value in teh 'snake segments' list is not the fist value in the list, and
    the segent is visible, and finaly, if the world object 'snake' is collding with any of the segments,
    the end_game function is called which pauses the game and gives a final message. the
    'if segment != world['snake segments'][0]:' makes the first segment a dummy segment so it will
    not end the game when it is fist created. then, if the segment i colliding with the designer object
    'food' it will be teleported to a random place within the window.
    '''
    for segment in world['snake segments']:
        if segment != world['snake segments'][0]:
        
            if segment['visible'] == True:
                if colliding(world['snake'], segment):
                    end_screen(world)
        if colliding(segment, world['food']):
            world['food']['x'] = random.randint(0, get_width())
            world['food']['y'] = random.randint(0, get_height())
def wall_colide(world:World):
    '''
    first, a world dictionary is consumed. then if the desinger object 'snake' x position is
    less than or equal to the max window height -10 or its x position is less than or equal to 10,
     the end_screen function is called which gives a final message and pauses the game. same thing
     happens with the 'snake' y position. if it is greater than window height -10 or less or equal
     to 10 the end_screen function is created. 10 is added or subrated to max height or 0 because
     the 'snake' object is 30 pixles wide and long and it would only collide with the border when the
     snake object is past the border so this constant 10 makes it so as soon as the snake object
     touches the border, the game is paused.
    '''
    if world['snake']['x'] >= get_width() -10 or world['snake']['x'] <= 10:
        end_screen(world)
    elif world['snake']['y'] >= get_height() -10 or world['snake']['y'] <= 10:
        end_screen(world)
        
def end_screen(world:World):
    '''
    First a World dictionary type is consumed and the world message is changed to say game over and
    give the uer their final score and the time it took them to end he game with getting the string
    valeus of 'seconds' and 'score' with the str() function. After the message is given, the game is
    paused with the pause() function
    '''
    world['message']['text'] = 'Game over! Final score: '+str(world['score'])+' with a time of '+str(world['seconds'])
    pause()
#########we need to make a timer and have it crate the segment aftera few updates#######

when('updating',timer) 
when('updating', add_segment)
when('updating',eating_food)
when('updating',where_food)
when('updating',body_snake)
when('updating',body_colide)
when('updating',wall_colide)

start()










