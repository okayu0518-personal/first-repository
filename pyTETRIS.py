import random
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
AQUA = (0, 255, 255)
ORANGE = (255, 100, 0)

colorarray = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
              (0, 0, 0), (255, 255, 0), (255, 0, 255),
              (0, 255, 255), (255, 100, 0)]


windowsize_x = 300
windowsize_y = 500

pygame.init()
pygame.display.set_caption("pyTETRIS")
SCREEN = pygame.display.set_mode((windowsize_x, windowsize_y))

font1 = pygame.font.SysFont(None, 70)
font2 = pygame.font.SysFont(None, 50)
smallfont = pygame.font.SysFont(None, 20)

fpsclock = pygame.time.Clock()

num = 0
currentmino = [1]
minonum = 0
changex = 0
changey = 0
gravity = 1
blocksize = 20  # マス目のサイズ
rotate = False  # 回転させるか
state = 0  # 回転の回数
pressflag = False  # 回転止めるよう
arrowpressflag = False  # 矢印用
downpressflag = False
arrowtime = 0
gameoverflg = False
time_gameover = 0
score = 0
time = pygame.time.get_ticks()


class class_mino(pygame.sprite.Sprite):
    # コンストラクタ
    def __init__(
            self,
            minonum,
            x,
            y,
            blocksize,
            stagestartx,
            stagestarty,
            stageendx,
            stageendy):
        pygame.sprite.Sprite.__init__(self)

        # self.block=[][]      #いくつめのブロックか[　[x,y]]
        self.block = [[0 for j in range(2)] for i in range(4)]
        self.minonum = minonum
        self.x = x
        self.y = y
        self.stagestartx = stagestartx
        self.stagestarty = stagestarty
        self.stageendx = stageendx
        self.stageendy = stageendy
        self.blocksize = blocksize

    def setshape(self, fillgrid):  # 操作用ミノ初期化

        self.fillgrid = fillgrid

        if self.minonum == 0:  # I
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize * 2
            self.block[2][1] = self.y
            self.block[3][0] = self.x + self.blocksize * 3
            self.block[3][1] = self.y

        if self.minonum == 1:  # o
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y
            self.block[3][0] = self.x + self.blocksize
            self.block[3][1] = self.y + self.blocksize

        if self.minonum == 2:  # s
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y

        if self.minonum == 3:  # z
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if self.minonum == 4:  # J
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if self.minonum == 5:  # L
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize * 2
            self.block[2][1] = self.y
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if self.minonum == 6:  # T
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

    def figure(  # 操作
            self,
            changex,
            changey,
            rotate,
            state
    ):

        if rotate:
            if self.minonum == 0:  # I
                if(state % 2 == 1):  # 初回
                    self.block[0][0] += self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0] -= self.blocksize
                    self.block[2][1] += self.blocksize
                    self.block[3][0] -= self.blocksize * 2
                    self.block[3][1] += self.blocksize * 2
                elif(state % 2 == 0):
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0] += self.blocksize
                    self.block[2][1] -= self.blocksize
                    self.block[3][0] += self.blocksize * 2
                    self.block[3][1] -= self.blocksize * 2

            if self.minonum == 1:  # o 回さない
                pass
            if self.minonum == 2:  # s
                if(state % 2 == 1):  # 初回
                    self.block[0][0] += self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0] += self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0]
                    self.block[3][1] += self.blocksize * 2
                elif(state % 2 == 0):
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0]
                    self.block[3][1] -= self.blocksize * 2

            if self.minonum == 3:  # z
                if(state % 2 == 1):  # 初回
                    self.block[0][0] += self.blocksize * 2
                    self.block[0][1]
                    self.block[1][0] += self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] += self.blocksize
                elif(state % 2 == 0):
                    self.block[0][0] -= self.blocksize * 2
                    self.block[0][1]
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] -= self.blocksize

            if self.minonum == 4:  # J
                if(state == 1):  # 初回
                    self.block[0][0] += self.blocksize * 2
                    self.block[0][1]
                    self.block[1][0] += self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] += self.blocksize
                elif(state == 2):
                    self.block[0][0]
                    self.block[0][1] += self.blocksize * 2
                    self.block[1][0] += self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 3:
                    self.block[0][0] -= self.blocksize * 2
                    self.block[0][1]
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 0:
                    self.block[0][0]
                    self.block[0][1] -= self.blocksize * 2
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] += self.blocksize

            if self.minonum == 5:  # L
                if(state == 1):  # 初回
                    self.block[0][0] += self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0]
                    self.block[2][1] += self.blocksize * 2
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] += self.blocksize
                elif(state == 2):
                    self.block[0][0] += self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0] -= self.blocksize * 2
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 3:
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0]
                    self.block[2][1] -= self.blocksize * 2
                    self.block[3][0] += self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 0:
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0]
                    self.block[1][1]
                    self.block[2][0] += self.blocksize * 2
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] += self.blocksize

            if self.minonum == 6:  # T
                if(state == 1):  # 初回
                    self.block[0][0] += self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0] += self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] += self.blocksize
                elif(state == 2):
                    self.block[0][0] += self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] += self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] -= self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 3:
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] += self.blocksize
                    self.block[1][0] -= self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] -= self.blocksize
                elif state == 0:
                    self.block[0][0] -= self.blocksize
                    self.block[0][1] -= self.blocksize
                    self.block[1][0] += self.blocksize
                    self.block[1][1] -= self.blocksize
                    self.block[2][0]
                    self.block[2][1]
                    self.block[3][0] += self.blocksize
                    self.block[3][1] += self.blocksize

        for i in range(4):  # 移動量
            self.block[i][0] += changex
            self.block[i][1] += changey

        changeflg = False

        for k in range(2):  # 場外の補正　　　　　たまに抜けれてxが11になってindexerrorがでるため二回回す
            for i in range(4):
                while self.block[i][0] + self.blocksize > self.stageendx:
                    for j in range(4):
                        self.block[j][0] -= self.blocksize
                        changeflg = True

                while self.block[i][0] < self.stagestartx:
                    for j in range(4):
                        self.block[j][0] += self.blocksize
                        changeflg = True

                while self.block[i][1] + self.blocksize > self.stageendy:
                    for j in range(4):
                        self.block[j][1] -= self.blocksize
                        changeflg = True

        if changeflg:
            return

        block = [(2) for i in range(4)]  # ほかのブロックとの衝突停止判定
        block[0] = (int(self.block[0][0] / 20),
                    int(self.block[0][1] / 20))
        block[1] = (int(self.block[1][0] / 20),
                    int(self.block[1][1] / 20))
        block[2] = (int(self.block[2][0] / 20),
                    int(self.block[2][1] / 20))
        block[3] = (int(self.block[3][0] / 20),
                    int(self.block[3][1] / 20))

        for i in range(4):
            x = block[i][0]
            y = block[i][1]

            if self.fillgrid[x][y] == 1 and changex != 0:
                for j in range(4):
                    # print("left")
                    self.block[j][0] -= changex
                    changeflg = True
            if changeflg:
                break

    def show(self):  # ミノ操作中描写
        block = [(4) for i in range(4)]
        block[0] = (self.block[0][0], self.block[0][1],
                    self.blocksize, self.blocksize)
        block[1] = (self.block[1][0], self.block[1][1],  #
                    self.blocksize, self.blocksize)
        block[2] = (self.block[2][0], self.block[2][1],
                    self.blocksize, self.blocksize)
        block[3] = (self.block[3][0], self.block[3][1],
                    self.blocksize, self.blocksize)

        if self.minonum == 0:
            self.color = AQUA
        elif self.minonum == 1:
            self.color = YELLOW
        elif self.minonum == 2:
            self.color = GREEN
        elif self.minonum == 3:
            self.color = RED
        elif self.minonum == 4:
            self.color = BLUE
        elif self.minonum == 5:
            self.color = ORANGE
        elif self.minonum == 6:
            self.color = PURPLE

        for i in range(4):
            pygame.draw.rect(SCREEN, self.color, block[i])
            # print(state)

    def minostop(self):  # ストップ判定

        block = [(2) for i in range(4)]  # ほかのブロックとの衝突停止判定
        block[0] = (int(self.block[0][0] / 20), int(self.block[0][1] / 20))
        block[1] = (int(self.block[1][0] / 20), int(self.block[1][1] / 20))
        block[2] = (int(self.block[2][0] / 20), int(self.block[2][1] / 20))
        block[3] = (int(self.block[3][0] / 20), int(self.block[3][1] / 20))

        for i in range(4):
            x = block[i][0]
            y = block[i][1]
            if self.fillgrid[x][y] == 1:
                # print(block)
                return 2
                break

            elif self.block[i][1] + self.blocksize >= self.stageendy:
                return 1
                break
        # for i in range(4):  # ステージ下停止判定

    def freeze(self):  # 停止したブロックのドロー
        block = [(4) for i in range(4)]
        block[0] = (self.block[0][0], self.block[0][1],
                    self.blocksize, self.blocksize)
        block[1] = (self.block[1][0], self.block[1][1],  #
                    self.blocksize, self.blocksize)
        block[2] = (self.block[2][0], self.block[2][1],
                    self.blocksize, self.blocksize)
        block[3] = (self.block[3][0], self.block[3][1],
                    self.blocksize, self.blocksize)

        stageblock = [(2) for i in range(4)]
        stageblock[0] = (self.block[0][0], self.block[0][1])
        stageblock[1] = (self.block[1][0], self.block[1][1])
        stageblock[2] = (self.block[2][0], self.block[2][1])
        stageblock[3] = (self.block[3][0], self.block[3][1])

        for i in range(4):
            pygame.draw.rect(SCREEN, self.color, block[i])

        return stageblock


