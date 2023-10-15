import os
import sys
from time import sleep
from math import sin, cos, sqrt, atan2
from random import randint, uniform

import pygame

from control import *
from images import *
from sound import *
from gridparttrail import *
from colordefs import *
from vectorfont import *


g_v_num = "5.4"
version = "Version " + g_v_num + " - Apr 19, 2006"
advert =  "Visit www.incitti.com for more games."


cheat: bool = False
nokillme: bool = False
valid: bool = True
mxaim: float = 0
myaim: float = 0

px: float = 512
py: float = 384
pr: int = 0
player_shield: int = 0
pscore: int = 0
upgradetime: int = 20
oldmx: float = 0
oldmy: float = 0
gameover : bool = False
dying : bool = False
powerupscore: int = 1
extralifecount: int = 1
extrabombcount: int = 1
lowesthiscore: int = 0
hiscore: int = 0
gcount: int = 0
numshots: int = 1
shottimer: int = 0
shot_back: int = 0
shot_side: int = 0
supershots: int = 0
bouncyshots: int = 0
shotspeed: float = 3
MAXPLAYERSPEED: int = 6.5
killcount: int = 0
multiplier: int = 1

#Global multiplieramount: int[] = [25,50,100,200,400,800,1600,3200,6400,12800]
multiplieramount = [25,100,200,400,800,1600,2500,3500,5000,5500]

speed_nme: float = 1
speed_nme1: float = 1
speed_nme2: float = 1
speed_nme3: float = 1
speed_nme4: float = 1
speed_nme5: float = 1
speed_nme6: float = 1
speed_nme7: float = 1
speed_nme8: float = 1
speed_le: float = 1
sp_x: int = 0
sp_t: int = 0
sp_c: int = 0
sp_x2: int = 0
sp_t2: int = 0
sp_c2: int = 0
sp_x3: int = 0
sp_t3: int = 0
sp_c3: int = 0
sp_x4: int = 0
sp_t4: int = 0
sp_c4: int = 0

letter = []
letter[0] = 32
letter[1] = 32
letter[2] = 32
letter[3] = 32
letter[4] = 32
letter[5] = 32
letter[6] = 32
letter[7] = 32

# top 10 scores, time reached and player names
# TODO I don't think these are correct
# scores = [10+1, 3]
# playtimes = [10+1, 3]
# names = [10+1, 3]
# scoresetting = [10+1, 3]
# checksum = [10+1, 3]

tcounter: int = 0

mess: float = None
messtime: int = 0
mlen: int = None

t: int = None

circ = []
circ.extend([0.0] * 36)

for t in range(0, 18):
	circ[t*2] = cos(t*20)*8
	circ[t*2+1] = sin(t*20)*8

print(circ)


SHOT_LIST = []
nme_LIST = []
nme1_LIST = []
nme2_LIST = []
nme3_LIST = []
nme4_LIST = []
nme5_LIST = []
nme6_LIST = []
nme7_LIST = []
nme8_LIST = []
ge_LIST = []
le_LIST = []
pu_LIST = []
score_list = []







def DoGameOver() -> int:

	Local looper: int = 2
	Local tim: int

	FlushKeys()
	while looper < 360:
		dying = True
		UpdateAll()
		Cls
		tim = MilliSecs()
		drawall()
		# if KeyDown(KEY_TAB): End
		# if not KeyDown(KEY_F8)
		SetColor 0,55+abs(Sin(looper/2))*200,0
		DrawString("GAME OVER", SCREENW/2-abs(Sin(looper/2))*19*5*9*.5, SCREENH/2-abs(Sin(looper/2))*100, abs(Sin(looper/2))*20)

		Flip 1
		tim = MilliSecs() - tim

		if tim < 20 and tim > 0:
			sleep(20-tim)

		if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and controltype = 3 and bombtime = 0)) or (JoyDown(j_d_option,joyport) and controltype = 0 and bombtime = 0):
			if Options(True):
				return True

		if KeyHit(k_bomb) or MouseHit(m_bomb)
			looper = 360

		looper  += 2

	return False






def ShowFriends(f: int = -1) -> int:
	Local counter: int = 0, i: int
	Local tim: int

	FlushKeys()
	bombtime = 20
	Local colr: int[8]
	Local colg: int[8]
	Local colb: int[8]
	Local lsp: int = 50
	Local lwsp: int = 0

	while (counter < 900):
		Cls
		gcount += 1
		tim = MilliSecs()
		if randint(0,100) > 94 and counter < 850:
			part.CreateFireworks(1)

		part.UpdateParticles(1)
		part.DrawParticles()
		BlackholeParticles()

		#red circles
		for n5 in nme5_list:
			n5.UpdateDisplayEffect()


		SetColor 255,255,0
		if (SCREENH<600):
			lsp = 32
			lwsp = 32
		else:
			lsp = 50
			lwsp = 0

		DrawString("Know Your Friends",SCREENW/2-4.5*5*18/2-32,10,4.5)

		CycleColours()
		CycleColours()
		colr[7] = rcol
		colg[7] = gcol
		colb[7] = bcol
		if counter % 4 = 0
			for i= 1 To 7
				colr[i-1] = colr[i]
				colg[i-1] = colg[i]
				colb[i-1] = colb[i]


		if counter > 50:
			SetColor 255,255,255
			SetRotation(counter)
		 	DrawImage whiteplayer,SCREENW/2-200+lwsp,SCREENH/2-lsp*4
			SetRotation(0)
			SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
			DrawString("Your Ship",SCREENW/2-100,SCREENH/2-lsp*4-10,3)
			SetColor 255,255,255

		if counter > 100:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200-lwsp,SCREENH/2-lsp*3,2
			SetBlend LIGHTBLEND
			SetColor colr[0],colg[0],colb[0]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200-lwsp,SCREENH/2-lsp*3
			SetRotation 0
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Temporary Back Shooter",SCREENW/2-100,SCREENH/2-lsp*3-10,3)

		if counter > 150:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200+lwsp,SCREENH/2-lsp*2,3
			SetBlend LIGHTBLEND
			SetColor colr[1],colg[1],colb[1]
			SetRotation(counter*6+45)
			DrawImage whitestar,SCREENW/2-200+lwsp,SCREENH/2-lsp*2
			SetRotation 0
			SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
			DrawString("Temporary Side Shooters",SCREENW/2-100,SCREENH/2-lsp*2-10,3)

		if counter > 200:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200-lwsp,SCREENH/2-lsp,0
			SetBlend LIGHTBLEND
			SetColor colr[2],colg[2],colb[2]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200-lwsp,SCREENH/2-lsp
			SetRotation 0
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Extra Front Shooter",SCREENW/2-100,SCREENH/2-lsp-10,3)

		if counter > 250:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200+lwsp,SCREENH/2,5
			SetBlend LIGHTBLEND
			SetColor colr[3],colg[3],colb[3]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200+lwsp,SCREENH/2
			SetRotation 0
			SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
			DrawString("Extra Shot Speed",SCREENW/2-100,SCREENH/2-10,3)

		if counter > 300:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200-lwsp,SCREENH/2+lsp,6
			SetBlend LIGHTBLEND
			SetColor colr[4],colg[4],colb[4]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200-lwsp,SCREENH/2+lsp
			SetRotation 0
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Extra Player",SCREENW/2-100,SCREENH/2+lsp-10,3)

		if counter > 350:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200+lwsp,SCREENH/2+lsp*2,8
			SetBlend LIGHTBLEND
			SetColor colr[5],colg[5],colb[5]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200+lwsp,SCREENH/2+lsp*2
			SetRotation 0
			SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
			DrawString("Extra Bomb",SCREENW/2-100,SCREENH/2+lsp*2-10,3)

		if counter > 400:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200-lwsp,SCREENH/2+lsp*3,9
			SetBlend LIGHTBLEND
			SetColor colr[6],colg[6],colb[6]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200-lwsp,SCREENH/2+lsp*3
			SetRotation 0
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Temporary Shield",SCREENW/2-100,SCREENH/2+lsp*3-10,3)

		if counter > 450:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200+lwsp,SCREENH/2+lsp*4,7
			SetBlend LIGHTBLEND
			SetColor colr[6],colg[6],colb[6]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200+lwsp,SCREENH/2+lsp*4
			SetRotation 0
			SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
			DrawString("Super Shots",SCREENW/2-100,SCREENH/2+lsp*4-10,3)

		if counter > 500:
			SetAlpha 1
			SetRotation 0
			SetBlend LIGHTBLEND
			SetColor 255,255,255
			DrawImage powerimage,SCREENW/2-200-lwsp,SCREENH/2+lsp*5,10
			SetBlend LIGHTBLEND
			SetColor colr[7],colg[7],colb[7]
			SetRotation(counter*6)
			DrawImage whitestar,SCREENW/2-200-lwsp,SCREENH/2+lsp*5
			SetRotation 0
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Bouncy Shots",SCREENW/2-100,SCREENH/2+lsp*5-10,3)


		SetColor 255,255,0
		if counter % 50 > 25:
			DrawString("Press BOMB Button to Start",SCREENW/2-250,SCREENH-32,4)


