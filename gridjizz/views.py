
"""
These appear to be intro screens
"""



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
		tim = time()
		if randint(0,100) > 94 and counter < 850:
			part.CreateFireworks(1)

		part.UpdateParticles(1)
		part.DrawParticles()
		BlackholeParticles()

		#red circles
		for n5 in NME5_LIST:
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
		tim = time() - tim
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
		tim = time()
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
		tim = time() - tim
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
		tim = time()
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
		tim = time() - tim
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
		tim = time()
		CycleColours()
		if tcounter > 350:
			if randint(0,100) > 90 and counter < 850:
				part.CreateFireworks(0)
			part.UpdateParticles(1)
			part.DrawParticles()
			BlackholeParticles()
			#red circles
			for Local n5 in NME5_LIST:
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
		tim = time() - tim
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
