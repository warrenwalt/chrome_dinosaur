import pygame


class Dinosaur:
    """:except
        This will be the player. The dinosaur will be moving forward
        as it jumps cactus, in an attempt to reach the highest score possible
        scores are awarded when dinosaur successfully jumps over a cactus without touching the cactus.
    """

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
        bot_up_dist = din_bottom-cact_top
        left_right_dist = din_right-cact_left
        if din_left < cact_left and din_right > cact_right:  #
            # check first if its directly below cactus
            if bot_up_dist == 0:  # check if top of cactus and bottom of dinosaur have touched.
                print("Game Over: top and bottom touched.")
        elif left_right_dist == 0 and din_bottom > cact_top:  # check if right side of dinosaur has collided with
            # left-side of cactus
            print("Game Over: sides Touched.")
        else:
            self.text = str(int(self.text) + 5)
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
        self.dimension()
        score = Score(900, 20)
        ground = Ground()
        cactus = Cactus(300, 428)
        dinosaur = Dinosaur(550, 400)
        background = Background().current
        while self.isGaming:
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

            score.change_score(dinosaur.x+dinosaur.WIDTH, cactus.x, cactus.y, dinosaur.y+dinosaur.HEIGHT, dinosaur.x,
                               cactus.x+cactus.WIDTH)
            cactus.move(10)
            pygame.time.delay(15)
            self.screen.fill(background)
            self.screen.blit(score.score(), (score.x, score.y))
            # pygame.draw.rect(self.screen, self.COLORS["GROUND"], [0, cactus.y, App().WIDTH, 5])
            pygame.draw.rect(self.screen, self.COLORS['GROUND'], [ground.X, ground.Y, ground.WIDTH, ground.HEIGHT])
            pygame.draw.rect(self.screen, self.COLORS['BORDER_OF_OBJECT'], [dinosaur.x, dinosaur.y, dinosaur.WIDTH,
                                                                            dinosaur.HEIGHT], 6)
            pygame.draw.rect(self.screen, self.COLORS["CACTUS_COLOR"], [cactus.x, cactus.y, cactus.WIDTH,
                                                                        cactus.HEIGHT], 5)
            pygame.display.update()

        # close application correctly
        pygame.quit()


if __name__ == '__main__':
    App().mainloop()