#		DrawLine 0,0,SCREENW,0
#		DrawLine 0,0,0,SCREENH
#		DrawLine SCREENW-1,0,SCREENW-1,SCREENH-1
#		DrawLine 0,SCREENH-1,SCREENW-1,SCREENH-1

		Flip 1
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		counter = counter+1
		bombtime = bombtime - 1
		if bombtime < 0:
			bombtime = 0

		if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_option,joyport) and controltype = 0 and bombtime = 0):
			if Options(False):
				return True

		if KeyHit(k_bomb) or MouseHit(m_bomb) or (JoyDown(j_pad_bomb,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_bomb,joyport) and controltype = 0 and bombtime = 0):
			counter = 1000
			playgame = True

	return False






def ShowEnemies(f: int = -1) -> int:
	counter: int = 0
	i: int
	Local tim: int
	Local lsp: int = 50
	Local lwsp: int = 0

	FlushKeys()
	bombtime = 20

	while (counter < 900):
		Cls
		tim = MilliSecs()
		if (SCREENH<600):
			lsp = 32
			lwsp = 32
		else:
			lsp = 50;lwsp = 0

		SetColor 255,0,0
		DrawString("Know Your Enemies",SCREENW/2-4.5*5*18/2-32,10,4.5)

		if counter > 50:
			SetColor 255,255,255
			SetRotation(counter*4)
			DrawImage pinkpinwheel,SCREENW/2-200-lwsp,SCREENH/2-lsp*4
			SetRotation(0)
			SetColor COL_PIN_R,COL_PIN_G,COL_PIN_B
			DrawString("Paul the Pinwheel (25 pts)",SCREENW/2-120,SCREENH/2-lsp*4-10,3)
			SetColor 255,255,255

		if counter > 100:
			Local sc%,scy: float, scx: float
			sc = counter % (256)
			if sc > 127:
				scy = sc-127
				if sc > 127+63:
					scy = 255-sc
				scx = 0
			else:
				scx = sc
				if sc > 63:
					scx = 127-sc
				scy = 0

			SetScale 1+scx/80.0,1+scy/80.0
			DrawImage bluediamond,SCREENW/2-200+lwsp,SCREENH/2-lsp*3
			SetScale 1,1
			SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
			DrawString("Dimmy the Diamond (50 pts)",SCREENW/2-120,SCREENH/2-lsp*3-10,3)
			SetColor 255,255,255

		if counter > 150:
			SetRotation(counter*2)
			DrawImage greensquare,SCREENW/2-200-lwsp,SCREENH/2-lsp*2
			SetRotation(0)
			SetColor COL_SQUARE_R,COL_SQUARE_G,COL_SQUARE_B
			DrawString("Shy the Square (100 pts)",SCREENW/2-120,SCREENH/2-lsp*2-10,3)
			SetColor 255,255,255

		if counter > 200:
			SetRotation(-counter*2.5+90)
			DrawImage purplesquare1,SCREENW/2-200+lwsp,SCREENH/2-lsp
			SetRotation(0)
			SetColor COL_CUBE_R,COL_CUBE_G,COL_CUBE_B
			DrawString("Cubie the Cube (50/100 pts)",SCREENW/2-120,SCREENH/2-lsp-10,3)
			SetColor 255,255,255

		if counter > 250:
			DrawImage bluecircle,SCREENW/2-200-lwsp,SCREENH/2
			SetColor COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B
			DrawString("Sammy the Seeker (10 pts)",SCREENW/2-120,SCREENH/2-10,3)
			SetColor 255,255,255

		if counter > 300:
			SetScale .75+Sin(counter*8)*.25,.75+Sin(counter*8)*.25
			DrawImage redcircle,SCREENW/2-200+lwsp,SCREENH/2+lsp
			SetScale 1,1
			SetColor COL_SUN_R,COL_SUN_G,COL_SUN_B
			DrawString("Dwight the Black Hole (150 pts)",SCREENW/2-120,SCREENH/2+lsp-10,3)
			SetColor 255,255,255

		if counter > 350:
			for Local tt: int = 0 To 23
				SetRotation 90-Cos(tt*30+counter)*20
				if tt == 0:
					DrawImage snakehead,SCREENW/2-200+lwsp+45-tt*13,SCREENH/2+lsp*2+Sin(tt*30+counter)*16
				else:
					DrawImage snaketail,SCREENW/2-200+lwsp+45-tt*13,SCREENH/2+lsp*2+Sin(tt*30+counter)*16,24-tt


			SetRotation 0
			SetColor COL_SNAKE_R,COL_SNAKE_G,COL_SNAKE_B
			DrawString("Selena the Snake (100 pts)",SCREENW/2-120,SCREENH/2+lsp*2-10,3)
			SetColor 255,255,255

		if counter > 400:
			SetRotation(counter)
			DrawImage redclone,SCREENW/2-200-lwsp,SCREENH/2+lsp*3
			SetRotation(0)
			SetColor COL_CLONE_R,COL_CLONE_G,COL_CLONE_B
			DrawString("Ivan the Interceptor (100 pts)",SCREENW/2-120,SCREENH/2+lsp*3-10,3)
			SetColor 255,255,255

		if counter > 450:
			SetRotation(-counter*3)
			DrawImage orangetriangle,SCREENW/2-200+lwsp,SCREENH/2+lsp*4
			SetRotation(0)
			SetColor COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B
			DrawString("Trish the Triangle (150 pts)",SCREENW/2-120,SCREENH/2+lsp*4-10,3)
			SetColor 255,255,255

		if counter > 500:
			SetRotation(counter*4)
			DrawImage indigotriangle,SCREENW/2-200-lwsp,SCREENH/2+lsp*5
			SetRotation(0)
			SetColor COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B
			DrawString("Indy the Butterfly (10 pts)",SCREENW/2-120,SCREENH/2+lsp*5-10,3)
			SetColor 255,255,255


		if randint(0,100) > 94 and counter < 850:
			part.CreateFireworks(1)

		part.UpdateParticles(1)
		part.DrawParticles()
		SetColor 255,255,0
		if counter % 50 > 25:
			DrawString("Press BOMB Button to Start",SCREENW/2-250,SCREENH-32,4)

		Flip 1
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		counter = counter+1
		bombtime -= 1
		if bombtime < 0:
			bombtime = 0

		if KeyHit(KEY_ESCAPE) or \
			(JoyDown(j_pad_option,joyport) and controltype = 3 and bombtime = 0) or \
			(JoyDown(j_d_option,joyport) and controltype = 0 and bombtime = 0):
			if Options(False):
				return True

		if KeyHit(k_bomb) or MouseHit(m_bomb) or \
			(JoyDown(j_pad_bomb,joyport) and controltype = 3 and bombtime = 0) or \
			(JoyDown(j_d_bomb,joyport) and controltype = 0 and bombtime = 0):
			counter = 1000
			playgame = True


	return False




