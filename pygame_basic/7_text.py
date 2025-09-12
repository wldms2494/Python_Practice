# 텍스트 처리 


# pygame이 잘 생성되었는지 확인
import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정 (480 * 640)
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("지니 게임") # 게임 이름
## 여기까지만 하면 화면이 떳따가 바로 종료됨

# FPS
clock = pygame.time.Clock()

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

# 캐릭터가 이동할 좌표
to_x = 0
to_y = 0

# 캐릭터 속도
character_speed = 0.6


# enemy 적 캐릭터 만들기
enemy = pygame.image.load("C:/Users/82107/Desktop/PythonWorkspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = (screen_width / 2 ) - (enemy_width / 2)
enemy_y_pos = (screen_height/2) - enemy_height # 화면 중앙에 배치 

# 폰트 정의 및 사이즈 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성, None 일 경우 디폴트 실행

# 총 시간
total_time = 10
# 시작 시간 
start_ticks = pygame.time.get_ticks() #시간 tick을 받아옴, tick이란 흐른시간을 밀리초 단위로 의미


#이벤트 루프
running = True # running 변수 역할은 게임이 진행중인지 확인
while running:
    dt = clock.tick(100) # 게임 화면의 초당 프레임 수를 설정 dt 는 delta를 의미, 10으로 설정하면 버벅거리는게 보임
    # 캐릭터가 1초에 100만큼 이동해야함 
    # 10 fps : 1번에 몇 만큼 이동? 10만큼 then 10* 10 = 100 그래서 10 번 동작해야함
    # 20 fps : 1번에 몇 만큼 이동? 5만큼 then 5* 20 = 100 그래서 20 번 동작해야함

    # character_speed 가 5일때 FPS가 10이면 속도가 
    print("fps : " + str(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT : # 창이 닫히는 이벤트가 발생 했는가?
            running = False # 게임 종료
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT : # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x = 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 땠을때 발생 -> 멈춤을 위함
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x  = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리 (캐릭터가 화면 밖을 벗어나지 못하도록 )
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width # 실제 화면 크기만 작성하면 화면 밖으로 나갈 수 있기 때문에 캐릭터 크기를 빼줌

    # 세로 경계값 처리 
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height 

    # 충돌 처리
    character_rect = character.get_rect() # 좌표가져오깅, 초기 좌표값 (0,0)을 가져옴
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos # 이렇게 설정하면 이동 좌표값을 가져옴 

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if(character_rect.colliderect(enemy_rect)): # 서로 충돌했는지 확인하는 함수 colliderect
        print("충돌했습니다.")
        running = False # 게임 종료
    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos )) # blit -> block Transfer 이미지를 (0,0) 위치에 화면에 그린다. 
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos )) # blit -> block Transfer 이미지를 (0,0) 위치에 화면에 그린다. 
    # 이렇게만 적으면 좌표가 적히지 않아 화면에 표시가 안됨 

    # screen.fill((0,255,100)) # RGB값

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = ((pygame.time.get_ticks()) - start_ticks) / 1000 # 경과시간(밀리세컨)을 초로 환산
    
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255)) # 1초 2초 정수 초단위로 표시하기 위해 int로 변환
    screen.blit(timer,(10,10))

    if total_time - elapsed_time <= 0:
        print(타임아웃)
        running = False

    # 출력할 글자, alias는 True, 그리고 글자 색상
    pygame.display.update() # 게임 화면을 다시 그리기 ( 계속 호출되어야 한다고 함..)

# 잠시 대기
pygame.timne.delay(2000)
# pygame 종료
pygame.quit()
