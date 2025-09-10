# pygame이 잘 생성되었는지 확인
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 649 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("지니 게임") # 게임 이름
## 여기까지만 하면 화면이 떳따가 바로 종료됨

#배경 이미지 불러오기
# background = pygame.image.load("C:\Users\82107\Desktop\PythonWorkspace\pygame_basic\background.png") # copy path 하면 경로 알려줌
background = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/background.png") # copy path 하면 경로 알려줌
# 탈출문자 처리 때문에 역슬러시를 두개씩 적어줌, 또는역슬러시를 슬러시로 변경해줌

#스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size # rectangle의 약자, 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기 
character_x_pos = (screen_width / 2 ) - (character_width / 2)# 캐릭터 포지션, 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
#character_y_pos = screen_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
character_y_pos = screen_height - character_height


#이벤트 루프
running = True # running 변수 역할은 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생 했는가?
            running = False # 게임 종료

    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos )) # blit -> block Transfer 이미지를 (0,0) 위치에 화면에 그린다. 
    # 이렇게만 적으면 좌표가 적히지 않아 화면에 표시가 안됨 

    # screen.fill((0,255,100)) # RGB값
    pygame.display.update() # 게임 화면을 다시 그리기 ( 계속 호출되어야 한다고 함..)
# pygame 종료
pygame.quit()