def ShowScores(f: int=-1) -> int:
	Local counter: int = 0, i: int
	Local ptime: str = GetPlayTime$(gcount)
	Local t: int, kol: int
	Local tim: int,s: str,spc: int
	Local d: int

	Local colr: int[10]
	Local colg: int[10]
	Local colb: int[10]

	for i: int = 9 To 0 Step -1:
		CycleColours()
		CycleColours()
		colr[i] = rcol
		colg[i] = gcol
		colb[i] = bcol

	FlushKeys()
	bombtime = 20
	while (counter < 750):
		Cls
		tim = MilliSecs()
		d = counter/250
		if f != -1:
			d = laststartingdifficulty
		CycleColours()
		CycleColours()
		colr[9] = rcol
		colg[9] = gcol
		colb[9] = bcol
		if counter % 4 == 0:
			for i= 1 To 9:
				colr[i-1] = colr[i]
				colg[i-1] = colg[i]
				colb[i-1] = colb[i]


		SetColor 0,0,240
		DrawString("TOP SCORES - "+difficulty$[d],SCREENW/2-200,SCREENH/2-220,4)
		SetColor 64,240,64
		DrawString("SCORE",SCREENW/2-250,SCREENH/2-180,3)
		DrawString("NAME",SCREENW/2-100,SCREENH/2-180,3)
		DrawString("TIME",SCREENW/2+130,SCREENH/2-180,3)

		for t = 0 To 9:
			SetColor colr[9-t],colg[9-t],colb[9-t]
			if t = f and d = laststartingdifficulty:
				SetColor 255,255,0

			if KeyDown(KEY_P):
				s: str = scores[t,d]
				spc= Len(s$)
				DrawString(s$,SCREENW/2-180-spc*14,SCREENH/2-150+t*32,2)
				DrawString(names[t,d],SCREENW/2-120,SCREENH/2-150+t*32,2)
				DrawString((playtimes[t,d]),SCREENW/2+64,SCREENH/2-150+t*32,2)
				s: str = scoresetting[t,d]
				DrawString(s$,SCREENW/2-180-spc*14,SCREENH/2-150+t*32+16,2)
			else:
				s: str = scores[t,d]
				spc= Len(s$)
				DrawString(s$,SCREENW/2-180-spc*14,SCREENH/2-150+t*30,3)
				DrawString(names[t,d],SCREENW/2-120,SCREENH/2-150+t*30,3)
				DrawString((playtimes[t,d]),SCREENW/2+64,SCREENH/2-150+t*30,3)


		if f = -20:
			s: str = pscore
			spc= Len(s$)
			SetColor 255,0,0
			DrawString(s$,SCREENW/2-180+32-spc*14,SCREENH/2-150+11*30,3)
			DrawString(ptime$,SCREENW/2+64-32,SCREENH/2-150+11*30,3)

		if randint(0,100) > 90 and counter < 700:
			part.CreateFireworks(1)
		part.UpdateParticles(1)
		part.DrawParticles()
		SetColor 255,255,0
		if counter % 50 > 25:
			DrawString("Press BOMB Button to Start",SCREENW/2-250,SCREENH-32,4)

		Flip 1
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		counter = counter+1
		bombtime -= 1
		if bombtime < 0:
			bombtime = 0
		if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_option,joyport) and controltype = 0 and bombtime = 0):
			if Options(False):
				return True
			bombtime = 20

		if KeyHit(k_bomb) or MouseHit(m_bomb) or (JoyDown(j_pad_bomb,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_bomb,joyport) and controltype = 0 and bombtime = 0):
			counter = 1000
			playgame = True
			bombtime = 20

	return False



def ShowTitle() -> int:

	Local counter: int,kol: int,sc: float,st: str,ln: int,xd: int,yd: int,z: int,cc: int,zz: float,b: int
	Local tim: int
	Local shrink: float = (SCREENW/1024.0)

	nme5.createdisplayeffect(SCREENW/2+randint(-100,100),SCREENH/2+randint(-100,100),randint(12,50))
	nme5.createdisplayeffect(SCREENW/2+randint(-100,100),SCREENH/2+randint(-100,100),randint(12,50))

	SetViewport 0,0,SCREENW,SCREENH
	gxoff = 0
	gyoff = 0

	FlushKeys()

	bombtime = 20
	counter = 0

	st: str = "GridWars 2"
	ln = Len(st$)-1

	while (counter < 900):
		SetLineWidth 2.0
		SetBlend lightblend
		SetAlpha 1
		shrink: float = (SCREENW / 1024.0)
		gcount += 1
		Cls
		tim = MilliSecs()
		CycleColours()
		if tcounter > 350:
			if randint(0,100) > 90 and counter < 850:
				part.CreateFireworks(0)
			part.UpdateParticles(1)
			part.DrawParticles()
			BlackholeParticles()
			#red circles
			for Local n5 in nme5_list:
				n5.UpdateDisplayEffect()

		kol = 128+tcounter/3
		if kol > 255:
			kol = 255
		SetColor 0,0,kol
		sc: float = tcounter/24.0
			if sc > 20:
				sc = 20
		for z = 0 To tcounter/25:
			SetColor rcol,gcol,bcol
			xd = (SCREENW-ln*sc*shrink*5.5)/2+Cos(z*20+counter*2)*(2+tcounter/60)
			yd = (SCREENH-18*sc*shrink)/2-50+Sin(z*20+counter*2)*(2+tcounter/60)+600/8-tcounter/8
			DrawString(st$,xd,yd,sc*shrink)


		SetColor 64,180,64
		DrawString("Programmed In Blitzmax",SCREENW/2-22/2*5*3.2*shrink,SCREENH-280,3.2*shrink)
		DrawString("By Mark Incitti",SCREENW/2-15/2*5*3.2*shrink,SCREENH-240,3.2*shrink)
		if counter % 200 > 99:
			DrawString(version$,SCREENW/2-25/2*5*3*shrink,SCREENH-200,3*shrink)
		else:
			DrawString(advert$,SCREENW/2-36/2*5*3*shrink,SCREENH-200,3.1*shrink)


		SetColor 240,32,200
		DrawString("Special Thanks To",SCREENW/2-17/2*5*3.2*shrink,SCREENH-160,3.2*shrink)
		SetColor 200,32,240
		DrawString("Svrman, taumel - Gfx & Effects, Swith - Music, RiK - Mac",SCREENW/2-56/2*5*3.2*shrink,SCREENH-120,3.2*shrink)

		SetColor 255,255,0
		if counter % 60 > 29:
			DrawString("Press BOMB Button to Start",SCREENW/2-26/2*5*4*shrink,SCREENH-32,4*shrink)

		Flip 1
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		counter = counter + 1
		bombtime -= 1
		if bombtime < 0:
			bombtime = 0

		tcounter = tcounter+1
		if tcounter > 600:
			tcounter = 600

		if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_option,joyport) and controltype = 0 and bombtime = 0):
			if Options(False):
				return True

		if KeyHit(k_bomb) or MouseHit(m_bomb) or (JoyDown(j_pad_bomb,joyport) and controltype = 3 and bombtime = 0) or (JoyDown(j_d_bomb,joyport) and controltype = 0 and bombtime = 0):
			counter = 1000
			playgame = True

	tcounter = 600
	return False



def CenterPlayer()

	px = PLAYFIELDW/2
	py = PLAYFIELDH/2
	gxoff = (PLAYFIELDW-SCREENW)/2
	gyoff = (PLAYFIELDH-SCREENH)/2


def GetReady() -> int:

	Local count: int
	Local i: int
	Local tim: int

	CenterPlayer()

	PlaySound2(get_ready_snd)
	count = 0
	while count < 60 and not KeyDown(KEY_ESCAPE):
		Cls
		tim = MilliSecs()

		gridpoint.UpdateGrid()
		UpdateAll()
		drawall()
#		if KeyDown(KEY_TAB): End
#		if not KeyDown(KEY_F8)
			SetColor 0,55+abs(Sin(count))*200,0
			DrawString("GET READY", SCREENW/2-abs(Sin(count))*19*5*9*.5, SCREENH/2-abs(Sin(count))*100, abs(Sin(count))*20)
#			DrawString("GET READY", SCREENW/2+60-abs(Sin(count))*SCREENW/2,SCREENH/2-abs(Sin(count))*100,abs(Sin(count))*20)

		Flip
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		count += 1
		if KeyHit(k_bomb) or MouseHit(m_bomb)
			count = 60

	gridpoint.Pull(px,py,20,20)
	count = 0
	while count < 40 and not KeyDown(KEY_ESCAPE):
		Cls
		tim = MilliSecs()

		gridpoint.UpdateGrid()
		UpdateAll()
		drawall()
		# if KeyDown(KEY_TAB): End
		# if not KeyDown(KEY_F8)
		SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
		if count > 10:
			DrawPlayer(px,py,pr)
		DrawCircle(SCREENW/2,SCREENH/2,300-count*6)
		DrawCircle(SCREENW/2,SCREENH/2,300-count*8)
		DrawCircle(SCREENW/2,SCREENH/2,300-count*12)

		Flip
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		count += 1
		if KeyHit(k_bomb) or MouseHit(m_bomb)
			count = 40

	player_shield = 80
	messtime = 0
	StartMusic(1)
	Score.ResetMultiplier()
	oldmx = 0
	oldmy = 0
	MoveMouse(SCREENW/2,SCREENH/2)



def KillPlayer() -> int:
	Local tim: int

	if nokillme or player_shield > 0:
		return False

	#only killed once per update
	if dying:
		return False

	dying = True
	StopMusic()

	PlaySound2(player_hit_snd)

	# create explosion
	for Local t: int = 0 To 255
		part.Create(px,py,0 ,COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B)


	gridpoint.Pull(px,py,32,64)

	Local s:shot
	for s in shot_list:
		shot_list.remove(s)


	removeall(False) #remove all but the killer
	Local count: int = 0
	while (count < 100) and not KeyDown(KEY_ESCAPE):
		Cls
		tim = MilliSecs()

		#gridpoint.UpdateGrid()
		UpdateAll(count)
		drawall()
		Flip
		tim = MilliSecs() - tim
		if tim < 20 and tim > 0:
			sleep(20-tim)

		count += 1

	removeall(True) #remove killer too

	# reset to center
	numplayers = numplayers - 1
	CenterPlayer()
	gridpoint.ResetAll()

	if numplayers == 0:
		gameover = True
		PlaySound2(game_over_snd)
	else:
		# take away a shot, speed and return to forward shooting
		if numshots > 2:
			numshots -= 1
		if shotspeed > 3:
			shotspeed -= 1
		shot_back = 0
		shot_side = 0
		supershots = 0
		bouncyshots	= 0
		jdfx = 0
		jdfy = 0
		# reset score multiplier to 1X
		score.ResetMultiplier()
		GetReady()

	dying = False
	Cls
	return True



