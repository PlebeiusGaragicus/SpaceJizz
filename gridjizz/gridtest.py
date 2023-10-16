# Framework BRL.GLMax2D

from colordefs import *
from gridparttrail import *

SetGraphicsDriver GLMax2DDriver()
Graphics 1024,768,0


sz: float = 64
amnt = 10


playsizew = 1024
playsizeh = 768
screensizew = 1024
screensizeh = 768
windowed = True

# GetGfxModes()
FindSetting()
SetUp()

Local pat:Int = 0

while not KeyDown(KEY_ESCAPE):

	Cls

	if MouseDown(1):
		gridpoint.Pull(MouseX()+gxoff,MouseY()+gyoff,sz,amnt)


	if MouseDown(2):
		gridpoint.Push(MouseX()+gxoff,MouseY()+gyoff,sz,amnt/4)

	if MouseHit(3):
		pat = (pat + 1) % 21

	tim = time()

	gridpoint.UpdateGrid()
	gridpoint.DrawGrid(pat)
	SetColor COL_BORDER_R,COL_BORDER_G,COL_BORDER_B
	SetLineWidth(2.0)
	DrawLine -gxoff,-gyoff,PLAYFIELDW-1-gxoff,-gyoff
	DrawLine -gxoff,-gyoff,-gxoff,PLAYFIELDH-1-gyoff
	DrawLine -gxoff,PLAYFIELDH-1-gyoff,PLAYFIELDW-1-gxoff,PLAYFIELDH-1-gyoff
	DrawLine PLAYFIELDW-1-gxoff,PLAYFIELDH-1-gyoff,PLAYFIELDW-1-gxoff,-gyoff

	if MouseX() < 100:
		gxoff:-10
		if gxoff < -100
			gxoff = -100


	if MouseY() < 100:
		gyoff:-10
		if gyoff < -100
			gyoff = -100


	if MouseX() > 1024-100:
		gxoff:+10
		if gxoff > PLAYFIELDW-1024+100
			gxoff = PLAYFIELDW-1024+100


	if MouseY() > 768-100:
		gyoff:+10
		if gyoff > PLAYFIELDH-768+100
			gyoff = PLAYFIELDH-768+100



	Flip
	tim = time() - tim
	if tim < 20 and tim > 0:
		# Delay 20-tim
		sleep(20-tim)
