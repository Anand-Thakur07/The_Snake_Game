#DEVELOPED BY ANAND
import random
import pygame
pygame.init()
import os

pygame.mixer.init()

#Colors
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)

#Game window
game_window = pygame.display.set_mode((600,350))
pygame.display.set_caption("PLAY SNAKE")
pygame.display.update()

bg_image = pygame.image.load("BGIMG.jpg")
bg_image = pygame.transform.scale(bg_image, (600, 350)).convert_alpha()

fps = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snake_list, snake_l, snake_w):
    for x,y in snake_list:
         pygame.draw.rect(game_window, color, [x, y, snake_l, snake_w])

#Home screen
def welcome_screen():
    exit_game = False
    while not exit_game:
        #game_window.fill(white)
        game_window.blit(bg_image, (0,0))
        text_on_screen("Welcome to ", (0,100,0), 150, 130)
        text_on_screen("The Snake Game", (0,50,0), 270, 130)
        text_on_screen("Press Space bar to start", (45,69,34), 180, 160)
        font1 = pygame.font.SysFont(None, 19)
        game_window.blit(font1.render("Developed by Anand", True, black), [5, 335])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("BGM.mp3")
                    pygame.mixer.music.play(5)
                    game_loop()
        pygame.display.update()
        clock.tick(fps)

#Game loop
def game_loop():
    # Game variables
    exit_game = False
    game_over = False
    snake_x = 250
    snake_y = 170
    snake_l = 8
    snake_w = 8
    velocity_x = 7
    velocity_y = 0
    food_l = 6
    food_w = 6
    food_x = random.randint(40, 500)
    food_y = random.randint(40, 300)
    score = 0
    snake_list = []
    snake_length = 1

    if (not os.path.exists("highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write(str(0))
    with open("Highscore.txt","r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill((221,160,221))
            text_on_screen("Game Over!", (128,0,128), 245, 135)
            text_on_screen("Press Enter to restart", (128, 0, 128), 200, 165)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("BGM.mp3")
                        pygame.mixer.music.play()
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_y = 7
                        velocity_x = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -7
                        velocity_y = 0

                    if event.key == pygame.K_RIGHT:
                        velocity_x = 7
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -7
                        velocity_x = 0

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 4 and abs(snake_y - food_y) < 4:
                score += 1
                food_x = random.randint(15, 500)
                food_y = random.randint(15, 300)
                snake_length += 4

            if int(highscore)<score:
                highscore = score

            game_window.fill((240,248,255))
            text_on_screen("Your Score: "+ str(score), (0,139,139), 5, 5)
            text_on_screen("Highscore: " + str(highscore), (0,128,128), 460, 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("GO.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>600 or snake_y<0 or snake_y>350:
                game_over = True
                pygame.mixer.music.load("GO.mp3")
                pygame.mixer.music.play()

            plot_snake(game_window, (75,0,130), snake_list, snake_l, snake_w)
            pygame.draw.rect(game_window, black, [food_x, food_y, food_l, food_w])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome_screen()