class class_stage(pygame.sprite.Sprite):
    def __init__(
            self,
            stagestartx,
            stagestarty,
            stageendx,
            stageendy,
            blocksize):
        pygame.sprite.Sprite.__init__(self)
        self.stagestartx = stagestartx
        self.stagestarty = stagestarty
        self.stageendx = stageendx
        self.stageendy = stageendy
        self.blocksize = blocksize
        self.stagecolor = 0

        self.stagegrid = [[0 for i in range(21)]for j in range(11)]

    def fillgrid(self, xandy):  # ステージの10化
        block = [(2) for i in range(4)]
        block[0] = (int(xandy[0][0] / 20), int(xandy[0][1] / 20))
        block[1] = (int(xandy[1][0] / 20), int(xandy[1][1] / 20))
        block[2] = (int(xandy[2][0] / 20), int(xandy[2][1] / 20))
        block[3] = (int(xandy[3][0] / 20), int(xandy[3][1] / 20))

        for i in range(4):
            x = block[i][0]
            y = block[i][1]

            self.stagegrid[x][y] = 1
        print(self.stagegrid)

        return self.stagegrid
        # self.stagegrid[block[i][0][block[i][1]] = 1

    def clear(self):
        lineflg = False

        for i in range(20, 0, -1):
            lineflg = True
            for j in range(1, 11):
                if self.stagegrid[j][i] != 1:
                    lineflg = False
                    break
            if lineflg:
                for l in range(i, 0, -1):
                    for k in range(1, 11):
                        #self.stagegrid[k][i] = 0
                        self.stagegrid[k][l] = self.stagegrid[k][l - 1]

                '''self.stagecolor += 1
                if self.stagecolor > 7:
                    self.stagecolor = 0'''
                return 1
            print(self.stagecolor)

    def remainshow(self):
        block = [(4) for i in range(200)]
        for i in range(11):
            for j in range(21):
                if self.stagegrid[i][j] == 1:
                    block[i] = (i * self.blocksize, j * self.blocksize,
                                self.blocksize, self.blocksize)

                    pygame.draw.rect(SCREEN, BLACK, block[i])

    def show(self, gridcolor):  # ステージ描写
        points = [
            (self.stagestartx - 10,
             self.stagestarty - 10),
            (self.stagestartx - 10,
             self.stageendy + 10),
            (self.stageendx + 10,
             self.stageendy + 10),
            (self.stageendx + 10,
             self.stagestarty - 10)]
        pygame.draw.lines(SCREEN, BLACK, True, points, 13)

        gridcolor = list(gridcolor)
        for parameter in range(len(gridcolor)):
            if gridcolor[parameter] > 0:
                gridcolor[parameter] /= 2
        for i in range(21):
            for j in range(11):
                block = [
                    (self.stagestartx,
                     self.stagestarty),
                    (self.stagestartx,
                     self.stagestarty + self.blocksize * i),
                    (self.stagestartx + self.blocksize * j,
                     self.stagestarty + self.blocksize * i),
                    (self.stagestartx + self.blocksize * j,
                        self.stagestarty)]
                pygame.draw.lines(
                    SCREEN, gridcolor, True, block, 2)

    def gameover(self):
        for i in range(11):
            if self.stagegrid[i][1] == 1:

                text1 = font1.render("GAME", True, (200, 20, 50))
                text2 = font1.render("OVER", True, (200, 20, 50))
                backtext1 = font1.render("GAME", True, BLACK)
                backtext2 = font1.render("OVER", True, BLACK)
                SCREEN.blit(text1,
                            [int((self.stageendx - 80) / 2),
                             int((self.stageendy - 100) / 2)])
                SCREEN.blit(text2,
                            [int((self.stageendx - 80) / 2),
                             int((self.stageendy - 20) / 2)])
                SCREEN.blit(backtext1,
                            [int((self.stageendx - 90) / 2),
                             int((self.stageendy - 110) / 2)])
                SCREEN.blit(backtext2,
                            [int((self.stageendx - 90) / 2),
                             int((self.stageendy - 30) / 2)])

                return 1
                break


