

# red circles
Type nme5
	Field x#,y#,dx#,dy#,r#,sz#, active:Int
	Field absorbcount:Int,killer:Int=False
	Field sndchindex:Int
	Field move:Int
	Field gcenterx#
	Field gcentery#
	Field ex:Int = False
	Field pulse#
	
	Global sndindex:Int = 0
	
	def CreateDisplayEffect(x#, y#, size#)
		Local cnt:Int = CountList(NME5_LIST)
		if cnt > 15 Then return
		Local n:nme5 = New nme5
		n.x = x
		n.y = y
		n.sz = size
		n.gcenterx# = x
		n.gcentery# = y
		n.active = 1
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(1,4)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		NME5_LIST.AddLast( n )	
	
	
	def UpdateDisplayEffect()
		r = r + 1
		x = x + dx
		y = y + dy
		if x < 32
			dx = abs(dx)
			x = x + dx
		elif: x > SCREENW-32
			dx = -abs(dx)
			x = x + dx
		
		if y < 32
			dy = abs(dy)
			y = y + dy
		elif: y > SCREENH-32
			dy = -abs(dy)
			y = y + dy
		Endif 
		gcenterx# = x+Sin(r*2)*sz/2.5
		gcentery# = y+Cos(r*2)*sz/2.5
		if active
#			if r % 6 = 0
#				for Local pp:Int = 0 To 7	
#					part.Create(x+Sin(pp*45)*sz*3,y+Cos(pp*45)*sz*3, 7,rcol,gcol,bcol, r+pp*45,0)
#					
#			
			if r % 25 = 0
#				for Local pp:Int = 0 To 7	
#					part.Create(x+Sin(r)*sz*2+Sin(pp*45)*8,y+Cos(r)*sz*2+Cos(pp*45)*8, 7,rcol,gcol,bcol, 0,0)
#				
				for Local pp:Int = 0 To 7	
					part.Create(x+Sin(r)*sz*1.25+Sin(pp*45)*8,y+Cos(r)*sz*1.25+Cos(pp*45)*8, 7,rcol,gcol,bcol,0,0)
										
			
		
	
	
	
	def Create( x#, y#, size# ,freeze:Int, close:Int = 0 )
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local cnt:Int = CountList(NME5_LIST)
		if cnt > 3 Then return
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme5_born_snd,1, pan, vol)
		Local n:nme5 = New nme5
		n.sndchindex = sndindex
		sndindex:+1;if sndindex > 7 Then sndindex = 0
		n.x = x
		n.y = y
		n.gcenterx# = x
		n.gcentery# = y
		n.sz = size
		n.absorbcount = 0
		n.active = 0
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(.05,.5)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		NME5_LIST.AddLast( n )	
	
	
	def Update()
		if move > 0
			move:-1
			return
		
		r = r + 1
		x = x + dx
		y = y + dy
		if x < 16
			dx = abs(dx)
			x = x + dx
		elif: x > PLAYFIELDW-16
			dx = -abs(dx)
			x = x + dx
		
		if y < 16
			dy = abs(dy)
			y = y + dy
		elif: y > PLAYFIELDH-16
			dy = -abs(dy)
			y = y + dy
		Endif 
		gcenterx# = x+Sin(r*3)*sz/2.5
		gcentery# = y+Cos(r*3)*sz/2.5
		if active Then gridpoint.Pull(x,y,5+sz/2) #/3
 		DoubleSun()				
		Local distx# = x-px
		Local disty# = y-py
		Local dist# = (distx * distx + disty * disty)
		if dist < (12+sz/2)*(12+sz/2)+12*12
			killer = True		
			if KillPlayer() Then NME5_LIST.Remove(Self)
		

		if active
			if r % 60 = 0
#				for Local pp:Int = 0 To 7	
#					part.Create(x+Sin(pp*45)*sz*3,y+Cos(pp*45)*sz*3, 7,rcol,gcol,bcol, r+pp*45,0)
#				
				for Local pp:Int = 0 To 7	
					part.Create(x+Sin(r)*sz*1.15+Sin(r+pp*45)*3,y+Cos(r)*sz*1.15+Cos(r+pp*45)*3, 7,rcol,gcol,bcol,r+pp*45)
					
			
			if r % 25 = 0 # 2 times per second
				if sunloopchan[sndchindex] <> Null
					Local pan# = (x-px)/PLAYFIELDW
					Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
					SetPanAndVolume(sunloopchan[sndchindex], pan, vol)
				
									
		
	
	
	def DoubleSun()
		Local n5:nme5
		for n5:nme5 = EachIn NME5_LIST
			if n5 <> Self
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y
				Local mag# = (n5.sz-sz)/8
				if mag < 1 Then mag = 1
				if mag > 8 Then mag = 8
				Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001		
				if dist < (n5.sz*2+sz*2) + 64
					ddx# = ddx/dist*mag
					ddy# = ddy/dist*mag
					if dist < n5.sz+sz
						ddx# = -ddx# - ddy#*.25
						ddy# = -ddy# - ddx#*.25
					
					dx = dx + ddx
					dy = dy + ddy
					Local speed# = Sqr(dx*dx+dy*dy)
					if speed > speed_nme5
						dx = dx/speed*speed_nme5
						dy = dy/speed*speed_nme5
					
				
			
		
	
			
	def Kill(points:Int=True)
		Local t:Int, rate#
		if active = False
			active = True
			if sunloopchan[sndchindex] <> Null
				StopChannel(sunloopchan[sndchindex])
			
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			sunloopchan[sndchindex] = PlaySound2(nme5_loop_snd,1, pan, vol)
			gridpoint.Push(x,y,6,1)
		
		sz = sz - 0.75 # sz goes from 4 to 64
		rate = sz/16
		if sunloopchan[sndchindex] <> Null Then SetChannelRate( sunloopchan[sndchindex], rate# )
		if points = False Then sz = 0
		for t = 0 To 3
			part.Create(x,y, 0 ,COL_SUN_R,COL_SUN_G,COL_SUN_B)	
		
		if sz < 4
			#gridpoint.pull(x,y,16,10)
			gridpoint.Push(x,y,8,2)									
			if sunloopchan[sndchindex] <> Null Then StopChannel(sunloopchan[sndchindex])
			NME5_LIST.Remove(Self)
			for t = 0 To 31
				part.Create(x,y, 0 ,COL_SUN_R,COL_SUN_G,COL_SUN_B)	
			
			if points
				Local sc:Int = 150
				sc:+ absorbcount*(absorbcount+1)/3*5
				score.IncScore(x,y,sc)			
			
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme5_killed_snd,1, pan, vol)			
		else:
			Local freq# = 1.1+(64-sz)/64
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme5_shrink_snd, freq, pan, vol)						
		
	
	
	def Grow(amnt#=1)
		Local t:Int,rate#
		Local speedup#,xx:Int,yy:Int
		
		absorbcount:+1
		speedup = 1+Float(gcount/(50*60*6)) #increase by 1 every 6 minutes
		if speedup > 5 Then speedup = 5
		sz = sz + amnt*speedup
		
		rate = sz/16
		if active = False
			active = True
			if sunloopchan[sndchindex] <> Null
				StopChannel(sunloopchan[sndchindex])
						
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			sunloopchan[sndchindex] = PlaySound2(nme5_loop_snd, 1, pan, vol)	
			gridpoint.Push(x,y,6,1)						
		
		if sunloopchan[sndchindex] <> Null Then SetChannelRate( sunloopchan[sndchindex] , rate# )		
		if sz > 64
			if sunloopchan[sndchindex] <> Null Then StopChannel(sunloopchan[sndchindex] )		
			for t = 0 To 15
				xx= x+Cos(t*22.5)*20
				yy= y+Sin(t*22.5)*20
				nme4.Create(xx,yy,4,1,1)	# 1=mean - move faster
						
			for t = 0 To 17
				xx= x+Cos(t*20)*30
				yy= y+Sin(t*20)*30
				nme8.Create(xx,yy,4,1)	
						
			NME5_LIST.Remove(Self)			
			for t = 0 To 35
				part.Create(x+Sin(t*10)*20,y+Cos(t*10)*20, 0 ,COL_SUN_R,COL_SUN_G,COL_SUN_B)	
			
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme5_explode_snd, 1, pan, vol)							
		else:
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme5_grow_snd, 1, pan, vol)							
				
	
	
	
	def Draw()
	
		Local szz# = .25+sz/64	
		SetColor COL_SUN_R,COL_SUN_G,COL_SUN_B
		SetOrigin x-gxoff,y-gyoff
		SetBlend ALPHABLEND
		Local sc# = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale Float(move)/5.0,Float(move)/5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc+sz/16,sc+sz/16
		
		DrawPoly circ
		if active = True
			pulse = pulse + sz/2
			szz = szz + Cos(pulse)/6
		
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale szz,szz	
		SetBlend lightblend
		DrawImage redcircle,x-gxoff,y-gyoff
		SetScale 1,1
		return




