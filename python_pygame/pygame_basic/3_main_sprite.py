# 캐릭터
import pygame

pygame.init()   # 초기화(필수)

# 화면 크기 설정
screen_width = 480   # 가로크기
screen_height = 640   # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\character.png")
character_size = character.get_rect().size   # 이미지 크기 불러옴
character_width = character_size[0]   # 캐릭터 가로크기
character_height = character_size[1]   # 캐릭터 세로크기

# 캐릭터 위치 설정 : 좌측 상단 = (0, 0)
character_x_pos = (screen_width / 2) - (character_width / 2)   # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height  # 화면 세로 크기 가장 아래

# 화면 타이틀 설정
pygame.display.set_caption("PyGame")   # 게임 이름

# 이벤트 루프 : 게임이 종료되지 않도록 대기
running = True   # 게임이 진행중인가?
while running:
    for event in pygame.event.get():   # 이벤트가 발생 하였는가?
    # 필수, 사용자의 활동 체크 -> 게임 동작
        if event.type == pygame.QUIT:   # 창이 닫히는 이벤트 발생 하였는가?
            running = False

    # screen.fill((100, 100, 155))   # 색 채우기(R, G, B)
    screen.blit(background, (0, 0))   # 배경 그리기(시작 위치(x, y))
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    pygame.display.update()   # 게임 화면 다시 그리기


# pygame 종료
pygame.quit()