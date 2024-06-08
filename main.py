import sys
import pygame
from game import Game, GAME_UPDATE

pygame.init()
screen = pygame.display.set_mode((550, 620))
pygame.display.set_caption("Tetris")
icon = pygame.image.load("asset/tetris.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

score_font = pygame.font.Font("freesansbold.ttf", 35)
start_font = pygame.font.Font("freesansbold.ttf", 50)
tutorial_font = pygame.font.Font("freesansbold.ttf", 25)

background_image = pygame.image.load("asset/tetrisscreen.png")

pygame.time.set_timer(GAME_UPDATE, 400)

# Game states
START_SCREEN = "start_screen"
TUTORIAL_SCREEN = "tutorial_screen"
GAME_SCREEN = "game_screen"
game_state = START_SCREEN

game = Game()

def draw_start_screen():
    """
    Vẽ màn hình bắt đầu của trò chơi.
    Return:
        tuple: Hình chữ nhật của nút bắt đầu và nút hướng dẫn.
    """
    screen.blit(background_image, (0, 0))
    title_surface = start_font.render("Tetris Game", True, "red")
    start_surface = start_font.render("Start", True, "white")
    tutorial_surface = start_font.render("Tutorial", True, "white")
    title_rect = title_surface.get_rect(center=(275, 150))
    start_rect = start_surface.get_rect(center=(275, 300))
    tutorial_rect = tutorial_surface.get_rect(center=(275, 400))
    pygame.draw.rect(screen, "blue", start_rect.inflate(20, 20), border_radius=10)
    pygame.draw.rect(screen, "blue", tutorial_rect.inflate(20, 20), border_radius=10)
    screen.blit(title_surface, title_rect)
    screen.blit(start_surface, start_rect)
    screen.blit(tutorial_surface, tutorial_rect)
    return start_rect, tutorial_rect

def draw_tutorial_screen():
    """
    Vẽ màn hình hướng dẫn của trò chơi.
    """
    screen.fill((255, 255, 153))
    welcome_surface = start_font.render("Welcome to Tetris ", True, (0, 0, 204))
    screen.blit(welcome_surface, welcome_surface.get_rect(center=(275, 50)))

    tutorial_text = [
        "Use arrow keys to move",
        "Space to rotate",
        "Down to speed up",
        "Press Esc to go back"
    ]
    tutorial_images = [
        pygame.image.load("asset/arrow_keys.png"),
        pygame.image.load("asset/space_key.png"),
        pygame.image.load("asset/down_key.png"),
        pygame.image.load("asset/esc_key.png")
    ]
    y = 150
    for i, line in enumerate(tutorial_text):
        text_surface = tutorial_font.render(line, True, (0, 0, 204))
        image = tutorial_images[i]
        screen.blit(text_surface, (50, y))
        screen.blit(image, (370, y-20))
        y += 70
    enjoy_surface = start_font.render("Enjoy the game!", True, (0, 0, 204))
    screen.blit(enjoy_surface, enjoy_surface.get_rect(center=(275, 500)))
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
        pygame.draw.rect(screen, (51, 51, 255), pygame.Rect(340, 70, 170, 60), 0, 10)
        pygame.draw.rect(screen, (51, 51, 255), pygame.Rect(330, 210, 180, 160), 0, 10)
        pygame.draw.rect(screen, (51, 51, 255), pygame.Rect(330, 420, 180, 60), 0, 10)
        pygame.draw.rect(screen, (51, 51, 255), pygame.Rect(340, 550, 170, 60), 0, 10)
        screen.blit(score_font.render("Score", True, "red"), (370, 20, 50, 50))
        screen.blit(score_font.render("Next Block", True, "red"), (330, 160, 50, 50))
        screen.blit(score_font.render("Level", True, "red"), (370, 380, 50, 50))
        screen.blit(score_font.render("Highest Score", True, "red"), (310, 510, 50, 50))
        score_val_surface = score_font.render(str(game.score), True, "white")
        screen.blit(score_val_surface, score_val_surface.get_rect(centerx=410, centery=100))
        level_val_surface = score_font.render(str(game.level), True, "white")
        screen.blit(level_val_surface, level_val_surface.get_rect(centerx=410, centery=450))
        highest_score_surface = score_font.render(str(game.highest_score), True, "white")
        screen.blit(highest_score_surface, highest_score_surface.get_rect(centerx=410, centery=590))
        game.draw(screen)
        if game.game_over:
            screen.blit(pygame.image.load("asset/gameover.jpg"), (-30, 0))
            screen.blit(score_font.render("Press Space to Restart", True, "white"), (90, 300))
    pygame.display.update()
    clock.tick(60)
