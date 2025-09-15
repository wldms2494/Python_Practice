# Quiz : 하늘에서 떨어지는 똥 피하기 게임을 만드시오
# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS는 30으로 고정

# [게임 이미지]
#. 배경 : 640 * 480 (세로 가로) - background.png
#. 캐릭터 : 70 * 70 - character.png
#. 똥 : 70 * 70 - enemy.png


########################################기본 초기화  (반드시 해야하는 것들 )##############################################
# 
import pygame
import random
pygame.init() 
screen_width = 480 
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥게임") 


# FPS
clock = pygame.time.Clock()
#######################################################################################################################


#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 이동 속도, 폰트 등)
background = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/background.png")
character = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/character.png")
enemy = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/poop.png")


character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

enemy_size = character.get_rect().size
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = random.randint(0,screen_width - enemy_width)
enemy_y_pos = 0 

to_x = 0
to_y = 0
character_speed = 10
enemy_speed = 8
enemy_to_y = 0

#이벤트 루프
running = True 
while running:
    dt = clock.tick(30) 
# 2. 이벤트 처리 부분(키보드, 마우스 등)
    for event in pygame.event.get():
        print("event running")
        
        if event.type == pygame.QUIT : 
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
        
    character_x_pos += to_x 
   


# 3. 게임 케릭터 위치 정의   
    if(character_x_pos < 0):
        character_x_pos = 0
    elif(character_x_pos > screen_width - character_width):
        character_x_pos = screen_width - character_width
   
    enemy_y_pos += enemy_speed
    if enemy_y_pos > screen_height :
        # enemy_y_pos = screen_height - enemy_height
        enemy_y_pos = 0
        enemy_x_pos = random.randint(70,480- enemy_width) 


# 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if(character_rect.colliderect(enemy_rect)):
        running = False
        
        


    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos, enemy_y_pos))
# 5. 화면에 그리기
    pygame.display.update() 
# pygame 종료
pygame.quit()
