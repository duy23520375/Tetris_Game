import sys
import pygame
from game import Game
from color import Colors

pygame.init()
screen = pygame.display.set_mode((550, 620))
pygame.display.set_caption("Tetris")
icon = pygame.image.load("asset/tetris.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

score_font = pygame.font.Font("freesansbold.ttf", 35)
start_font = pygame.font.Font("freesansbold.ttf", 50)

# Load the background image
background_image = pygame.image.load("asset/tetrisscreen.png")

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Game states
START_SCREEN = "start_screen"
TUTORIAL_SCREEN = "tutorial_screen"
GAME_SCREEN = "game_screen"
game_state = START_SCREEN

game = Game()

def draw_start_screen():
    screen.blit(background_image, (0, 0))
    title_surface = start_font.render("Tetris", True, "white")
    start_surface = start_font.render("Start", True, "white")
    tutorial_surface = start_font.render("Tutorial", True, "white")

    title_rect = title_surface.get_rect(center=(275, 150))
    start_rect = start_surface.get_rect(center=(275, 300))
    tutorial_rect = tutorial_surface.get_rect(center=(275, 400))

    screen.blit(title_surface, title_rect)
    screen.blit(start_surface, start_rect)
    screen.blit(tutorial_surface, tutorial_rect)

    return start_rect, tutorial_rect

def draw_tutorial_screen():
    screen.fill(Colors.dark_blue)
    tutorial_text = [
        "Use arrow keys to move",
        "Space to rotate",
        "Down to speed up",
        "Press Esc to go back"
    ]
    y = 100
    for line in tutorial_text:
        text_surface = score_font.render(line, True, "white")
        screen.blit(text_surface, (50, y))
        y += 50

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_state == START_SCREEN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                start_rect, tutorial_rect = draw_start_screen()
                if start_rect.collidepoint(mouse_pos):
                    game_state = GAME_SCREEN
                elif tutorial_rect.collidepoint(mouse_pos):
                    game_state = TUTORIAL_SCREEN
        elif game_state == TUTORIAL_SCREEN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state = START_SCREEN
        elif game_state == GAME_SCREEN:
            if event.type == pygame.KEYDOWN:
                if game.game_over:
                    if event.key == pygame.K_SPACE:
                        game.reset()
                else:
                    if event.key == pygame.K_LEFT:
                        game.move_left()
                    if event.key == pygame.K_RIGHT:
                        game.move_right()
                    if event.key == pygame.K_DOWN:
                        game.move_down()
                    if event.key == pygame.K_SPACE:
                        game.rotate()
            if event.type == GAME_UPDATE:
                if not game.game_over:
                    game.move_down()

    if game_state == START_SCREEN:
        start_rect, tutorial_rect = draw_start_screen()
    elif game_state == TUTORIAL_SCREEN:
        draw_tutorial_screen()
    elif game_state == GAME_SCREEN:
        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, (100, 101, 123), pygame.Rect(340, 70, 170, 60), 0, 10)
        pygame.draw.rect(screen, (100, 101, 123), pygame.Rect(330, 210, 180, 160), 0, 10)
        pygame.draw.rect(screen, (100, 101, 123), pygame.Rect(330, 420, 180, 60), 0, 10)
        pygame.draw.rect(screen, (100, 101, 123), pygame.Rect(340, 550, 170, 60), 0, 10)
        screen.blit(score_font.render("Score", True, "white"), (370, 20, 50, 50))
        screen.blit(score_font.render("Next Block", True, "white"), (330, 160, 50, 50))
        screen.blit(score_font.render("Level", True, "white"), (370, 380, 50, 50))
        screen.blit(score_font.render("Highest Score", True, "white"), (310, 510, 50, 50))

        score_val_surface = score_font.render(str(game.score), True, "white")
        screen.blit(score_val_surface, score_val_surface.get_rect(centerx=410, centery=100))
        level_val_surface = score_font.render(str(game.level), True, "white")
        screen.blit(level_val_surface, level_val_surface.get_rect(centerx=410, centery=450))
        highest_score_surface = score_font.render(str(game.highest_score), True, "white")
        screen.blit(highest_score_surface, highest_score_surface.get_rect(centerx=410, centery=590))

        game.draw(screen)

        if game.game_over:
            screen.blit(score_font.render("Game Over", True, "red"), (150, 250))
            screen.blit(score_font.render("Press Space to Restart", True, "white"), (80, 300))

    pygame.display.update()
    clock.tick(60)
