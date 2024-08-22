import pygame 
import sys
from game import Game
from colors import Colors

pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score",True, Colors.white)
next_surface = title_font.render("Next",True,Colors.white)
game_over = title_font.render("GAME OVER",True, Colors.white)
high_score_surface = title_font.render("HIGH SCORE",True, Colors.white)

high_score_rect = pygame.Rect(320,540,170,60)
score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200) #timer in miliseconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
   
    #drawing
    score_value_surface = title_font.render(str(game.score),True,Colors.white)
    high_score_value = title_font.render(str(game.high_score),True,Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365,20,50,50))
    screen.blit(next_surface,(375, 180,50,50))
    screen.blit(high_score_surface,(320,510,50,50))
    if game.game_over == True:
        
        screen.blit(game_over, (320,450,50,50))
    
    pygame.draw.rect(screen,Colors.lightblue,score_rect,0,15)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery) )
    pygame.draw.rect(screen,Colors.lightblue,high_score_rect,0,15)
    screen.blit(high_score_value,high_score_value.get_rect(centerx = high_score_rect.centerx,centery = high_score_rect.centery) )
    pygame.draw.rect(screen,Colors.lightblue,next_rect,0,15)

    
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)