def RemoveAll(all: bool=False)

	Local n:nme
	Local n1:nme1
	Local n2:nme2
	Local n3:nme3
	Local n4:nme4
	Local n5:nme5
	Local n6:nme6
	Local n7:nme7
	Local n8:nme8
	Local g:ge
	Local ll:le
	Local po:pu
	Local sc:score
	Local s:shot
	Local tr:trail

	for tr in trail_list:
		trail_list.Remove(tr)


	for s in shot_list:
		shot_list.Remove(s)


	for sc in score_list:
		score_list.Remove(sc)


	if all:
		part.ResetAll()

	StopLoopingSounds()

	for n in nme_list:
		if all or n.killer = False nme_LIST.Remove(n)

	for n1 in nme1_list:
		if all or n1.killer is False:
			nme1_LIST.Remove(n1)

	for n2 in nme2_list:
		if all or n2.killer is False:
			nme2_LIST.Remove(n2)

	for n3 in nme3_list:
		if all or n3.killer is False:
			nme3_LIST.Remove(n3)

	for n4 in nme4_list:
		if all or n4.killer is False:
			nme4_LIST.Remove(n4)

	for n5 in nme5_list:
		if all or n5.killer is False:
			nme5_LIST.Remove(n5)

	for ll in le_list:
		if all or ll.killer is False:
			le_LIST.Remove(ll)

	for g in ge_list:
		if all or g.killer is False:
			ge_list.Remove(g)

	for po in pu_list:
		pu_list.Remove(po)

	for n6 in nme6_list:
		if all or n6.killer is False:
			nme6_LIST.Remove(n6)

	for n7 in nme7_list:
		if all or n7.killer is False:
			nme7_LIST.Remove(n7)

	for n8 in nme8_list:
		if all or n8.killer is False:
			nme8_LIST.Remove(n8)

	if all:
		gridpoint.ResetAll()

	# reset the spawn counters
	sp_t = 0
	sp_t2 = 0
	sp_t3 = 0
	sp_t4 = 0



def DestroyAll()
	Local n:nme
	Local n1:nme1
	Local n2:nme2
	Local n3:nme3
	Local n4:nme4
	Local n5:nme5
	Local n6:nme6
	Local n7:nme7
	Local n8:nme8
	Local g:ge
	Local ll:le
	Local po:pu

	for n:nme = EachIn nme_list
		n.kill(False)

	for n1 in nme1_list:
		n1.kill(False)

	for n2 in nme2_list:
		n2.kill(False)

	for n3 in nme3_list:
		n3.kill(False)

	for n4 in nme4_list:
		n4.kill(False)

	for n5 in nme5_list:
		n5.kill(False)

	for n6 in nme6_list:
		if n6.ishead:
			n6.kill(False)

	for n7 in nme7_list:
		n7.kill(False)

	for n8 in nme8_list:
		n8.kill(False)

	for ll in le_list:
		ll.kill(False,0,0)

	for g in ge_list:
		g.kill(False)



def ResetGame()

	laststartingdifficulty = startingdifficulty
	gameover = False

	speed_nme#  = 3.1
	speed_nme1: float = 2.25
	speed_nme2: float = 3.25
	speed_nme3: float = 3.0
	speed_nme4: float = 4.35
	speed_nme5: float = 2.5
	speed_nme6: float = 3.5
	speed_nme7: float = 4.45
	speed_nme8: float = 5.0
	speed_le#   = 2.0

	Select startingdifficulty
		Case 0 # easy

			upgradetime = 20

			speed_nme *=  .75
			speed_nme1 *= .75
			speed_nme2 *= .75
			speed_nme3 *= .75
			speed_nme4 *= .75
			speed_nme5 *= .75
			speed_nme6 *= .75
			speed_nme7 *= .75
			speed_nme8 *= .75
			speed_le *= .75

			numplayers = 4
			numbombs = 4

			numshots = 2
			shotspeed = 4
			gcount = 1

			EXTRABOMB = exbomb[0]  #100000
			EXTRALIFE = exlife[0]   #75000

		Case 1 #medium

			upgradetime = 18

			numplayers = 3
			numbombs = 3

			numshots = 2
			shotspeed = 3
			gcount = 1

			EXTRABOMB = exbomb[1]  #150000
			EXTRALIFE = exlife[1]   #100000

		Case 2 #hard

			upgradetime = 16

			speed_nme *=  1.25
			speed_nme1 *= 1.25
			speed_nme2 *= 1.25
			speed_nme3 *= 1.25
			speed_nme4 *= 1.25
			speed_nme5 *= 1.25
			speed_nme6 *= 1.25
			speed_nme7 *= 1.25
			speed_nme8 *= 1.25
			speed_le *=   1.25

			numplayers = 2
			numbombs = 2

			numshots = 2
			shotspeed = 3
			gcount = 7000

			EXTRABOMB = exbomb[2]  #200000
			EXTRALIFE = exlife[2]   #150000



	extralifecount = 1
	shot_back = 0
	shot_side = 0
	supershots = 0
	bouncyshots = 0
	jdfx = 0
	jdfy = 0
	powerupscore = POWERUP
	bombtime = 20
	extrabombcount = 1
	sp_t = 0
	sp_t2 = 0
	sp_t3 = 0
	sp_t4 = 0

	score.ResetScore()
	score.ResetMultiplier()



def EnemyType(cnt: int) -> int:

	Local t: int
	Local sel: int = cnt/1100
	if sel > 8:
		sel = 8

	Select sel
		Case 0
			t = 0
		Case 1
			t = randint(0,1)
		Case 2
			t = randint(0,2)
		Case 3
			t = randint(0,3)
		Case 4
			t = randint(0,4)
		Case 5
			t = randint(0,5)
		Case 6
			t = randint(0,6)
		Case 7
			t = randint(0,7)
		Case 8
			t = randint(0,9)

	return t




def Spawn(cnt: int):

Rem
	if cnt % 40 = 0
		CreateEnemy(randint(1,2),20, randint(0,12))

	if cnt % 40 = 0
		CreateEnemy(5,20, randint(0,12))

	return
End Rem
	Local gk: int,sz: int,rate: int

	#single enemy
	if (cnt/350) % 2 == 0:
		if cnt % 33 == 0:
			CreateEnemy(EnemyType(cnt),30, randint(0,12))


	#single generator
	if cnt % 444 == 0:
		gk = EnemyType(cnt/3+500)+1
		sz = Min(randint(16+cnt/2000),32)
		rate = 80+randint(60)-cnt/1000
		if rate < 60:
			rate = 60
		if gk == 9: #no clone generator
			gk = 10 #butterfly geerator

		if gk == 6: #no sun generator
			gk = randint(3,5) #green, purp, or blue

		CreateEnemy(10,20,randint(0,12),rate,gk,sz)

	#whole bunch
	if cnt % 777 == 0:
		sp_c = randint(0,12)
		sp_x = EnemyType(cnt/3)
		sp_t = randint(15,24+(cnt/750))*2
		if sp_t > 100:
			sp_t = 100
		if sp_x == 5:
			sp_t = 2*8


	if cnt % 1850 == 0:
		#whole bunch
		sp_c2 = randint(0,12)
		sp_x2 = EnemyType(cnt/2)
		sp_t2 = randint(15,24+(cnt/750))*2
		if sp_t2 > 175:
			sp_t2 = 175
		if sp_x2 == 5:
			sp_t2 = 2*8


	if cnt % 2900  == 0:
		#whole bunch
		sp_c3 = 5 #all 4 corners
		sp_x3 = EnemyType(cnt/2)
		sp_t3 = randint(20,40+(cnt/750))*3
		if sp_t3 > 100*3:
			sp_t3 = 100*3
		if sp_x3 == 5:
			sp_t3 = 3*8


	if ((cnt/4000) % 2 = 1) and (cnt % 3333 = 0):
		#whole bunch
		sp_c4 = randint(0,11) #any corner/s
		sp_x4 = EnemyType(cnt/2)
		sp_t4 = randint(20,40+(cnt/750))*3
		if sp_t4 > 100*3:
			sp_t4 = 100*3
		if sp_x4 == 5:
			sp_t4 = 3 * 8


	#keep placing the whole bunch
	if sp_t > 0:
		sp_t -= 1
		if sp_t % 2 == 0:
			CreateEnemy(sp_x,24,sp_c)


	#keep placing the whole bunch
	if sp_t2 > 0:
		sp_t2 -= 1
		if sp_t2 % 2 == 0:
			CreateEnemy(sp_x2,24,sp_c2)


	#keep placing the whole bunch
	if sp_t3 > 0:
		sp_t3 -= 1
		if sp_t3 % 3 == 0:
			if sp_x3 = 9:
				CreateEnemy(sp_x3,20,sp_c3) # 2X more indigo triangles
			CreateEnemy(sp_x3,20,sp_c3)


	#keep placing the whole bunch
	if sp_t4 > 0:
		sp_t4 -= 1
		if sp_t4 % 3 == 0:
			if sp_x4 = 9:
				CreateEnemy(sp_x4,20,sp_c4) # 2X more indigo triangles
			CreateEnemy(sp_x4,20,sp_c4)


	if cnt % 50*60 == 1: #every minute?
		inc: float = 0.15+startingdifficulty*0.1
		speed_nme += inc
		speed_nme1 += inc
		speed_nme2 += inc
		speed_nme3 += inc
		speed_nme4 += inc
		speed_nme5 += inc
		speed_nme6 += inc
		speed_nme7 += inc
		speed_nme8 += inc
		speed_le += inc




