# pygame이 잘 생성되었는지 확인
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_heigh = 649 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_heigh))

# 화면 타이틀 설정
pygame.display.set_caption("지니 게임") # 게임 이름
## 여기까지만 하면 화면이 떳따가 바로 종료됨

#이벤트 루프
running = True # running 변수 역할은 게임이 진행중인지 확인
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생 했는가?
            running = False # 게임 종료
# pygame 종료
pygame.quit()
