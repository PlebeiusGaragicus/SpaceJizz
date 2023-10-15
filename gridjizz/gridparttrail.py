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
particledecay# = .95
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
screensize: int = 0
screensizew: int = 1024
screensizeh: int = 768
playsize: int = 0
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


class gfxmode:
	Field w: int
	Field h: int
	Field desc$
	Field s$


gfxmodearr = gfxmode[100]
numgfxmodes: int = 0

playfieldsizes = [
	1024,768,
	512,384,
	640,480,
	720,400,
	720,480,
	720,576,
	800,600,
	1024,720,
	1024,768,
	1152,864,
	1152,870,
	1280,720,
	1280,768,
	1280,800,
	1280,854,
	1280,960,
	1280,1024,
	1440,900,
	1400,1050,
	1600,1024,
	1600,1200,
	1600,1280,
	1680,1050,
	1800,1440,
	1920,1080,
	1920,1200,
	2048,768,
	2048,1536,
	2560,1024,
	2560,1600,
	2560,2048,
	3200,2048,
	3200,2400,
	3840,2400,
	5120,4096
]
numplayfieldsizes: int = 34   #0-33

DefData "USER",   1024, 768
DefData "BWMac",  512,  384
DefData "VGA",	640,  480
DefData "????",   720,  400
DefData "NTSCDVD",720,  480
DefData "PALDVD", 720,  576
DefData "SVGA",   800,  600
DefData "XGA-",   1024, 720
DefData "XGA",	1024, 768
DefData "XGA+",   1152, 864
DefData "XGA++",  1152, 870
DefData "720p",   1280, 720
DefData "WXGA",   1280, 768
DefData "WXGA+" , 1280, 800
DefData "WXGA++" , 1280, 854
DefData "WXGA+++", 1280, 960
DefData "SXGA",   1280, 1024
DefData "WSXGA",  1440, 900
DefData "SXGA+",  1400, 1050
DefData "WSXGA",  1600, 1024
DefData "UXGA",   1600, 1200
DefData "UXGA+",  1600, 1280
DefData "WSXGA+", 1680, 1050
DefData "?????",  1800, 1440
DefData "1080p",  1920, 1080
DefData "WUXGA",  1920, 1200
DefData "DUALW",  2048, 768
DefData "QXGA",   2048, 1536
DefData "DUALW+", 2560, 1024
DefData "WQXGA",  2560, 1600
DefData "QSXGA",  2560, 2048
DefData "WQSXGA", 3200, 2048
DefData "QUXGA",  3200, 2400
DefData "WQUXGA", 3840, 2400
DefData "HSXGA",  5120, 4096

numgfxmodes: int = 34  # 0-33



def GetGfxModes():
	Local desc$,w: int,h: int

	for Local cnt: int = 0 To numgfxmodes:
		Local g:gfxmode = New gfxmode
		ReadData desc$,w,h
		g.w = w
		g.h = h
		g.desc$ = desc$
		g.s$ = g.w+"X"+g.h
		gfxmodearr[cnt] = g

	 #  set first entry to what the user has in config
	gfxmodearr[0].w = screensizew
	gfxmodearr[0].h = screensizeh




def FindSetting():

	screensize = 0  #  pick first one
	playsize = 0  #  use the defaul/file settings
	playfieldsizes[0] = playsizew
	playfieldsizes[1] = playsizeh

	for Local t = 0 To numgfxmodes
		 #  or find the one that matches file
		if gfxmodearr[t].w = screensizew And gfxmodearr[t].h = screensizeh
			screensize = t




def SetDimensions():

	SCREENW = gfxmodearr[screensize].w
	SCREENH = gfxmodearr[screensize].h

	PLAYFIELDW = playfieldsizes[playsize*2]
	PLAYFIELDH = playfieldsizes[playsize*2+1]

	screensizew = gfxmodearr[screensize].w
	screensizeh = gfxmodearr[screensize].h

	playsizew = PLAYFIELDW
	playsizeh = PLAYFIELDH



def SetUp() -> int:

	Local ret: int = True

	SetDimensions()

	if windowed
		if GraphicsModeExists( SCREENW,SCREENH )
			Graphics(SCREENW, SCREENH, 0)
		else:
			Local fh:TStream = WriteFile("errors.txt")
			WriteLine(fh,"Can not set graphics mode: Windowed - "+SCREENW+"X"+SCREENH)
			CloseFile fh
			ret = False

	else:
		Local sucess: bool = False
		for Local dep: int = 32 To 16 Step -8
			if GraphicsModeExists( SCREENW,SCREENH,dep)
				Graphics(SCREENW, SCREENH, dep, 60)
				sucess = True
				Exit


		if not sucess:
			Local fh:TStream = WriteFile("errors.txt")
			WriteLine(fh,"Could not set graphics mode: Fullscreen - "+SCREENW+"X"+SCREENH)
			CloseFile fh
			ret = False



	if ret == True:
		Select gridsize
			Case 0
				GRIDWIDTH = 4
				GRIDHEIGHT = 4
			Case 1
				GRIDWIDTH = 8
				GRIDHEIGHT = 8
			Case 2
				GRIDWIDTH = 16
				GRIDHEIGHT = 16
			Case 3
				GRIDWIDTH = 32
				GRIDHEIGHT = 32


		NUMGPOINTSW = PLAYFIELDW/GRIDWIDTH
		NUMGPOINTSH = PLAYFIELDH/GRIDHEIGHT
		gridpoint.ResetAll()

		LoadImages()
		if PLAYFIELDW > SCREENW Or PLAYFIELDH > SCREENH Then scroll = True
 # 		if PLAYFIELDW <= SCREENW And PLAYFIELDH <= SCREENH Then scroll = False
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
