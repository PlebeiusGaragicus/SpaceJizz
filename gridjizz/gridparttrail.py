from random import randint, uniform
from math import sin, cos, pi, sqrt

# Import BRL.Random
# Import BRL.FileSystem

from colordefs import *
from utils import *
from images import *


debug: int = 0

moiAkt: float = 0.0
moiAkt2: float = 0.0

numgridstyles: int = 20
windowed: bool = False
MAXPARTICLES: int = 50000
MAXPARTICLELIFE: int = 80
numparticles: int = 2048
particlelife: int = 40
gravityparticles: int = 1
particledecay: float = .95
particlestyle: int = 0
numparticlestyles: int = 3  #0,1,2,3
g_red: int = 32
g_green: int = 80
g_blue: int = 200
g_opacity: float = 0.85

fullgrid: bool = True

showstars: int = 300
MAXSTARS: int = 10000

slotcount: int #0 to numparticles-1

partarray:part[]
partarray = New part[MAXPARTICLES+1]

starx: int[MAXSTARS+1]
stary: int[MAXSTARS+1]
stard: float[MAXSTARS+1]

part_LIST:TList = New TList
trail_LIST:TList = New TList
gwlow: int
gwhi: int
ghlow: int
ghhi: int
gxoff: int
gyoff: int

scroll: bool = False
# screensize: int = 0 # INDEX INTO GFXMODEARR
screensizew: int = 1024
screensizeh: int = 768
# playsize: int = 0 # INDEX INTO PLAYFIELDSIZES
playsizew: int = 1024
playsizeh: int = 768
gridsize: int = 2
SCREENW: int = 1024
SCREENH: int = 768
PLAYFIELDW: int = 1024 #1280  #2^8*5
PLAYFIELDH: int = 768 #1024  #2^8*2*2
GRIDWIDTH: int = 16   #4,5,8,10,16,20,32,40,64
GRIDHEIGHT: int = 16  #4,8,16,32,64,128,256

GRIDHILIGHT: int = 4

NUMGPOINTSW: int = PLAYFIELDW / GRIDWIDTH # //?
NUMGPOINTSH: int = PLAYFIELDH / GRIDHEIGHT # //?

grid:gridpoint[,]
grid = New gridpoint[5120/4+2, 4096/4+2] # maximum size

a: int
b: int
# for a = 0 To 1920/4
for a in range(480):
	for b in range(300):
		grid[a,b] = New gridpoint



def SetUp() -> int:
	ret: bool = True

	gridpoint.ResetAll()

	LoadImages()

	if PLAYFIELDW > SCREENW Or PLAYFIELDH > SCREENH:
		scroll = True
	gxoff = 0
	gyoff = 0

	capturedimg:TImage = CreateImage(SCREENW,SCREENH)
	SetLineWidth 2
	glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

	CreateStars()

	return ret



def CreateStars():
	for t in range(MAXSTARS):
		starx[t] = randint(-100, max(PLAYFIELDW,SCREENW)+100)
		stary[t] = randint(-100, max(PLAYFIELDH,SCREENH)+100)
		stard[t] = 2 + float(t % 8)/4


def DrawStars():
	if showstars > 0:
		SetBlend lightblend
		SetScale 2,2
		SetAlpha .8
		SetLineWidth 2.0

		for t in showstars:
			SetColor 480/stard[t],480/stard[t],480/stard[t]
			DrawRect starx[t]-gxoff/stard[t],stary[t]-gyoff/stard[t],1,1

		SetAlpha 1
		SetScale 1,1
