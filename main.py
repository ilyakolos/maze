from data import *
from maze_funcion import *


window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Лабіринт (твої данні вже у мене)")

def run():

    hero = Hero(50,50, 75,75, image= hero_list)
    bot1 = Bot(250, 100, 50, 50, image= bot1_list, orientation= "vertical")

    clock = pygame.time.Clock()
    game = True
    while game:
        window.fill((122, 246, 185))

        x,y = 20, 20
        for i in range(50):
            pygame.draw.line(window, (255,255,255), (0, y), (1000, y))
            pygame.draw.line(window, (255,255,255), (x, 0), (x, 700))
            x += 20
            y += 20

        



    hero.move(window)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.MOVE["UP"] = True
            if event.key == pygame.K_d:
                hero.MOVE["RIGHT"] = True
            if event.key == pygame.K_s:
                hero.MOVE["DOWN"] = True
            if event.key == pygame.K_a:
                hero.MOVE["LEFT"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.MOVE["UP"] = False
            if event.key == pygame.K_d:
                hero.MOVE["RIGHT"] = False
            if event.key == pygame.K_s:
                hero.MOVE["DOWN"] = False
            if event.key == pygame.K_a:
                hero.MOVE["LEFT"] = False

          
        clock.tick(60)
        pygame.display.flip()

run()