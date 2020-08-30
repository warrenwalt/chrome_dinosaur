import pygame
import random

# initialize all the modules
pygame.init()

# for exiting the loop
isGaming = True

#  setting dimension of screen.
SIZE = 1000, 560
screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)

# setting caption of the screen
pygame.display.set_caption("CHROME DINOSAUR")

#  setting game icon
icon = pygame.image.load("images/bullet.png")
pygame.display.set_icon(icon)

# setting the color themes of this game using dictionary comprehension
a = ["SCORE", "CACTUS_COLOR", "BORDER_OF_OBJECT", "GROUND", "ROCKS", "BACKGROUND", "WHITE"]
c = [(226, 125, 96), (46,	219, 40), (195, 141, 158), (232, 168, 124), (106, 81, 31), (82, 78, 77), (255, 255, 255)]
COLORS = {a: c for (a, c) in zip(a, c)}

# creating the font system
sysFont = pygame.font.get_default_font()  # get default system font
font = pygame.font.SysFont(sysFont, 50)  # set system font as program font, and font-size of 60
score = font.render("SCORE: 109", True, COLORS["WHITE"])
score_rect = score.get_rect()
print(score.get_rect())

# creating ground
ground_width = SIZE[0]
ground_height = 100
ground_y = SIZE[1]-100
ground_x = 0

# creating rocks
rock_x = 950
rock_y = random.randint(SIZE[1]-100, SIZE[1])
rock_width = 25
rock_height = 25

# creating the dinosaur
din_x = 20
din_y = SIZE[1] - 200
din_width = 50
din_height = 100

# creating cactus
cact_x = 100
cact_y = SIZE[1] - 150
cact_width = 25
cact_height = 50

""" formulae for jumping ==> F = 1/2*m*v^2
    F = the force up/down , think of it as the y axis
    m  = mass of object
    v = velocity, how fast do you want it to travel
"""
isJumping = False  # checks if the player is jumping or not
v = 12
m = 1
f_list = []
m_list = []
v_list = []

while isGaming:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGaming = False

        if event.type == pygame.KEYDOWN:

            # for moving the dinosaur right(experiment).
            if event.key == pygame.K_RIGHT:
                din_x += 10
            if event.key == pygame.K_SPACE:
                isJumping = True
    if isJumping:
        # calculate the force (y)
        F = (1/2)*m*(v**2)

        # change the y coordinate
        din_y -= F
        # decrease velocity while going up and become negative while coming down.
        v = v-1

        # check if object has reached its maximum height
        if v < 0:
            m = -1  # negative sign is added to counter negative velocity

        # check if object has reached its original state.
        if v == -13:
            isJumping = False

            # ser original values of v and m
            v = 12
            m = 1
    if cact_x < 0:
        cact_x = SIZE[0]-cact_width
    cact_x -= 8

    # for moving the rock to make impression of the ground moving
    if rock_x < 0:
        rock_x = 950
    rock_x -= 8

    pygame.time.delay(20)
    screen.fill(COLORS["BACKGROUND"])  # background color
    pygame.draw.rect(screen, COLORS["SCORE"], [SIZE[0]-250, 10, score_rect[2]+10, score_rect[3]+10])  # scoreboard color
    screen.blit(score, (SIZE[0]-250, 10))  # for scoreboard
    pygame.draw.rect(screen, COLORS["GROUND"], [ground_x, ground_y, ground_width, ground_height])  # ground
    pygame.draw.ellipse(screen, COLORS["ROCKS"], [rock_x, rock_y, rock_width, rock_height])  # rocks
    pygame.draw.rect(screen, COLORS["BORDER_OF_OBJECT"], [din_x, din_y, din_width, din_height], 4)  # rect object
    pygame.draw.rect(screen, COLORS['CACTUS_COLOR'], (cact_x, cact_y, cact_width, cact_height), 2)  # cactus
    pygame.display.update()

#  exit the game correctly
pygame.quit()
