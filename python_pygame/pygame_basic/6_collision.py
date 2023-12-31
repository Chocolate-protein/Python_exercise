# 충돌처리
import pygame

pygame.init()   # 초기화(필수)

# 화면 크기 설정
screen_width = 480   # 가로크기
screen_height = 640   # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("PyGame")   # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\background.png")

# FPS
clock = pygame.time.Clock()

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\character.png")
character_size = character.get_rect().size   # 이미지 크기 불러옴
character_width = character_size[0]   # 캐릭터 가로크기
character_height = character_size[1]   # 캐릭터 세로크기

# 캐릭터 위치 설정 : 좌측 상단 = (0, 0)
character_x_pos = (screen_width / 2) - (character_width / 2)   # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터
enemy = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size   # 이미지 크기 불러옴
enemy_width = enemy_size[0]   # 캐릭터 가로크기
enemy_height = enemy_size[1]   # 캐릭터 세로크기

enemy_x_pos = (screen_width / 2) - (enemy_width / 2)   # 화면 가로의 절반 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로의 절반 위치


# 이벤트 루프 : 게임이 종료되지 않도록 대기
running = True   # 게임이 진행중인가?
while running:
    dt = clock.tick(60)   # 게임화면의 초당 프레임  .tick(프레임수)
    # but, 프레임에 따라 이동속도 차이남 -> 보정 필요
    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get():   # 이벤트가 발생 하였는가?
    # 필수, 사용자의 활동 체크 -> 게임 동작
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트 발생 하였는가?
            running = False
        
        # 입력값에 따라 캐릭터 이동
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는가
            if event.key == pygame.K_LEFT:   # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:   # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:   # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:   # 캐릭터를 아래로
                to_y += character_speed
        
        # 사용자가 키에서 손을 뗐을때
        if event.type == pygame.KEYUP:   # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 이동, 프레임당 이동속도 보정
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 캐릭터가 화면을 벗어난 경우
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = screen_width - character_width
    
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = screen_height - character_height

    # 충돌 처리위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("Crash!")
        running = False

    # screen.fill((100, 100, 155))   # 색 채우기(R, G, B)
    screen.blit(background, (0, 0))   # 배경 그리기(시작 위치(x, y))
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    pygame.display.update()   # 게임 화면 다시 그리기


# pygame 종료
pygame.quit()