def CreateEnemy(kind: int,freeze: int,corner: int=0,rate: int=100,gkind: int=1,size: int=20)

	if bombtime > 0:
		return

	Local x: int,y: int,k: int,sz: int

	if corner > 4:
		Select corner
			Case 5
				corner = randint(1,4)
			Case 6
				if randint(1,10) > 5:
					corner = 1
				else:
					corner = 2
			Case 7
				if randint(1,10) > 5:
					corner = 2
				else:
					corner = 3
			Case 8
				if randint(1,10) > 5:
					corner = 3
				else:
					corner = 4
			Case 9
				if randint(1,10) > 5:
					corner = 1
				else:
					corner = 3
			Case 10
				if randint(1,10) > 5:
					corner = 1
				else:
					corner = 4
			Case 11
				if randint(1,10) > 5:
					corner = 2
				else:
					corner = 4


	Select corner
		Case 0
			x = randint(30,PLAYFIELDW-30)
			y = randint(30,PLAYFIELDH-30)
		Case 1
			x = randint(30,80)
			y = randint(30,80)
		Case 2
			x = randint(PLAYFIELDW-80,PLAYFIELDW-30)
			y = randint(30,80)
		Case 3
			x = randint(PLAYFIELDW-80,PLAYFIELDW-30)
			y = randint(PLAYFIELDH-80,PLAYFIELDH-30)
		Case 4
			x = randint(30,80)
			y = randint(PLAYFIELDH-80,PLAYFIELDH-30)
		Case 12
			Local dir: int = randint(0,360)
			Local mag: float = 240
			x = px+Cos(dir)*mag
			y = py+Sin(dir)*mag


	Select kind
		Case 0
			nme1.Create(x,y,freeze)
		Case 1
			nme2.Create(x,y,freeze)
		Case 2
			nme.Create(x,y,freeze)
		Case 3
			nme3.Create(x,y,0,freeze)
		Case 4
			nme4.Create(x,y,freeze)
		Case 5
			nme5.Create(x,y,20,freeze)
		Case 6
			le.Create(x,y,freeze)
		Case 7
			nme6.Create(x,y,24,freeze)
		Case 8
			nme7.Create(x,y,freeze)
		Case 9
			nme8.Create(x,y,freeze)
		Case 10
			ge.Create(x,y,gkind,rate,size,freeze)






def Updateplayer()

	Local xx: float, yy: float, xy: float,  jb: int, i: int, r: int	, speed: float
	Select controltype

		Case 1 # mouse
			#bombs
			jb = 0
			bombtime = bombtime - 1
			if bombtime < 0:
				bombtime = 0
			jb = KeyDown(k_bomb) + MouseDown(m_bomb)
			if jb and bombtime == 0:
				shot.SuperBomb()

			#move
			xx = (MouseX()-SCREENW/2)
			yy = (MouseY()-SCREENH/2)
			MoveMouse(SCREENW/2,SCREENH/2)

			jdmx = xx/128*(1+m_sensitivity*5)
			jdmy = yy/128*(1+m_sensitivity*5)
#			xy = sqrt(jdmx*jdmx+jdmy*jdmy)

#			if xy > 10
#				jdmx = jdmx/xy*10
#				jdmy = jdmy/xy*10
#

			#fire
			if MouseDown(m_fire):
				#change fire direction
				xy = (jdmx*jdmx+jdmy*jdmy)
				if xy > 0:
					jdfx = xx/16
					jdfy = yy/16

			else:
				if not autofire
					jdfx = 0
					jdfy = 0


			oldmx *= inertia
			oldmy *= inertia
			jdmx += oldmx
			jdmy += oldmy
			# stay within screen
			speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
			if speed > (1+m_sensitivity*10):
				jdmx = jdmx/(1+m_sensitivity*10)
				jdmy = jdmy/(1+m_sensitivity*10)

			oldmx = jdmx
			oldmy = jdmy
		Case 0 # dual analog joy
			#bombs
			jb = 0
			bombtime = bombtime - 1
			if bombtime < 0:
				bombtime = 0
			jb = JoyDown(j_d_bomb,joyport)
			if jb and bombtime = 0:
				shot.SuperBomb()

			#move
			jdmx = GetJoyByAxis(joyport, axis_move_x,axis_move_x_inv,axis_move_x_sc,axis_move_x_center )
			jdmy = GetJoyByAxis(joyport, axis_move_y,axis_move_y_inv,axis_move_y_sc,axis_move_y_center )
			# if abs(jdmx) < axis_move_x_dz: jdmx = 0
			# if abs(jdmy) < axis_move_y_dz: jdmy = 0
			if abs(jdmx) < axis_move_x_dz and abs(jdmy) < axis_move_y_dz:
				jdmx = 0
				jdmy = 0


			#fire
			jdfx = GetJoyByAxis(joyport, axis_fire_x,axis_fire_x_inv,axis_fire_x_sc,axis_fire_x_center )
			jdfy = GetJoyByAxis(joyport, axis_fire_y,axis_fire_y_inv,axis_fire_y_sc,axis_fire_y_center )
			# if abs(jdfx) < axis_fire_x_dz: jdfx = 0
			# if abs(jdfy) < axis_fire_y_dz: jdfy = 0
			if abs(jdfx) < axis_fire_x_dz and abs(jdfy) < axis_fire_y_dz:
				jdfx = 0
				jdfy = 0

			oldmx *= inertia
			oldmy *= inertia
			jdmx += oldmx
			jdmy += oldmy
			# stay within screen
			speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
			if speed > 1:
				jdmx = jdmx/speed
				jdmy = jdmy/speed

			oldmx = jdmx
			oldmy = jdmy

		Case 2 #keys
			#bombs
			jb = KeyDown(k_bomb)
			bombtime = bombtime - 1
			if bombtime < 0:
				bombtime = 0
			if jb and bombtime == 0:
				shot.SuperBomb()

			#move
			jdmx = KeyDown(k_move_right) - KeyDown(k_move_left)
			jdmy = KeyDown(k_move_down) - KeyDown(k_move_up)

			#fire
			if autofire:
				if KeyDown(k_fire_right):
					jdfx = 1
					jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

				if KeyDown(k_fire_left):
					jdfx = -1
					jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

				if KeyDown(k_fire_down):
					jdfy = 1
					jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)

				if KeyDown(k_fire_up):
					jdfy = -1
					jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)

			else:
				jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)
				jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

			oldmx *= inertia
			oldmy *= inertia
			jdmx += oldmx
			jdmy += oldmy
			# stay within screen
			speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
			if speed > 1:
				jdmx = jdmx/speed
				jdmy = jdmy/speed

			oldmx = jdmx
			oldmy = jdmy
		Case 3 #joypad
			#bombs
			jb = 0
			bombtime = bombtime - 1
			if bombtime < 0:
				bombtime = 0
			jb = JoyDown(j_pad_bomb,joyport)
			if jb and bombtime == 0:
				shot.SuperBomb()

			Select j_config
				Case 0
					#move
					jdmx = JoyX()
					jdmy = JoyY()

					#fire
					jdfx = JoyDown(j_pad_3, joyport) - JoyDown(j_pad_1, joyport)
					jdfy = JoyDown(j_pad_2, joyport) - JoyDown(j_pad_4, joyport)

				Case 1
					#move
					jdmx = JoyDown(j_pad_3, joyport) - JoyDown(j_pad_1, joyport)
					jdmy = JoyDown(j_pad_2, joyport) - JoyDown(j_pad_4, joyport)

					#fire
					jdfx = JoyX()
					jdfy = JoyY()

			if abs(jdmx) < 0.5:
				jdmx = 0
			if abs(jdmy) < 0.5:
				jdmy = 0
			if abs(jdfx) < 0.5:
				jdfx = 0
			if abs(jdfy) < 0.5:
				jdfy = 0

			oldmx *= inertia
			oldmy *= inertia
			jdmx += oldmx
			jdmy += oldmy
			# stay within screen
			speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
			if speed > 1:
				jdmx = jdmx/speed
				jdmy = jdmy/speed

			oldmx = jdmx
			oldmy = jdmy
		Case 4 # hybrid mouse/keys
			#bombs
			jb = KeyDown(k_bomb) + MouseDown(m_bomb)
			bombtime = bombtime - 1
			if bombtime < 0:
				bombtime = 0
			if jb and bombtime == 0:
				shot.SuperBomb()

			Select h_config
				Case 0
					#move
					jdmx = KeyDown(k_move_right) - KeyDown(k_move_left)
					jdmy = KeyDown(k_move_down) - KeyDown(k_move_up)

					mxaim= MouseX()
					myaim= MouseY()
					xx = mxaim-(px-gxoff)
					yy = myaim-(py-gyoff)
					xy = sqrt(xx*xx+yy*yy)
					if xy < 1:
						xy = 1

					#fire
					if MouseDown(m_fire):
						jdfx = xx/xy
						jdfy = yy/xy
					else:
						if not autofire:
							jdfx = 0
							jdfy = 0


					#Draw target
					DrawTarget(mxaim,myaim,gcount)
					oldmx *= inertia
					oldmy *= inertia
					jdmx += oldmx
					jdmy += oldmy
					# stay within screen
					speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
					if speed > 1:
						jdmx = jdmx/speed
						jdmy = jdmy/speed

					oldmx = jdmx
					oldmy = jdmy
				Case 1
					#move
					xx = (MouseX()-SCREENW/2)
					yy = (MouseY()-SCREENH/2)
					MoveMouse(SCREENW/2,SCREENH/2)

					jdmx = xx/128*(1+m_sensitivity*5)
					jdmy = yy/128*(1+m_sensitivity*5)

					#fire
					if autofire:
						if KeyDown(k_fire_right):
							jdfx = 1
							jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

						if KeyDown(k_fire_left):
							jdfx = -1
							jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

						if KeyDown(k_fire_down):
							jdfy = 1
							jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)

						if KeyDown(k_fire_up):
							jdfy = -1
							jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)

					else:
						jdfx = KeyDown(k_fire_right) - KeyDown(k_fire_left)
						jdfy = KeyDown(k_fire_down) - KeyDown(k_fire_up)

					oldmx *= inertia
					oldmy *= inertia
					jdmx += oldmx
					jdmy += oldmy
					# stay within screen
					speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
					if speed > (1+m_sensitivity*10):
						jdmx = jdmx/(1+m_sensitivity*10)
						jdmy = jdmy/(1+m_sensitivity*10)

					oldmx = jdmx
					oldmy = jdmy
				Case 2
					#move
					jdmx = KeyDown(k_move_right) - KeyDown(k_move_left)
					jdmy = KeyDown(k_move_down) - KeyDown(k_move_up)

					xx = (MouseX()-SCREENW/2)
					yy = (MouseY()-SCREENH/2)

					#fire
					if not autofire:
						if MouseDown(m_fire):
							xy = sqrt(xx*xx+yy*yy)
							if xy > 1:
								mxaim = xx/xy
								myaim = yy/xy

							jdfx = mxaim
							jdfy = myaim
						else:
