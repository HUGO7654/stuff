import pygame

# Getting window ----------------------------------------------

white = (255,255,255)
black = (0,0,0)
minesweeper_gray = (189, 189, 189)
minesweeper_gray2 = (123, 123, 123)
magenta = (255, 0, 255)
orange = (247, 92, 30)


win_width = int(input('screen width: '))
win_height = int(input('screen height: '))
blocksize = int(input('blocksize: '))


screen = pygame.display.set_mode((win_width,win_height))
screen.fill(minesweeper_gray)
pygame.display.set_caption('Maze solver')

#--------------------------------------------------------------

def grid(): # draws grid of player chocie to screen

    for x in range(0,win_width,blocksize): 
        for y in range(0,win_height,blocksize):
            rect = pygame.Rect(x,y,blocksize,blocksize)
            pygame.draw.rect(screen,minesweeper_gray2,rect,1)
            

#--------------------------------------------------------------

def click(): # makes list of lists of size of players grid 
    global grid_xy

    grid_xy = []
    temp = win_width/blocksize
    for i in range(0, int(temp)):
        grid_xy.append([])

    for x in range(0, win_width):
        if x%blocksize == 0:
            x = x/blocksize
            for i in range (0,int(temp)):
                grid_xy[int(i)].append(False)
    return grid_xy
click() # just to make sure grid_xy exists        

#--------------------------------------------------------------        
                
        
# MAIN LOOP ---------------------------------------------------

running = True
grid()
while  running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(round((mx/blocksize)-0.5),round((my/blocksize)-0.5))
            grid_xy[round((my/blocksize)-0.5)][round((mx/blocksize)-0.5)] = True

            for y in range(0,win_height,blocksize): 
                for x in range(0,win_width,blocksize):
                    if  x%blocksize == 0 and y%blocksize == 0:
                        if grid_xy[int(y/blocksize)][int(x/blocksize)] == True:
                            rect = pygame.Rect(x,y,blocksize,blocksize)
                            pygame.draw.rect(screen,black,rect,0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mx, my = pygame.mouse.get_pos()
                print(round((mx/blocksize)-0.5),round((my/blocksize)-0.5))
                grid_xy[round((my/blocksize)-0.5)][round((mx/blocksize)-0.5)] = 'start'

                for y in range(0,win_height,blocksize): 
                    for x in range(0,win_width,blocksize):
                        if  x%blocksize == 0 and y%blocksize == 0:
                            if grid_xy[int(y/blocksize)][int(x/blocksize)] == 'start':
                                rect = pygame.Rect(x,y,blocksize,blocksize)
                                pygame.draw.rect(screen,magenta,rect,0)

            if event.key == pygame.K_2:
                mx, my = pygame.mouse.get_pos()
                print(round((mx/blocksize)-0.5),round((my/blocksize)-0.5))
                grid_xy[round((my/blocksize)-0.5)][round((mx/blocksize)-0.5)] = 'end'

                for y in range(0,win_height,blocksize): 
                    for x in range(0,win_width,blocksize):
                        if  x%blocksize == 0 and y%blocksize == 0:
                            if grid_xy[int(y/blocksize)][int(x/blocksize)] == 'end':
                                rect = pygame.Rect(x,y,blocksize,blocksize)
                                pygame.draw.rect(screen,orange,rect,0)

                            
    pygame.display.update()

