import turtle
import random


def draw_square(turtle_name):
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
  
    for i in range(1,360):
        turtle_name.color("red")
        turtle_name.left(33)
        random.shuffle(colors)
        turtle_name.color(colors[0])
        
        for i in range(1,5):
            turtle_name.forward(100)
            turtle_name.right(90)
    


def draw_triangle(turtle_name):
    colors = ["blue","black","brown","red","yellow","green","orange","beige","turquoise","pink"]
  
    
    for i in range(1,50):
        turtle_name.left(30)
        random.shuffle(colors)
        turtle_name.color(colors[0])
        for i in range(1,5):
            turtle_name.forward(100)
            turtle_name.right(120)
            

def draw_art():

    window = turtle.Screen();
    window.bgcolor("red")
    
    #define our turtle for square
    mimo = turtle.Turtle()
    mimo.speed(0)
    mimo.color("pink")
    mimo.shape("turtle")
    
    # the same turtle do all stuff
    #use the function draw_square() to draw square 
    draw_square(mimo)
    #use the function draw_triangle() to draw triangle 
    draw_triangle(mimo)
    mimo.pendown("4");
    
    #draw circle 
    #mimo.circle(120)
    

              
      
        


        





draw_art()