#							MoveMouse(SCREENW/2,SCREENH/2)
							jdfx = 0
							jdfy = 0

					else:
						xy = sqrt(xx*xx+yy*yy)
						if xy > 1:
							mxaim = xx/xy
							myaim = yy/xy

						jdfx = mxaim
						jdfy = myaim


					if KeyDown(k_fire_up):
						if myaim > -1:
							myaim = myaim -.1
						if mxaim != 0:
							mxaim = mxaim*.8
						jdfx = mxaim
						jdfy = myaim

					if KeyDown(k_fire_down):
						if myaim < 1:
							myaim = myaim +.1
						if mxaim != 0:
							mxaim = mxaim*.8
						jdfx = mxaim
						jdfy = myaim

					if KeyDown(k_fire_right):
						if mxaim < 1:
							mxaim = mxaim +.1
						if myaim != 0:
							myaim = myaim*.8
						jdfx = mxaim
						jdfy = myaim

					if KeyDown(k_fire_left):
						if mxaim > -1:
							mxaim = mxaim -.1
						if myaim != 0:
							myaim = myaim*.8
						jdfx = mxaim
						jdfy = myaim

					#Draw target
					DrawTarget(px+mxaim*80-gxoff,py+myaim*80-gyoff,gcount)
					oldmx *= inertia
					oldmy *= inertia
					jdmx += oldmx
					jdmy += oldmy
					# stay within screen
					speed: float = sqrt(jdmx*jdmx + jdmy*jdmy)
					if speed > 1:
						jdmx = jdmx/speed
						jdmy = jdmy/speed

					oldmx = jdmx
					oldmy = jdmy



	px = px + jdmx*MAXPLAYERSPEED
	if px < 16 or px > PLAYFIELDW-16
		px = px - jdmx*MAXPLAYERSPEED
		oldmx = -oldmx

	py = py + jdmy*MAXPLAYERSPEED
	if py < 16 or py > PLAYFIELDH-16
		py = py - jdmy*MAXPLAYERSPEED
		oldmy = -oldmy

	if jdmy != 0 or jdmx != 0
		pr = ATan2(jdmy,jdmx)-90


	# create player trail
	if abs(jdmx) > 0.1 or abs(jdmy) > 0.1
		for Local tt: int = 0 To 2
			trail.create(..
			px-jdmx*12+Sin(gcount*12+tt*45)*8,..
			py-jdmy*12+Cos(gcount*12+tt*45)*8,..
			COL_TRAIL_R,COL_TRAIL_G,COL_TRAIL_B,..
			-jdmx,-jdmy)




	if scroll:
		# scroll the playfield
		Local scr: int
		scr = px-gxoff
		if scr < 500:
			gxoff -= 2*(5-scr/100)
			if gxoff < -80:
				gxoff = -80


		scr = py-gyoff
		if scr < 500:
			gyoff -= 2*(5-scr/100)
			if gyoff < -80:
				gyoff = -80


		scr = px-gxoff-SCREENW
		if scr > -500
			gxoff += 2*(5-abs(scr)/100)
			if gxoff > (PLAYFIELDW-SCREENW)+80
				gxoff = (PLAYFIELDW-SCREENW)+80


		scr = py-gyoff-SCREENH
		if scr > -500:
			gyoff += 2*(5-abs(scr)/100)
			if gyoff > (PLAYFIELDH-SCREENH)+80:
				gyoff = (PLAYFIELDH-SCREENH)+80




if KeyHit(KEY_F3):
	g_style += 1
	if g_style > numgridstyles:
		g_style = 0:
	score.create("Grid Style ="+g_style,px-100,py-64,2)

if KeyHit(KEY_F4):
	showstars += 100
	if showstars > MAXSTARS:
		showstars = 0
	score.create("Number of Stars ="+showstars,px-100,py-64,2)

if KeyHit(KEY_F5):
	gravityparticles = 1-gravityparticles
	if gravityparticles:
		score.create("Particle Gravity ON",px-100,py-64,2)
	else:
		score.create("Particle Gravity OFF",px-100,py-64,2)


if KeyHit(KEY_F6):
	particlestyle += 1
	if particlestyle > numparticlestyles:
		 particlestyle = 0
	score.create("Particle - Style "+particlestyle,px-100,py-64,2)

if KeyHit(KEY_F7):
	# debug = 1-debug # TODO - make this consistent
	debug = not debug
	if debug:
		score.create("Debug ON",px-100,py-64,2)
	else:
		score.create("Debug OFF",px-100,py-64,2)



# cheat stuff
if KeyHit(KEY_F1):
	valid = False
	# cheat = 1-cheat #
	cheat = not cheat # TODO here too
	if cheat:
		score.create("Cheatmode ON",px-100,py-64,2)
	else:
		score.create("Cheatmode OFF",px-100,py-64,2)


