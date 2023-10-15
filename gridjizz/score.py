class score:
	Field x:Int,y:Int,s$,life:Int
	
	def __init__(self, s: str, x: int, y: int, l: int = 0):
		Local sc:score = New score
		sc.x = x
		sc.y = y
		sc.s$ = s$
		sc.life = 30+l*20
		score_list.AddLast( sc )


	def UpdatePoints(self):
		Local sc:score
		for sc:score = EachIn score_list
			sc.life:-1
			if sc.life <= 0 Then score_LIST.Remove(sc)	
			
	
	
	def DrawPoints(self):
		Local sc:score
		
		SetBlend lightblend		
		SetScale 1,1
		SetAlpha 1
		SetLineWidth 2.0
		for sc:score = EachIn score_list
			Local cc%
			cc = 75 + sc.life * 10
			if cc > 255 Then cc = 255
			SetColor cc,cc,32
			Drawstring (sc.s$,sc.x-gxoff-sc.life,sc.y-gyoff-16,1+Float(sc.life)/12.0)
			
		SetAlpha 1
	
				
	def ResetMultiplier(self):
		multiplier = 1
		killcount = 0
		# set back powerupscore to just above current
		powerupscore = pscore + POWERUP*2
		powerupscore = Int(powerupscore/POWERUP/2)*POWERUP*2
		messtime = 180
		mess$ = "Power Up at "+ powerupscore
		mlen = Len(mess$)
	

	def ResetScore(self):
		lowesthiscore = scores[9,startingdifficulty]
		hiscore = scores[0,startingdifficulty]	
		pscore = 0
	
	
	def IncScore(x:Int,y:Int,amt:Int,m:Int=True)

		Local s$	
		pscore = pscore + amt*multiplier
		s$ = amt*multiplier
		if m Then score.create(s$,x,y)
		
		if m Then killcount:+1
		if multiplier < 10
			if killcount >= multiplieramount[multiplier-1] #0-9
				multiplier:+1
				PlaySound2(multiplier_increase_snd)
				s$ = multiplier+"X Multiplier"
				score.create(s$,px-13*6,py-32,True)
			Endif 	
		
		if pscore >= extralifecount*EXTRALIFE
#			numplayers:+1
			extralifecount:+1
			PlaySound2(extra_life_snd)
#			s$ = "Extra Life"
#			score.create(s$,px-10*6,py-32,True)
			if numplayers < 10 Then pu.MakePowerup(4)
		Endif 	
		if pscore >= extrabombcount*EXTRABOMB 
#			numbombs:+1
			extrabombcount :+1
			PlaySound2(extra_bomb_snd)
