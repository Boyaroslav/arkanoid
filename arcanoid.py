import pygame
import random
import time

pygame.init()
root=pygame.display.set_mode((1000,800))
clock=pygame.time.Clock()

colorthemes=[[(255,0,255),(255,255,255),(255,0,0),(0,255,0),(0,0,0)],[(50,100,50),(255,100,100),(100,255,100),(200,200,255),(100,150,100)]]

colors=colorthemes[random.randint(0,1)]

blocks=["+" for i in range(20)]

xont=pygame.font.Font('font.ttf',30)




x=500
y=600
inertion=0
platx=400
platy=650
up,down=1,0
left,right=0,0

score=0


while True:
    text=xont.render(str(score),True,(255,255,255))
    root.fill(colors[-1])
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            quit()
        if i.type==pygame.KEYDOWN:
            if i.key==pygame.K_LEFT:
                left,right=1,0
            if i.key==pygame.K_RIGHT:
                left,right=0,1
        if i.type==pygame.KEYUP:
            left,right=0,0
    for j in range(0,9):
        if blocks[j]=='+':
            pygame.draw.rect(root,colors[2],(j*100+75,50,50,50))
            if x-50<j*100+75+50 and x+50>j*100+75:
                if y<=100 and y>=50:
                    down,up=1,0
                    blocks[j]="-"
                    score+=1
    for j in range(10,19):
        if blocks[j]=='+':
            pygame.draw.rect(root,colors[3],((j-10)*100+75,150,50,50))
            if (x-50<(j-10)*100+75+50 and x>(j-10)*100+75) or (x+50<(j-10)*100+75+50 and x+50>(j-10)*100+75) or (x-50<(j-10)*100+75+50 and x-50>(j-10)*100+75):
                if y<=200 and y>=150:
                    down,up=1,0
                    blocks[j]="-"
                    score+=1
    if y<=0:
        down,up=1,0
    if left:
        platx-=10
    if right:
        platx+=10
    if platx>=800:
        platx-=10
    if platx<=0:
        platx+=10
    if platx-50<x and platx+250>x:
        if platy-20==y:
            inertion=((x-platx)+(x-(platx+200)))  //30       #400      #x-platx=___+---   #
            up,down=1,0
    if up:
        y-=10
        x+=inertion
    if down:
        y+=10
        x+=inertion
    if x<=0 or x>=1000:
        inertion=-inertion
    pygame.draw.circle(root,colors[1],(x,y),20)         #platx+200=center of the platform
    pygame.draw.rect(root,colors[0],(platx,platy,200,50))
    root.blit(text,(10,10))
    if score==18:
        pygame.draw.rect(root,(255,255,255),(100,100,800,600))
        fin=xont.render("You win!",True,(0,0,0))
        root.blit(fin,(500,400))
        pygame.display.update()
        time.sleep(1)
        quit()
    if y>=800:
        pygame.draw.rect(root,(255,255,255),(100,100,800,600))
        fin=xont.render("You lose!",True,(0,0,0))
        root.blit(fin,(500,400))
        pygame.display.update()
        time.sleep(1)
        quit()
    pygame.display.update()
    clock.tick(60)