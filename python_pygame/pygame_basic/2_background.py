#  배경
import pygame

pygame.init()   # 초기화(필수)

# 화면 크기 설정
screen_width = 480   # 가로크기
screen_height = 640   # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\김영기\\Desktop\\Python Workspace\\python_util\\pygame_basic\\background.png")


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
    screen.blit(background, (0, 0))   # 배경 그리기 : .blit(이미지, (시작위치 : x, y))
    pygame.display.update()   # 게임 화면 다시 그리기

# pygame 종료
pygame.quit()