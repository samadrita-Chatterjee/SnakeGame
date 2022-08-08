from importlib import resources
import pygame
import random
import time
pygame.init()
pygame.mixer.init()
width,height=600,600
game_screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")
x,y =100,200                        #initial coordinate of sanke
box_x,box_y = 10, 0            

apple_x = random.randrange(0, width)//10*10
apple_y = random.randrange(0, height)//10*10
body_list=[(x,y)]                   #list to store the coordinate of each unit of body of snake
clock = pygame.time.Clock()
game_over =False

font =pygame.font.SysFont('arial',25,'bold')

def snake():
    global x,y,apple_x,apple_y,game_over
    x= (x + box_x)%width
    y = (y + box_y)%height
    if((x,y) in body_list):
        game_over = True
        return 
    body_list.append((x,y))

    if (apple_x == x and  apple_y == y):
        sound = pygame.mixer.Sound("Music1.wav")
        pygame.mixer.Sound.play(sound)
        while((apple_x, apple_y) in body_list):
            apple_x = random.randrange(0, width)//10.0*10.0
            apple_y = random.randrange(0, height)//10.0*10.0
    else:
        del body_list[0]

    game_screen.fill((203, 195, 227))
    score= font.render("Score: "+str(len(body_list)-1), True,(0,100,0))
    game_screen.blit(score, [0,0])
    pygame.draw.rect(game_screen, ((255,0,0)),[apple_x, apple_y, 10, 10])
    for (i,j) in body_list:
        pygame.draw.rect(game_screen, ((0,0,0)), [i,j,10,10])
    pygame.display.update() 

while True:
    #Game Over
    if (game_over):                                       
        game_screen.fill((0,0,0))
        score = font.render("Score: "+str(len(body_list)-1), True, ((0,100,0))) #Score
        game_screen.blit(score, [0,0])
        msg = font.render("GAME OVER!", True, (255,255,255))
        game_screen.blit(msg, [width//3,height//3])
        sound = pygame.mixer.Sound("Music2.wav")
        pygame.mixer.Sound.play(sound)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()
    events=pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
          pygame.quit()
          quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT and box_x != 10):            
                box_x = -10
                box_y = 0
            elif(event.key == pygame.K_RIGHT and box_x != -10):
                box_x= 10
                box_y = 0
            elif(event.key == pygame.K_UP and box_y != 10):
                box_x = 0
                box_y = -10
            elif(event.key == pygame.K_DOWN and box_y != -10):
                box_x = 0
                box_y = 10
            else:
                continue
            snake() #if there is no events snake  function will call automatically 
    if (not events):
        snake()
    clock.tick(15)
    


    
     