class class_UI(pygame.sprite.Sprite):
    def __init__(self, scorex, scorey, nextx, nexty, blocksize=20):
        pygame.sprite.Sprite.__init__(self)
        self.scorex = scorex
        self.scorey = scorey
        self.nextx = nextx
        self.nexty = nexty
        self.blocksize = blocksize - 10
        self.x = nextx + 5
        self.y = nexty + 30
        self.block = [[j for j in range(2)] for i in range(4)]

    def show(self, nextmino, score):
        score = font2.render(str(score), True, (0, 0, 0))
        nexttext = smallfont.render("NEXT", True, WHITE)
        nexttextshadow = smallfont.render("NEXT", True, BLACK)
        SCREEN.blit(score, [self.scorex, self.scorey])
        SCREEN.blit(nexttextshadow, [self.nextx + 1, self.nexty + 1])
        SCREEN.blit(nexttext, [self.nextx, self.nexty])

        nextwindow = [self.x - 5,
                      self.y - 5,
                      int(self.blocksize * 4.5),
                      int(self.blocksize * 6)]
        pygame.draw.rect(SCREEN, BLACK, nextwindow)
        nextwindow = [self.x - 10,
                      self.y - 10,
                      int(self.blocksize * 4.5),
                      int(self.blocksize * 6)]
        pygame.draw.rect(SCREEN, WHITE, nextwindow)

        if nextmino == 0:  # I
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x
            self.block[2][1] = self.y + self.blocksize * 2
            self.block[3][0] = self.x
            self.block[3][1] = self.y + self.blocksize * 3

        if nextmino == 1:  # o
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y
            self.block[3][0] = self.x + self.blocksize
            self.block[3][1] = self.y + self.blocksize

        if nextmino == 2:  # s
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y

        if nextmino == 3:  # z
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if nextmino == 4:  # J
            self.block[0][0] = self.x
            self.block[0][1] = self.y
            self.block[1][0] = self.x
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if nextmino == 5:  # L
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y + self.blocksize
            self.block[2][0] = self.x + self.blocksize * 2
            self.block[2][1] = self.y
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        if nextmino == 6:  # T
            self.block[0][0] = self.x
            self.block[0][1] = self.y + self.blocksize
            self.block[1][0] = self.x + self.blocksize
            self.block[1][1] = self.y
            self.block[2][0] = self.x + self.blocksize
            self.block[2][1] = self.y + self.blocksize
            self.block[3][0] = self.x + self.blocksize * 2
            self.block[3][1] = self.y + self.blocksize

        block = [(4) for i in range(4)]
        block[0] = (self.block[0][0], self.block[0][1],
                    self.blocksize, self.blocksize)
        block[1] = (self.block[1][0], self.block[1][1],  #
                    self.blocksize, self.blocksize)
        block[2] = (self.block[2][0], self.block[2][1],
                    self.blocksize, self.blocksize)
        block[3] = (self.block[3][0], self.block[3][1],
                    self.blocksize, self.blocksize)

        if nextmino == 0:
            self.color = AQUA
        elif nextmino == 1:
            self.color = YELLOW
        elif nextmino == 2:
            self.color = GREEN
        elif nextmino == 3:
            self.color = RED
        elif nextmino == 4:
            self.color = BLUE
        elif nextmino == 5:
            self.color = ORANGE
        elif nextmino == 6:
            self.color = PURPLE

        for i in range(4):
            pygame.draw.rect(SCREEN, self.color, block[i])


