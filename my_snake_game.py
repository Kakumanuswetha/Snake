import pygame#normally it needs to be installed
import random
pygame.init()#initializes all the imported pygame modules.
width=600
height=400
snake_block=10#block size of the snake
dis = pygame.display.set_mode((width,height))#creating main game display
#update module used whenever we made change on the display after this method is call they appears as it refreshes the display..
pygame.display.update()
pygame.display.set_caption("Snake game by Swetha")

#creation of colors using rgb values.
h=(255,150,20)#color for the head of the snake
body=(0,200,255)#color for body of the snake
red=(128,0,0)
black=(0,0,0)
white=(255,255,255)
grey=(150,150,150)
orange=(255,150,20)
fo=(0,200,255)#color for food
#rect at module draw is used to draw rectangles.This function takes 3 inputs:the display in which we draw,the color and the rectangle specification which are position and dimension 

#fill function changes the background color
dis.fill(grey)
x=width//2
y=height//2
x_change=0
y_change=0
game_over=False
snake_speed=15
clock = pygame.time.Clock()
game_close=False

font_style=pygame.font.SysFont("freesans",25)#creation of a font to display play again or quit.
lost_img=font_style.render("You Lost! Press P-Play Agian and Q-Quit",True,red)
def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,orange,(x[0],x[1],snake_block,snake_block))      
def thescore(score):
    end_score=font_style.render("Your score: "+str(score),True,fo)
    dis.blit(end_score,[0,0])

def game_loop():
    game_over=False
    game_close=False
    x=width//2
    y=height//2
    x_change=0
    y_change=0
    foodx=snake_block*random.randint(0,(width//snake_block)-1)
    foody=snake_block*random.randint(0,(height//snake_block)-1)
    snake_list=[]#this is alist which contains positions of snake body
    length_of_snake=1
    while(game_over==False):
    #The following loop is included as the program doesnot close/end by clicking X button and the kernel closes if we attempt to.
    #To do so we need to specify to close it by following lines.
        while(game_close==True):
            dis.fill(white)
            dis.blit(lost_img,[100,100])# display.blit() function is used to display a image on it which only takes an image and the required position for it.
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True 
                        game_close=False
                    if event.key==pygame.K_p:
                        game_loop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    x_change=0
                    y_change=-10
                elif event.key==pygame.K_DOWN:
                    x_change=0
                    y_change=10  
                elif event.key==pygame.K_LEFT:
                    x_change=-10
                    y_change=0
                elif event.key==pygame.K_RIGHT:
                    x_change=10
                    y_change=0
        if(x>=width or x<0 or y>=height or y<0):
                game_close=True
        x=x+x_change
        y=y+y_change
        dis.fill(grey)
        # a rectangle of size snake_block x snake_block is placed at center the dispaly

        pygame.draw.rect(dis,fo,(foodx,foody,snake_block,snake_block))#food rectangle
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if(len(snake_list)>length_of_snake):
            del snake_list[0]
        for i in snake_list[:-1]:
            if(i==snake_head):
                game_close=True
        our_snake(snake_block,snake_list)#calling oursnake function to draw the update snake list values
        if(x==foodx and y==foody):
            length_of_snake+=1
            foodx=snake_block*random.randint(0,(width//snake_block)-1)
            foody=snake_block*random.randint(0,(height//snake_block)-1)
        thescore(length_of_snake-1)#to update the score of the game
        pygame.display.update()
        
        clock.tick(snake_speed)#speed at which snake moves

    pygame.quit()
game_loop()
# Used to quit the display.
#cannot able to see the pygame display as it immediately quits 
#So we need to create a gameloop that keeps looping until we quit the game.

