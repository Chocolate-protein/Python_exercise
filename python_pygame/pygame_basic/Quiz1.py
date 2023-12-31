#  Quiz1) 똥 피하기 게임

import random
import pygame

#********************************************************************************

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()   # 초기화(필수)

# 화면 크기 설정
screen_width = 480   # 가로크기
screen_height = 640   # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")   # 게임 이름

# FPS
clock = pygame.time.Clock()

#********************************************************************************

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경화면
background = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\background.png")

# 사용자 캐릭터 크기
character = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# 캐릭터 위치
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# 이동 위치
character_to_x = 0

# 이동속도
character_speed = 0.3

# 똥
# 사용자 캐릭터 크기
enemy = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

# 캐릭터 위치
enemy_x_pos = random.randrange(0, screen_width - enemy_width + 1)
enemy_y_pos = 0

# 이동속도
enemy_speed = 0.5

#********************************************************************************


running = True
while running:
    dt = clock.tick(60)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
    
        if event.type == pygame.KEYUP:
            character_to_x = 0
    
    enemy_y_pos += enemy_speed * dt
    

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos >= screen_height:
        enemy_x_pos = random.randrange(0, screen_width - enemy_width + 1)
        enemy_y_pos = 0

    # 4. (이미지 간) 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("Crash!")
        running = False
    

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    
    pygame.display.update()

pygame.time.delay(1500)

# pygame 종료
pygame.quit()