#			s$ = "Extra Bomb"
#			score.create(s$,px-10*6,py-32,True)
			if numbombs < 9 Then pu.MakePowerup(5)
		Endif 		
		if pscore >= powerupscore
			pu.MakePowerUp()
			powerupscore:+POWERUP*multiplier*multiplier
			PlaySound2(bonus_born_snd)
		Endif 	
		if pscore > hiscore
			hiscore = pscore
		
		
	
	
	def DrawScore()
		# draw scores
		SetColor COL_SCORE_R,COL_SCORE_G,COL_SCORE_B	
		DrawString("SCORE: "+pscore, 10,10,3)
		DrawString("HISCORE: " + hiscore, SCREENW-260,10,3)
		DrawString(multiplier+"X", 240,10,2.5)			
		if debug Then DrawString(gcount, 300,10,3)			
	
	
	
	def GetHighScore:Int()
	if Not valid Then return -20
	
		Local slot:Int = 0, t:Int
		Local name$
		Local done:Int = False
		Local ignoreyjoy:Int
		Local ignorefyjoy:Int
		Local ignorexjoy:Int
		Local tim:Int

		gxoff = 0
		gyoff = 0

		bombtime = 20
		PlaySound2(high_score_snd)
		Local playtime$ = GetPlayTime(gcount)
		FlushKeys()
		FlushMouse()
		while done = False
			Cls
			tim = MilliSecs()
			
			jdfy = GetJoyByAxis(joyport, axis_fire_y, axis_fire_y_inv, axis_fire_y_sc, axis_fire_y_center ) 
			jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )	
			jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )	
			if abs(jdfy) < 0.3 Then jdfy = 0 
			if abs(jdmy) < 0.3 Then jdmy = 0
			if abs(jdmx) < 0.3 Then jdmx = 0
			if jdfy = 0 Then ignorefyjoy = False
			if jdmy = 0 Then ignoreyjoy = False
			if jdmx = 0 Then ignorexjoy = False			
			if ignoreyjoy = True and bombtime > 0 Then jdmy = 0 
			if ignorefyjoy = True and bombtime > 0 Then jdfy = 0 
			if ignorexjoy = True and bombtime > 0 Then jdmx = 0			
			if KeyDown(KEY_UP) and bombtime = 0 Then jdmy =-1
			if KeyDown(KEY_DOWN) and bombtime = 0 Then jdmy = 1			
			if KeyHit(KEY_LEFT) Then jdmx =-1
			if KeyHit(KEY_RIGHT) Then jdmx = 1
			if jdmy <> 0 Then ignoreyjoy = True
			if jdfy <> 0 Then ignorefyjoy = True
			if jdmx <> 0 Then ignorexjoy = True
			
			if KeyDown(KEY_RSHIFT) Or KeyDown(KEY_LSHIFT)
				for Local kk:Int = 48 To 90
					if KeyHit(kk)
						#FlushKeys()
						letter[slot]=kk
						jdmx = 1						
						Exit
					
				
			else:
				for Local kk:Int = 48 To 90
					if KeyHit(kk)
						#FlushKeys()
						if kk >= 65 and kk <= 65+26
							letter[slot]=kk+32
							jdmx = 1
						else:
							letter[slot]=kk
							jdmx = 1
						
						Exit
					
								
			
			if KeyHit(KEY_SPACE)
				letter[slot] = 32
				jdmx = 1
			

			if jdfy <> 0 
			   PlaySound2(quarkhitsound) 
			   if letter[slot] > 64 and letter[slot] < 91 Then 
			         letter[slot] = letter[slot] + 32 
			   else: if letter[slot] > 96 and letter[slot] < 123 Then 
			         letter[slot] = letter[slot] - 32 
			   End if 
			   bombtime = 15 
			Endif 
			    
			if jdmy < 0 
			   letter[slot] = letter[slot] - 1 
			   PlaySound2(quarkhitsound) 
			   if letter[slot] = 32 Then 
			         letter[slot] = 126 
			   else: if letter[slot] = 64 Then 
			         letter[slot] = 32 
			   else: if letter[slot] < 32 Then 
			         letter[slot] = 64 
			    
			   else: if letter[slot] = 96 Then 
			         letter[slot] = 32 
			   else: if letter[slot] = 122 Then 
			         letter[slot] = 96 
			   End if 
			   bombtime = 8 
			Endif 
			if jdmy > 0 
			   letter[slot] = letter[slot] + 1 
			   PlaySound2(quarkhitsound) 
			   if letter[slot] > 126 Then 
			         letter[slot] = 33 
			   else: if letter[slot] = 65 Then 
			         letter[slot] = 32 
			   else: if letter[slot] = 33 Then 
			         letter[slot] = 65 
			    
			   else: if letter[slot] = 123 Then 
			         letter[slot] = 91       
			   else: if letter[slot] = 97 Then 
			         letter[slot] = 123 
			   End if 
			
			   bombtime = 8             
			Endif 
			if jdmx < 0
				slot = slot - 1
				PlaySound2(quarkhitsound)
				if slot < 0 Then slot = 7
				bombtime = 15				
			
			if jdmx > 0
				slot = slot + 1
				PlaySound2(quarkhitsound)
				if slot > 7 Then slot = 0
				bombtime = 15				
			
						
			SetColor 255,255,255
			DrawString("Congratulations!", SCREENW/2-250,SCREENH/2-240,3)
			DrawString("You are in the top 10.",SCREENW/2-250,SCREENH/2-200,3)
			DrawString("Difficulty Level: "+difficulty$[laststartingdifficulty],SCREENW/2-250,SCREENH/2-160,3)
			SetColor 0,255,0
			DrawString("Score: " + pscore, SCREENW/2-200,SCREENH/2-80,3)
			DrawString("Time:  " + playtime$, SCREENW/2-200,SCREENH/2-40,3)
			DrawString("Name:  " + name$, SCREENW/2-200,SCREENH/2,3)
			for t = 0 To 7
				if slot = t
					SetColor 255,255,0
				else:
					SetColor 0,255,0
				
				DrawLine SCREENW/2-200+7*15+t*15,SCREENH/2+22,SCREENW/2-200+7*15+t*15+12,SCREENH/2+22
			
			SetColor 255,255,255		
			DrawString("Up and Down to select letter,",SCREENW/2-250,SCREENH/2+80,3)
			DrawString("Left and Right to select position.",SCREENW/2-250,SCREENH/2+120,3)
			DrawString("Press Enter when done.",SCREENW/2-250,SCREENH/2+160,3)
			name$ = ""
			for t = 0 To 7
				name$:+ Chr$(letter[t])
			
			if Rand(0,100) > 90 Then part.CreateFireworks(2)
			part.UpdateParticles()
			part.DrawParticles()		
			Flip 1
			tim = MilliSecs() - tim
			if tim < 20 and tim > 0
				Delay 20-tim
			
			
			bombtime = bombtime - 1
			if bombtime < 0 Then bombtime = 0
			
			if KeyHit(KEY_ENTER) Or MouseHit(m_bomb) Or ..
				(JoyDown(j_pad_bomb,joyport) and controltype = 3 and bombtime = 0) Or ..
				(JoyDown(j_d_bomb,joyport) and controltype = 0 and bombtime = 0)				
				bombtime = 20
				done = True		
			
						
		
		return insertscore(pscore, name$, playtime$,score.GetSettings(), laststartingdifficulty)
	
	
	def GetSettings$()
		Local ret$ = ""
		#game version
		ret$:+ g_v_num$ +","		
		#screen size
		ret$:+ gfxmodearr[screensize].s$+","
		#play size	
		ret$:+ playfieldsizes[playsize*2]+"X"+playfieldsizes[playsize*2+1]+","
		#control type
		if controltype > 2
			ret$:+ control_method[controltype]
			if controltype = 3
				ret$:+ "-"+j_config+","
			
			if controltype = 4
				ret$:+ "-"+h_config+","
			
		else:
			ret$:+ control_method[controltype]+","
		
		#scroll
		ret$:+ scroll +","		
		#gfx set
		ret$:+ gfxset +","		
		#grid style
		ret$:+ g_style +","		
		#autofire
		ret$:+ autofire +","		
		#inertia
		ret$:+ Int(inertia*100)
					
		return ret$
	
	
	def CalcChecksum:Int(sc:Int, tm$, n$, set$)
		Local pad:Int = 0
		Local st$ = sc+n$+tm$+set$
		 
		for Local tt:Int = 0 To Len(st$)-1
			pad = pad + st$[tt]
		
		
		return pad	
	
	
	def InsertScore:Int(sc:Int,name$,tm$, set$, tb:Int)
		# find position
		# shift others down
		# and insert new score
		Local minpos:Int=10
		Local t:Int
		for t = 9 To 0 Step -1
			if sc > scores[t,tb] Then minpos=t
		
		for t = 9 To (minpos+1) Step -1
			scores[t,tb]=scores[t-1,tb]
			names[t,tb]=names[t-1,tb]
			playtimes[t,tb]=playtimes[t-1,tb]
			scoresetting$[t,tb] = scoresetting$[t-1,tb] 
			checksum[t,tb] = checksum[t-1,tb]
		
		scores[minpos,tb]= sc
		playtimes$[minpos,tb]= tm$
		names$[minpos,tb]= name$
		scoresetting$[minpos,tb] = set$ 
		checksum[minpos,tb] = score.CalcChecksum(sc, tm$, name$, set$)
		lowesthiscore = scores[9,tb]
		return minpos
		
	
	
	
	
	def LoadScores()
		Local tb:Int	
		Local t:Int
		Local fh:TStream = OpenFile("hiscores.dat")
		if fh = Null
			# if score file not found use the default
			score.SetDefault()
		else:
			for tb = 0 To 2
				for t = 0 To 9
					scores[t,tb] = Int(ReadLine(fh))
					playtimes[t,tb] = ReadLine(fh)
					names$[t,tb] = ReadLine(fh)
					scoresetting$[t,tb] = ReadLine(fh)
					checksum[t,tb] = Int(ReadLine(fh))
				
					
			CloseFile fh
		
		score.ValidateScores()
	

	def ValidateScores()
		Local tb:Int
		Local t:Int
		Local pad:Int
		Local dirtyscores:Int = False
		
		for tb = 0 To 2
			for t = 0 To 9
				pad = score.CalcChecksum(scores[t,tb],playtimes[t,tb],names$[t,tb],scoresetting$[t,tb])
				if pad <> checksum[t,tb]
					dirtyscores = True
				Endif 
			
		
		if dirtyscores Then score.SetDefault()
		
	
			
	def SetDefault()
	
		Local tb:Int	
		Local t:Int
		for tb = 0 To 2
			for t = 0 To 9
				if tb = 0 Then scores[t,tb]= (200000-t*19000)
				if tb = 1 Then scores[t,tb]= (100000-t*9000)
				if tb = 2 Then scores[t,tb]= (50000-t*4900)				
				playtimes[t,tb] = GetPlayTime(50*60*11-t*50*40-tb*50*60*2)
				names$[t,tb]= "Mark Inc"
				scoresetting$[t,tb] = "0,0,0,0,0,0,0,0,0,0"
				checksum[t,tb] = score.CalcChecksum(scores[t,tb],playtimes[t,tb],names$[t,tb],scoresetting$[t,tb])
			
			
	

	def SaveScores()
		# write the scores out to file
		Local tb:Int
		Local t:Int
		Local fh:TStream = WriteFile("hiscores.dat")
		if fh <> Null
			for tb = 0 To 2
				for t = 0 To 9
					WriteLine(fh,scores[t,tb])
					WriteLine(fh,playtimes[t,tb])
					WriteLine(fh,names$[t,tb])
					WriteLine(fh,scoresetting$[t,tb])
					WriteLine(fh,checksum[t,tb])
				
			
			CloseFile fh