if cheat:
	if KeyHit(KEY_1):
		shot_back +=  15*30
	if KeyHit(KEY_2):
		shot_side +=  15*30
	if KeyHit(KEY_3):
		supershots +=  15*30
	if KeyHit(KEY_4):
		bouncyshots +=  15*30
	if KeyHit(KEY_X):
		numshots += 1
		if numshots > 4:
			numshots = 4
	if KeyHit(KEY_Z):
		shotspeed += 1
		if shotspeed > 5:
			shotspeed = 5
	if KeyHit(KEY_S):
		pu.MakePowerup(6)
	if KeyHit(KEY_F2):
		# nokillme = 1-nokillme
		nokillme = not nokillme
		if nokillme:
			score.create("God %e ON",px-100,py-64,2)
		else:
			score.create("God %e OFF",px-100,py-64,2)



	# timed upgrades
	if shot_back > 0:
		shot_back -= 1

	if shot_side > 0:
		shot_side -= 1

	if player_shield > 0
		player_shield -= 1
		if player_shield = 100 or player_shield = 70 or player_shield = 40
			playsound2(shieldwarningsnd)


	if supershots > 0
		supershots  -= 1

	if bouncyshots> 0
		bouncyshots -= 1


	# fire!
	shottimer -= 1
	if shottimer < 0:
		shottimer = 0
	if shottimer = 0:
		if debug:
			shottimer = 4
			# evil!
			if numshots = 2:
				shottimer = 8   #4,4,6,6
			if numshots = 3:
				shottimer = 10
			if numshots = 4:
				shottimer = 8
			if jdfx != 0 or jdfy != 0:
				Local xr: float
				Local yr: float
				speed: float = sqrt(jdfx*jdfx+jdfy*jdfy)
				jdfx = jdfx/speed
				jdfy = jdfy/speed
				#Local dir2: float = ATan2(jdfy,jdfx)
				if numshots = 1:
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					#TFormR(0,0,0, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)

				if numshots = 2:
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,12, xr ,yr )
					shot.create(px+25*xr,py+25*yr,xr,yr,shotspeed*2)
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,-12, xr ,yr )
					shot.create(px+25*xr,py+25*yr,xr,yr,shotspeed*2)

				if numshots = 3:
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,3, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)
					xr: float = jdfx*shotspeed*2.05
					yr: float = jdfy*shotspeed*2.05
					TFormR(0,0,2.5, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2.05)
					xr: float = jdfx*shotspeed*2.05
					yr: float = jdfy*shotspeed*2.05
					TFormR(0,0,0, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2.05)
					xr: float = jdfx*shotspeed*2.05
					yr: float = jdfy*shotspeed*2.05
					TFormR(0,0,-2.5, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2.05)
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,-3, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)

				if numshots = 4:
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,-2, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)
					xr: float = jdfx*shotspeed*2.25
					yr: float = jdfy*shotspeed*2.25
#					TFormR(0,0,0, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2.25)
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,2, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)

				if shot_back > 0:
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,-180, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)

				if shot_side > 0
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,90, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)
					xr: float = jdfx*shotspeed*2
					yr: float = jdfy*shotspeed*2
					TFormR(0,0,-90, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*2)

				PlaySound2(shot_born_snd)
				#evil

		else:
			shottimer = 4 + numshots/2
			if jdfx != 0 or jdfy != 0:
				Local xr: float
				Local yr: float
				speed: float = sqrt(jdfx*jdfx+jdfy*jdfy)
				jdfx = jdfx/speed
				jdfy = jdfy/speed
				if numshots % 2 = 1:
					xr: float = jdfx*shotspeed*3.2
					yr: float = jdfy*shotspeed*3.2
					TFormR(0,0,0, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3.2)

				if numshots > 1:
					if numshots % 2 = 0:
						r = 2 else: r = 4
					xr: float = jdfx*shotspeed*3.15
					yr: float = jdfy*shotspeed*3.15
					TFormR(0,0,r, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3.15)
					xr: float = jdfx*shotspeed*3.15
					yr: float = jdfy*shotspeed*3.15
					TFormR(0,0,-r, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3.15)

				if numshots > 3:
					if numshots == 4: # TODO WTF?
						r = 5
					else:
						r = 5
					xr: float = jdfx*shotspeed*3.1
					yr: float = jdfy*shotspeed*3.1
					TFormR(0,0,r, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3.1)
					xr: float = jdfx*shotspeed*3.1
					yr: float = jdfy*shotspeed*3.1
					TFormR(0,0,-r, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3.1)

				if shot_back > 0:
					xr: float = jdfx*shotspeed*3
					yr: float = jdfy*shotspeed*3
					TFormR(0,0,-180, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3)

				if shot_side > 0:
					xr: float = jdfx*shotspeed*3
					yr: float = jdfy*shotspeed*3
					TFormR(0,0,90, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3)
					xr: float = jdfx*shotspeed*3
					yr: float = jdfy*shotspeed*3
					TFormR(0,0,-90, xr ,yr )
					shot.create(px,py,xr,yr,shotspeed*3)

				PlaySound2(shot_born_snd)




	# check triangle bond lines
	Local ll:le
	for ll:le = EachIn le_list
		if ll.attached is True:
			if ll.checked == False:
				ll.checked = True
				if ll.le2 != None:
					ll.le2.checked = True

				if linecollide2(ll.x,ll.y,ll.le2.x,ll.le2.y,px,py,12):
					Killplayer()
					Exit




	# sucked into blackholes
	Local n5:nme5
	for n5 in nme5_list:
		Local ddx: float = n5.x-px
		Local ddy: float = n5.y-py
		Local dist: float = sqrt(ddx*ddx + ddy*ddy)
		if dist < n5.sz * 10:  #effect from 4*10 upto 64*10
			ddx: float = ddx/dist/30*n5.sz # pull from 0 to 2.5
			ddy: float = ddy/dist/30*n5.sz # pull from 0 to 2.5
			px = px + ddx
			py = py + ddy





def BlackholeParticles()
	"""
	"""

	Local st: int = gcount % 2
	Local spin: float = 3
	if st == 0:
		spin = -3
	Local p:part
	Local t: int
	Local n5:nme5
	for n5 in nme5_list:
		if n5.active:
			for t = st To numparticles-1 Step 2
				p:part = partarray[t]
				if p.active > 0:
					Local ddx: float = n5.x-p.x
					Local ddy: float = n5.y-p.y
					Local dist: float = sqrt(ddx * ddx + ddy * ddy)
					if dist < n5.sz * 8 and dist > 8:
						#towards the gcenter
						if dist < n5.sz / 4:
							ddx: float = - ddx / dist
							ddy: float = - ddy / dist
							p.dx = p.dx + ddx / 2#.75
							p.dy = p.dy + ddy / 2#.75
							p.dx = p.dx + ddy / spin#.75# / dist/4
							p.dy = p.dy - ddx / spin#.75# / dist/4
						else:
							p.active +=  3
							ddx: float = ddx / dist
							ddy: float = ddy / dist
							p.dx = p.dx + ddx / 2#.75
							p.dy = p.dy + ddy / 2#.75
							p.dx = p.dx - ddy / spin#.75# / dist/4
							p.dy = p.dy + ddx / spin#.75# / dist/4

						Local speed: float = (p.dx*p.dx+ p.dy*p.dy)
						if speed > 12*12:
							Local sproot: float = sqrt(speed)
							p.dx = p.dx/sproot
							p.dy = p.dy/sproot





def UpdateAll(cnt: int = 0):

	Local n:nme
	Local n1:nme1
	Local n2:nme2
	Local n3:nme3
	Local n4:nme4
	Local n5:nme5
	Local n6:nme6
	Local n7:nme7
	Local n8:nme8
	Local g:ge
	Local ll:le
	Local s:shot
	Local pow:pu

	if gravityparticles:
		BlackholeParticles()

	CycleColours()
	CycleColours()

	score.UpdatePoints()

	trail.UpdateTrail()

	gridpoint.UpdateGrid()

	if cnt == 0:
		part.UpdateParticles()
	else:
		if cnt % 2 == 0:
			part.UpdateParticles()



	if not dying:
		#generators
		for g in ge_list:
			g.Update()

		#green squares
		for n in nme_list:
			n.Update()

		#pink pinwheel
		for n1 in nme1_list:
			n1.Update()

		#cyan diamonds
		for n2 in nme2_list:
			n2.Update()

		#purple cubes
		for n3 in nme3_list:
			n3.Update()

		#blue circles
		for n4 in nme4_list:
			n4.Update()

		# purple snakes
		for n6 in nme6_list:
			n6.Update()

		# red clone
		for n7 in nme7_list:
			n7.Update()

		# blue butterfly
		for n8 in nme8_list:
			n8.Update()

		#orange triangles
		for ll in le_list:
			ll.Update()

		#powerups
		for pow in pu_list:
			pow.Update()

		#red circles
		for n5 in nme5_list:
			n5.Update()

		#shots
		for s in SHOT_list:
			s.Update()




def DrawMessage():
	#DrawString(powerupscore, 10,30,3)
	if messtime > 0:
		messtime -= 1
		if messtime == 90:
			mess: str = "Power Up at "+ powerupscore
			mlen = Len(mess$)

		SetColor messtime,255-90+messtime/2,messtime
		DrawString(mess$, SCREENW/2-mlen*7,SCREENH-26,2.8)



