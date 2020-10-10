import pygame


class Dinosaur:
    """:except
        Thi s will be the player. The dinosaur will be moving forward
        as    it jumps cactus, in an attempt to reach the highest score possible
        s cores are awarded when dinosaur successfully jumps over a cactus without touching the cactus.
    """

    # images for running
    run = ["Run (1).png", "Run (2).png", "Run (3).png", "Run (4).png", "Run (5).png", "Run (6).png", "Run (7).png",
           "Run (8).png"]
    walkCount = 0
    dino_run = []
    for i in range(len(run)):
        dino_run.append(pygame.transform.scale(pygame.image.load("images/running/" + run[i]), (200, 150)))

    # images for jumping
    jump = ["Jump (1).png", "Jump (2).png", "Jump (3).png", "Jump (4).png", "Jump (9).png", "Jump (10).png",
            "Jump (11).png", "Jump (12).png"]
    dino_jump = []
    for j in range(len(jump)):
        dino_jump.append(pygame.transform.scale(pygame.image.load("images/jumping/" + jump[j]), (200, 150)))

    # images for dying.
    die = ['Dead (1).png', 'Dead (2).png', 'Dead (3).png', 'Dead (4).png', 'Dead (5).png', 'Dead (6).png',
           'Dead (7).png', 'Dead (8).png']
    dino_die = []
    for d in range(len(die)):
        dino_die.append(pygame.transform.scale(pygame.image.load("images/dead/"+die[d]), (200, 150)))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 50
        self.HEIGHT = 100
        self.isJumping = False


class Cactus:
    """:except
        cactus are basically the enemies, they should be jumped by the dinosaur as it moves.
        when player comes into contact with cactus, game ands(though there could be future changes for this, now we just
        keeping things simple)
    """
    moving = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 25
        self.HEIGHT = 70

    def move(self, v):
        if self.x < 0:
            self.x = App().WIDTH
        self.x -= v

    def get_rect(self):
        pass


class Background:
    """:except
        this will be the image or color on the background. it can change with time, especially when the player is doing
        so well.
    """

    def __init__(self):
        self.a = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN"]
        self.c = [(226, 125, 96), (46, 219, 40), (195, 141, 158), (232, 168, 124), (106, 81, 31), (82, 78, 77),
                  (255, 255, 255)]
        self.COLORS = {a: c for (a, c) in zip(self.a, self.c)}
        self.current = self.COLORS["SIX"]


class Score:
    """:except
        this will keep track of points scored by player when it successfully jumps over a cactus.
        it will store the highest record and time taken to attain it.
    """

    def __init__(self, x, y):
        self.text = str(0)
        self.x = x
        self.y = y

    def score(self):
        sysFont = pygame.font.get_default_font()
        font = pygame.font.SysFont(sysFont, 50)
        score = font.render("SCORE: " + self.text, True, Background().COLORS["SEVEN"])
        return score

    def change_score(self, din_right, cact_left, cact_top, din_bottom, din_left, cact_right):
        bot_up_dist = din_bottom - cact_top
        left_right_dist = din_right - cact_left

        if left_right_dist == 0 and din_bottom > cact_top:  # check if right side of dinosaur has collided with
            # left-side of cactus
            print("Game Over: sides Touched.")
            return False
        else:
            self.text = str(int(self.text) + 5)
            return True
        # if dist == 0:
        #     print("game Over")
        # else:
        #     self.text = str(int(self.text) + 5)


class Ground:
    """:except
        this is standing place for both the cactus and the dinosaur
    """

    def __init__(self):
        self.X = 0
        self.Y = 500
        self.WIDTH = App().WIDTH
        self.HEIGHT = 100


class App:
    """
        this will be the dimensions of the application, and also will be responsible for creating objects for
        other classes.
    """

    def __init__(self):
        pygame.init()
        self.WIDTH = 1200
        self.HEIGHT = 600
        self.isGaming = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.a = ["SCORE", "CACTUS_COLOR", "BORDER_OF_OBJECT", "GROUND", "ROCKS", "BACKGROUND", "WHITE"]
        self.c = [(226, 125, 96), (46, 219, 40), (195, 141, 158), (232, 168, 124), (106, 81, 31), (82, 78, 77),
                  (255, 255, 255)]
        self.COLORS = {a: c for (a, c) in zip(self.a, self.c)}

    @staticmethod
    def dimension():
        pygame.display.set_caption("CHROME DINOSAUR")
        icon = pygame.image.load("images/bullet.png")
        pygame.display.set_icon(icon)

    def mainloop(self):
        m = 1
        v = 12
        FPS = 64
        clock = pygame.time.Clock()
        self.dimension()
        score = Score(900, 20)
        ground = Ground()
        cactus = Cactus(300, 428)
        dinosaur = Dinosaur(550, 370)
        background = Background().current
        while self.isGaming:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isGaming = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dinosaur.isJumping = True
                    if event.key == pygame.K_UP:
                        pass
            if dinosaur.isJumping:
                # calculate the force (y)
                F = (1 / 2) * m * (v ** 2)

                # change the y coordinate
                dinosaur.y -= F
                # decrease velocity while going up and become negative while coming down.
                v = v - 1

                # check if object has reached its maximum height
                if v < 0:
                    m = -1  # negative sign is added to counter negative velocity

                # check if object has reached its original state.
                if v == -13:
                    dinosaur.isJumping = False

                    # ser original values of v and m
                    v = 12
                    m = 1
            # method for getting rect for dinosaur and cactus

            score.change_score(dinosaur.x + dinosaur.WIDTH, cactus.x, cactus.y, dinosaur.y + dinosaur.HEIGHT,
                               dinosaur.x,
                               cactus.x + cactus.WIDTH)
            cactus.move(Cactus.moving)
            self.screen.fill(background)
            self.screen.blit(score.score(), (score.x, score.y))
            # pygame.draw.rect(self.screen, self.COLORS["GROUND"], [0, cactus.y, App().WIDTH, 5])
            pygame.draw.rect(self.screen, self.COLORS['GROUND'], [ground.X, ground.Y, ground.WIDTH, ground.HEIGHT])

            # bliting the dinosaur
            if dinosaur.isJumping:
                self.screen.blit(Dinosaur.dino_jump[dinosaur.walkCount // 8], (dinosaur.x, dinosaur.y))
            elif not score.change_score(dinosaur.x + dinosaur.WIDTH, cactus.x, cactus.y, dinosaur.y + dinosaur.HEIGHT,
                                        dinosaur.x,
                                        cactus.x + cactus.WIDTH):
                self.screen.blit(Dinosaur.dino_die[dinosaur.walkCount // 8], (dinosaur.x, dinosaur.y))
            else:
                self.screen.blit(Dinosaur.dino_run[dinosaur.walkCount // 8], (dinosaur.x, dinosaur.y))
            dinosaur.walkCount += 1
            if dinosaur.walkCount + 1 > 64:
                dinosaur.walkCount = 0

            pygame.draw.rect(self.screen, self.COLORS["CACTUS_COLOR"], [cactus.x, cactus.y, cactus.WIDTH,
                                                                        cactus.HEIGHT], 5)
            pygame.time.delay(2)
            pygame.display.update()

        # close application correctly
        pygame.quit()


if __name__ == '__main__':
    App().mainloop()
