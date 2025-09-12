# 코드가 너무 길어 리펙토링 ! 

########################################기본 초기화  (반드시 해야하는 것들 )##############################################
# 
import pygame
pygame.init() # 초기화 (반드시 필요)
# 화면 크기 설정 (480 * 640)
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
# 화면 타이틀 설정
pygame.display.set_caption("게임 이름") 
## 여기까지만 하면 화면이 떳따가 바로 종료됨

# FPS
clock = pygame.time.Clock()
#######################################################################################################################


#1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 이동 속도, 폰트 등)

#이벤트 루프
running = True # running 변수 역할은 게임이 진행중인지 확인
while running:
    dt = clock.tick(30) 
# 2. 이벤트 처리 부분(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT : 
            running = False # 게임 종료      
# 3. 게임 케릭터 위치 정의     

# 4. 충돌 처리
# 5. 화면에 그리기
    pygame.display.update() 
# pygame 종료
pygame.quit()
