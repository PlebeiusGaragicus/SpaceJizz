


#powerups
class pu:
	Field x#,y#,dx#,dy#,r#,kind:Int
	Field move:Int, life:Int, die:Int
	
	def Create( x#, y#, kind:Int, freeze:Int )
		Local n:pu = New pu
		n.x = x
		n.y = y
		n.kind = kind
		n.life = 0
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(.5,2.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		POWERUP_LIST.AddLast( n )	
	
	
	def Update()
		Local otherpu:pu
		Local distx#
		Local disty#
		Local dist#
		Local t:Int

		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 20*20 + 16*16
			PowerUp()
			die = True 
		
				
		if move > 0
			move:-1
			return
		
		life:+1
		r = r + 1
		x = x + dx
		y = y + dy
		if x < 8 
			dx = abs(dx)
			x = x + dx
		elif: x > PLAYFIELDW-8
			dx = -abs(dx)
			x = x + dx
		
		if y < 8
			dy = abs(dy)
			y = y + dy
		elif: y > PLAYFIELDH-8
			dy = -abs(dy)
			y = y + dy
		Endif 
		if Not die Then blackhole()
		if Rand(0,100) > 96 Then Toward(px,py,PLAYFIELDW)
		if life > 10*20
			if kind > 1
				for otherpu:pu  = EachIn POWERUP_LIST
					if otherpu<> Self and otherpu.kind > 1
						distx# = otherpu.x-x
						disty# = otherpu.y-y
						dist# = (distx * distx + disty * disty)
						if life > 15*20
							#towards
							dx = dx + Sgn(distx)/64
							dy = dy + Sgn(disty)/64
							otherpu.dx:- Sgn(distx)/64
							otherpu.dy:- Sgn(disty)/64					
						
						if dist < 16*16 + 16*16
							#merge
							#otherpu.move = 200
							POWERUP_LIST.Remove(otherpu)
							die = True
							ge.Create( x, y, 10, 20, 20, 20)
							for t = 0 To 7
								part.Create(x,y, 0 ,COL_POWERUP_R,COL_POWERUP_G,COL_POWERUP_B)
								
						
					
				
			else:
				# back and side shooters disappear 
				if life > 20*20
					die = True
					nme8.Create( x, y, 30)
					for t = 0 To 7
						part.Create(x,y, 0 ,COL_POWERUP_R,COL_POWERUP_G,COL_POWERUP_B)
						
				
			
		
		Local speed# = Sqr(dx*dx+dy*dy)+0.001
		if speed > 4 
			dx = dx/speed*4
			dy = dy/speed*4
		
			
		if die Then POWERUP_LIST.Remove(Self)
	

	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn NME5_LIST
			if n5.active			
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75+n5.sz*5
					dx = dx + ddx/dist/4096*(400-dist)
					dy = dy + ddy/dist/4096*(400-dist)
					if dist < 12+n5.sz
						Kill()
						n5.Grow(1)
						Exit
					
				
			
		
	
				
	def Toward(xx#,yy#,range#)
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range
			dx = dx + ddx/dist
			dy = dy + ddy/dist
		
	
#	
	def Kill()
		for Local t:Int = 0 To 14
			part.Create(x,y, 2 ,COL_POWERUP_R,COL_POWERUP_G,COL_POWERUP_B,t*24+r)	
		
		POWERUP_LIST.Remove(Self)				
	

	def Draw()
		SetAlpha 1
		SetScale 1,1
		SetRotation 0
		SetBlend LIGHTBLEND
		SetColor 255,255,255
		if life > 18*20	
			SetColor 180,80,200
		
		Select kind
			Case 0 #back shooter
				DrawImage powerimage,x-gxoff,y-gyoff,2
			Case 1 #side shooters
				DrawImage powerimage,x-gxoff,y-gyoff,3
			Case 2 #Xtra Bullet B
				DrawImage powerimage,x-gxoff,y-gyoff,0
			Case 3 #shot speed  ->
				DrawImage powerimage,x-gxoff,y-gyoff,5
			Case 4 #Free ship    X
				DrawImage powerimage,x-gxoff,y-gyoff,6		
			Case 5 #Free bomb
				DrawImage powerimage,x-gxoff,y-gyoff,8
			Case 6 #shield
				DrawImage powerimage,x-gxoff,y-gyoff,9
			Case 7 #supershots
				DrawImage powerimage,x-gxoff,y-gyoff,7
			Case 8 #bouncyshots
				DrawImage powerimage,x-gxoff,y-gyoff,10
		End Select
		SetBlend LIGHTBLEND	
		SetColor rcol,gcol,bcol
		if life > 15*20	
			SetColor 180,80,200
		
		SetOrigin 0,0
		SetRotation(life*6)
		DrawImage whitestar,x-gxoff,y-gyoff
		SetRotation 0
		SetScale 1,1
		SetOrigin 0,0
					
	
	
	def PowerUp()
		Select kind
			Case 0 #back shooter
				shot_back:+ 20*upgradetime 
				mess$ = "Reverse Shooter"
				mlen = 15
			Case 1 #side shooters			
				shot_side:+ 20*upgradetime 
				mess$ = "Side Shooters"
				mlen = 13
			Case 2 #Bullet B
				numshots:+1
				if numshots > 4
					numshots = 4
					mess$ = "2000 Points!"				
					mlen = 12
					score.IncScore(x,y,2000,0)
				else:
					mess$ = "Extra Cannon"				
					mlen = 12
				
			Case 3 #Shot Speed   S
				shotspeed:+1
				if shotspeed > 5
					shotspeed = 5
					mess$ = "2000 Points!"				
					score.IncScore(x,y,2000,0)
					mlen = 12
				else:
					mess$ = "Faster Shots"
					mlen = 12
				
			Case 4 #Free ship    X
				if numplayers > 9
					mess$ = "2000 Points!"				
					score.IncScore(x,y,2000,0)
					mlen = 12
				else:
					numplayers:+1
					mess$ = "Extra Player"
					mlen = 12
				
			Case 5 #bomb
				if numbombs > 8
					mess$ = "2000 Points!"				
					score.IncScore(x,y,2000,0)
					mlen = 12
				else:
					numbombs:+1
					mess$ = "Extra Bomb"
					mlen = 10
				
			Case 6 #shield
				player_shield:+ 20*upgradetime 
				if player_shield > 20*upgradetime*2 Then player_shield = 20*upgradetime*2
				mess$ = "Shield"
				mlen = 6
			Case 7 #super shots
				supershots:+ 20*upgradetime 
				mess$ = "Super Shots"
				mlen = 15
			Case 8 #Bouncy shots
				bouncyshots:+ 20*upgradetime 
				mess$ = "Bouncy Shots"
				mlen = 15
		End Select
		score.create(mess$,x-mlen*6,y-8,True)
#		messtime = 180
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(pu_collect_snd, 1, pan, vol)	
	
	
	def MakePowerUp(tp:Int=-1)
		Local x:Int,y:Int,k:Int
	
		x = Rand(250,PLAYFIELDW-250)
		y = Rand(150,PLAYFIELDH-150)
	
		# figure out what#s needed based on
		# numplayers, numbombs   
		# numshots   (1-4)
		# shotspeed  (3-5)
	
		# can always be 0,1
		# if bullets needed then 2
		# if speed needed then 3
		# if low on men then 4
		# if low on bombs then 5
		k = Rand(0,1)
		if Rand(0,100) > 80
			k = 6#shield
			if Rand(0,100) > 45 Then k = 7 + Rand(0,1) #supershots or bouncy shots
					
		if shotspeed < 5
			# need more shot speed!
			if Rand(1,shotspeed) < 2  #2/3 to 2/5
				k = 3
			
		
		if numshots < 4
			# need more bullets!
			if Rand(1,numshots) = 1 #1-1 to 1-6
				k = 2
			
		
		if k < 2 and Rand(0,100) > 40 # ie not bullet or speed
			if numplayers < 2
				k = 4
			elif: numbombs < 2
				k = 5
			
		
		if tp <> -1 Then k = tp
		pu.Create(x,y,k,2)	
		gridpoint.Push(x,y,6,1)