def main():
    global currentmino
    global num
    global minonum
    global changex
    global changey
    global rotate
    global state
    global pressflag
    global arrowpressflag
    global downpressflag
    global arrowtime
    global gameoverflg
    global time_gameover
    global time
    global score
    gameflag = 0  # ゲーム自体の終了用
    stagestartx = 20  # ステージの左上
    stagestarty = 20
    stageendx = stagestartx + 200  # ステージの右下
    stageendy = stagestarty + 400

    stage = class_stage(  # ステージクラス
        stagestartx,
        stagestarty,
        stageendx,
        stageendy,
        blocksize)

    UI = class_UI(30, 450, 250, 20, blocksize)

    freezedblock = [(2) for i in range(4)]  # 止まった時の座標入れ
    fillgrid = [[0 for i in range(21)] for j in range(11)]  # ゲーム中のブロック10データ

    backgroundcolor = (190, 190, 200)

    minoset = [i for i in range(7)]
    random.shuffle(minoset)

    minostartposx = 100  # 落下開始位置
    minostartposy = 20
    currentmino[num] = class_mino(  # ミノクラス
        minoset[minonum],
        minostartposx,
        minostartposy,
        blocksize,
        stagestartx,
        stagestarty,
        stageendx,
        stageendy)

    currentmino[num].setshape(fillgrid)  # ミノ生成

    while gameflag == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameflag = 1

        SCREEN.fill(backgroundcolor)  # 背景

        if pygame.time.get_ticks() - time > 800:  # 落下一コマずつ
            gravity = blocksize
            time = pygame.time.get_ticks()
        else:
            gravity = 0

        # for oldminonum in range(len(currentmino) - 1):  # 落下済みのミノ描写
            # currentmino[oldminonum].freeze()
        if currentmino[num].minostop() == 1:  # 底まで落下if
            minonum += 1
            if minonum >= 7:
                minonum = 0
                random.shuffle(minoset)
            currentmino.append(
                class_mino(
                    minoset[minonum],
                    minostartposx,
                    minostartposy,
                    blocksize,
                    stagestartx,
                    stagestarty,
                    stageendx,
                    stageendy))
            freezedblock = currentmino[num].freeze()
            # print(freezedblock)
            fillgrid = stage.fillgrid(freezedblock)
            num += 1
            state = 0
            currentmino[num].setshape(fillgrid)
            downpressflag = False

        if currentmino[num].minostop() == 2:  # ミノで停止if

            minonum += 1
            if minonum >= 7:
                minonum = 0
                random.shuffle(minoset)
            currentmino.append(
                class_mino(
                    minoset[minonum],
                    minostartposx,
                    minostartposy,
                    blocksize,
                    stagestartx,
                    stagestarty,
                    stageendx,
                    stageendy))
            currentmino[num].figure(0, -blocksize, False, state)
            currentmino[num].show()
            freezedblock = currentmino[num].freeze()
            fillgrid = stage.fillgrid(freezedblock)
            num += 1
            state = 0
            currentmino[num].setshape(fillgrid)
            downpressflag = False

        # if pygame.time.get_ticks()-time_freeze>200:

        if stage.clear() == 1:
            score += 1000
        stage.remainshow()
        if stage.gameover() == 1:
            
            if not gameoverflg:
                time_gameover = pygame.time.get_ticks()
                gameoverflg = True
                backgroundcolor = (180, 10, 5)

            if not pygame.time.get_ticks() - time_gameover >= 2000:
                currentmino[num].show()  # 操作中ミノ描写
                stage.show(currentmino[num].color)  # ステージ描写
                if minonum >= 6:
                    minonum = 0
                    random.shuffle(minoset)
                UI.show(minoset[minonum + 1], score)
            if pygame.time.get_ticks() - time_gameover >= 2000:
                if score>=0:
                    score -= 5
                if score < 0:
                    break

        currentmino[num].figure(
            changex,
            gravity + changey,
            rotate,
            state)  # 操作中ミノ移動&回転

        currentmino[num].show()  # 操作中ミノ描写
        stage.show(currentmino[num].color)  # ステージ描写
        if minonum >= 6:
            minonum = 0
            random.shuffle(minoset)
        UI.show(minoset[minonum + 1], score)

        press = pygame.key.get_pressed()  # キー操作受付
        rotate = False
        if((press[pygame.K_LSHIFT] or press[pygame.K_RSHIFT]) and pressflag is False):
            pressflag = True
            state += 1
            rotate = True

        if(not press[pygame.K_LSHIFT] and not press[pygame.K_RSHIFT]):
            pressflag = False
            rotate = False

        if(state >= 4):
            state = 0

        xspeed = 20
        yspeed = 20
        changex = changey = 0
        if(press[pygame.K_RIGHT] and arrowpressflag is False):
            changex = xspeed
            arrowpressflag = True
            arrowtime = pygame.time.get_ticks()
        if(press[pygame.K_LEFT] and arrowpressflag is False):
            changex = -xspeed
            arrowpressflag = True
            arrowtime = pygame.time.get_ticks()

        if press[pygame.K_LEFT] and pygame.time.get_ticks() - arrowtime > 500:
            changex = -xspeed
        if press[pygame.K_RIGHT] and pygame.time.get_ticks() - arrowtime > 500:
            changex = xspeed
        if((not press[pygame.K_RIGHT] and not press[pygame.K_LEFT])):
            changex = 0
            arrowpressflag = False

        if press[pygame.K_DOWN] and downpressflag is False:
            changey = yspeed
            downpressflag = True
            arrowtime = pygame.time.get_ticks()

        '''if press[pygame.K_UP] and downpressflag is False:
            changey = stageendy - max(
                currentmino[num].block[0][1],
                currentmino[num].block[1][1],
                currentmino[num].block[2][1],
                currentmino[num].block[3][1])
            print(changey)
            downpressflag = True'''

        if press[pygame.K_DOWN] and pygame.time.get_ticks() - arrowtime > 200:
            changey = yspeed
        if(not press[pygame.K_UP] and not press[pygame.K_DOWN]):
            changey = 0
            downpressflag = False

        pygame.display.flip()  # ウィンドウ自体描写
        fpsclock.tick(60)  # フレームレート指定

    pygame.quit()  # 終了


if __name__ == "__main__":
    main()
