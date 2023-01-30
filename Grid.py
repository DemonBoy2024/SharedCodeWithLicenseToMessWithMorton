import pygame, sys
from pygame.locals import QUIT
pygame.init()

WW = 400
WH = 600
CW = WW//20
CH = WH//30
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)


data = open('data.txt', 'r')
data = data.read().split('\n')
dicData = {'Sedimentary Rocks': [], 'Snow/Ice': []}


for i in data:
    if i[0:2] == 'Se':
      lst = [[i[i.index('row') + 5:i.index('and') - 1], i[i.index('column') + 8:]]]
      dicData["Sedimentary Rocks"] += lst
    elif i[0:2] == 'Sn':
      lst = [[i[i.index('row') + 5:i.index('and') - 1], i[i.index('column') + 8:]]]
      dicData["Snow/Ice"] += lst


DISPLAYSURF = pygame.display.set_mode((WW, WH))
DISPLAYSURF.fill(WHITE)


def drawGrid():
    r = 0
    for x in range(0, WH, CH):
        c = 0
        for y in range(0, WW, CW):
            rect = pygame.Rect(y, x, CW, CH)
            if [str(r), str(c)] in dicData['Sedimentary Rocks']:
              pygame.draw.rect(DISPLAYSURF, (0, 0, 255), rect)
            elif [str(r), str(c)] in dicData['Snow/Ice']:
              pygame.draw.rect(DISPLAYSURF, BLACK , rect)
            c = c + 1
        r = r + 1


while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