def Drawall():
#if KeyDown(KEY_TAB): End
#if KeyDown(KEY_F8): return

	#Local p:part
	Local n:nme
	Local n1:nme1
	Local n2:nme2
	Local n3:nme3
	Local n4:nme4
	Local n5:nme5
	Local n6:nme6
	Local n7:nme7
	Local n8:nme8
	Local g:ge
	Local ll:le
	Local pow:pu
	Local t: int

	gridpoint.DrawGrid(g_style)

	SetOrigin 0,0

	DrawStars()

	score.DrawPoints()

	SetViewport 0,0,SCREENW,SCREENH
	SetScale 1,1
	SetAlpha 1

	trail.DrawTrail()

	part.DrawParticles()

	SetLineWidth 2

	for g in ge_list:
		g.Draw()

	#green squares
	SetColor COL_SQUARE_R,COL_SQUARE_G,COL_SQUARE_B
	for n in nme_list:
		n.Draw()

	#pink pinwheel
	SetColor COL_PIN_R,COL_PIN_G,COL_PIN_B
	for n1 in nme1_list:
		n1.Draw()

	#cyan diamonds
	SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
	for n2 in nme2_list:
		n2.Draw()

	#purple cubes
	SetColor COL_CUBE_R,COL_CUBE_G,COL_CUBE_B
	for n3 in nme3_list:
		n3.Draw()

	#blue circles
	SetColor COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B
	for n4 in nme4_list:
		n4.Draw()

	#red circles
	SetColor COL_SUN_R,COL_SUN_G,COL_SUN_B
	for n5 in nme5_list:
		n5.Draw()

	#snake
	for n6 in nme6_list:
		n6.Draw()

	#red clone
	SetColor COL_CLONE_R,COL_CLONE_G,COL_CLONE_B
	for n7 in nme7_list:
		n7.Draw()

	#blue butterflies
	SetColor COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B
	for n8 in nme8_list:
		n8.Draw()

	#orange triangles
	SetColor COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B
	for ll in le_list:
		ll.Draw()

	# bonds (orange to green)
	for ll in le_list:
		ll.DrawBond()

	#powerups
	for pow in pu_list:
		pow.Draw()

	SetScale 1,1
	SetLineWidth 2

	# draw player & men left yellow
	if py < 80:
		SetAlpha .5+Float(py)/400.0
	else:
		SetAlpha .80

	if numplayers > 1:
		SetColor 255,255,255
		DrawImage iconimage,SCREENW/2-16,19,0
		SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
		if numplayers > 2:
			drawstring(numplayers-1,SCREENW/2-48,10,3)

	if numbombs > 0:
		SetColor 255,255,255
		DrawImage iconimage,SCREENW/2+16,19,1
		SetColor COL_PLAYER_R,COL_PLAYER_G,COL_PLAYER_B
		if numbombs > 1:
			drawstring(numbombs,SCREENW/2+32,10,3)


	score.DrawScore()

	if py > SCREENH-80:
		SetAlpha 1-Float(py-(SCREENH-80))/400.0
	else:
		SetAlpha .80

	drawmessage()

	if not dying:
		DrawPlayer(px,py,pr)
		# draw shots
		shot.DrawAllShots()

	SetScale 1,1
	SetAlpha 1

	# draw border
	SetColor g_red,g_green,g_blue
	SetLineWidth 2.0
	DrawLine -gxoff,-gyoff,PLAYFIELDW-1-gxoff,-gyoff
	DrawLine -gxoff,-gyoff,-gxoff,PLAYFIELDH-1-gyoff
	DrawLine -gxoff,PLAYFIELDH-1-gyoff,PLAYFIELDW-1-gxoff,PLAYFIELDH-1-gyoff
	DrawLine PLAYFIELDW-1-gxoff,PLAYFIELDH-1-gyoff,PLAYFIELDW-1-gxoff,-gyoff




def DrawPlayer(x: int,y: int,r: int):

	Local sc: float
	if player_shield > 60 or ((player_shield) % 15 > 7)
		SetAlpha 0.48
		sc = 2.75 + Float(player_shield)/128
		SetScale sc,sc
		SetColor rcol,gcol,bcol
		SetOrigin px-gxoff,py-gyoff
		SetBlend ALPHABLEND
		DrawPoly circ
#	else:
#		SetAlpha 0.1
#		sc = .5
#		SetScale sc,sc

	SetOrigin 0,0
	SetScale 1,1
	SetAlpha 1
	SetBlend LIGHTBLEND
	SetColor 255,255,255
	SetRotation r
	DrawImage whiteplayer,x-gxoff,y-gyoff
	SetRotation 0




def SafeXY(x# Var,y# Var, plx: int,ply: int,range: int, close: int = 0)

	Local dx: float, dy: float, dist: float

	if x < 20:
		x = 20
	if y < 20:
		y = 20
	if x > PLAYFIELDW-20:
		x = PLAYFIELDW-20
	if y > PLAYFIELDH-20:
		y = PLAYFIELDH-20

	if close == 1:
		dx: float = plx-x
		dy: float = ply-y
		dist: float = sqrt(dx*dx + dy*dy) + 0.001
		while dist < range:
			x = x - dx/dist*10
			y = y - dy/dist*10
			dx = plx-x
			dy = ply-y
			dist = sqrt(dx*dx + dy*dy)
			if dist < 0.001
				x = plx + randint(10,20)*(1-2*randint(10)>5)
				y = ply + randint(10,20)*(1-2*randint(10)>5)
				dx = plx-x
				dy = ply-y
				dist = sqrt(dx*dx + dy*dy)


	else:
		dx: float = plx-x
		dy: float = ply-y
		dist: float = (dx*dx + dy*dy)
		while dist < range*range
			Local dir: float = randint(0,360*8)/8.0
			x = plx + Sin(dir)*range
			y = ply + Cos(dir)*range
			if x < 20:
				x = 20
			if y < 20:
				y = 20
			if x > PLAYFIELDW-20:
				x = PLAYFIELDW-20
			if y > PLAYFIELDH-20:
				y = PLAYFIELDH-20
			dx = plx-x
			dy = ply-y
			dist = (dx*dx + dy*dy)








def setup():
	pygame.init()
	screen: pygame.display = pygame.display.set_mode((640, 480))

	JoyCount()
	LoadConfig() # see control.bmx for more global settings
	LoadColours()
	GetGfx%es()
	FindSetting()
	SetController()
	SetupKeyTable()
	SetUp()
	LoadSounds()
	SeedRnd(MilliSecs())

	score.LoadScores()
	HideMouse()
	Main()
	ShowMouse()
	SaveConfig()
	SaveColours() # only needed once
	score.SaveScores()





def main():
	setup()

	tim: int
	tim2: int
	tim3: int
	tim4: int

	looper: int
	f: int
	done: bool = False

	part.CreateAll()

	FlushKeys()

	while not done:
		while playgame is False and done is False:
			StartMusic(0)
			if playgame is False and done is False:
				done = ShowTitle()
			if playgame is False and done is False:
				done = ShowScores()
			if playgame is False and done is False:
				done = ShowFriends()
			if playgame is False and done is False:
				done = ShowEnemies()

		if playgame and not done:
			if not cheat:
				valid = True
				nokillme = False

			StopMusic()
			RemoveAll(True)
			ResetGame()
			dying = True
			done = GetReady()
			dying = False
			Cls

			while gameover is not True or playgame is False:
				tim = MilliSecs()
				Spawn(gcount)
				UpdatePlayer()
				UpdateAll()
				tim2: int = MilliSecs()-tim
				DrawAll()
				tim3: int = MilliSecs()-tim

				if gameover:
					StopMusic()
					done = DoGameOver()
					playgame = False

				if cheat:
					DrawString("Update ms: "+tim2, 10,30,3)
					DrawString("Draw ms: " + (tim3 - tim2) , 10 , 50 , 3)
					DrawString("Last Frame ms: " + (tim4) , 10 , 70 , 3)
					Flip 1
					if KeyDown(KEY_P):
						pause: bool = True
						while pause:
							sleep(100)
							if KeyHit(KEY_O):
								pause = False
				else:
					Flip 1

				gcount += 1

				if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and controltype == 3 and bombtime == 0) or (JoyDown(j_d_option,joyport) and controltype == 0 and bombtime == 0)
					ret: int = Options(True)
					if ret > 0:
						done = True
						gameover = True
						if ret = 2:
							StopMusic()
							playgame = False
							done = False

					bombtime = 20

				tim4: int = MilliSecs() - tim
				if tim4 < 20 and tim4 > 0:
					sleep(20-tim4)

				Cls
			# Until gameover = True or playgame = False


			RemoveAll(True) # in case some sounds still playing and we quit
			if done == False:
				gxoff = 0
				gyoff = 0
				if pscore > lowesthiscore:
					StartMusic(2)
					f = score.GetHighScore()
					done = ShowScores(f)
					pscore = 0
					StopMusic()
				else:
					if pscore > 0:
						StartMusic(0);
						done = ShowScores(-20)



if __name__ == '__main__':
	main()
