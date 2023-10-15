
# pink pinwheel
Type nme1
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field move:Int

	def Create:nme1( x#, y# ,freeze:Int, close:Int = 0)
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme1_born_snd,1, pan, vol)
		Local dir:Int,mag#
		Local n:nme1 = New nme1
		n.x = x
		n.y = y
		n.r = 90 #Rand(0,359)
		dir = Rand(0,359)
		mag# = Rnd(.5,2.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		NME1_LIST.AddLast( n )	
		return n

	
	def Update()
		Local othern:nme1
		Local dist#,distx#,disty#
		
		if move > 0
			move:-1
			return
		
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
		#Toward(px,py,400)
		BlackHole()
		for othern:nme1 = EachIn NME1_LIST
			if othern <> Self
				distx# = othern.x-x
				disty# = othern.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 20*20  + 20*20
					dx = dx - Sgn(distx)
					dy = dy - Sgn(disty)
				
			
				
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed > speed_nme1
			dx = dx/speed*speed_nme1
			dy = dy/speed*speed_nme1
		
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 24*24
			killer = True
			if KillPlayer() Then NME1_LIST.Remove(Self)
					
	

	def blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn NME5_LIST
			if n5.active
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75+n5.sz*8
					dx = dx + ddx/dist/512*(1200-dist)
					dy = dy + ddy/dist/512*(1200-dist)
					if dist < 12+n5.sz/2
						Kill(False)
						n5.Grow(1)
						Exit
					
				
			
		
	
	
#	def Toward(xx#,yy#,range:Int)
#		Local ddx# = xx-x
#		Local ddy# = yy-y 
#		Local dist# = Sqr(ddx*ddx + ddy*ddy)
#		if dist < range and dist > 16
#			dx = dx + ddx/dist*32
#			dy = dy + ddy/dist*32
#		
#	
		
	def Kill(points:Int=True)
		if points
			score.IncScore(x,y,25)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhitsound,1, pan, vol)			
				
		for Local t:Int = 0 To 15
			part.Create(x,y,6 ,COL_PIN_R,COL_PIN_G,COL_PIN_B,r)	
		
		gridpoint.Shockwave(x,y)
		NME1_LIST.Remove(Self)				
	

	def Draw()		
		Local sc#
		Local sqa#[]=[0.0,12.0, 12.0,0.0, 0.0,-12.0, -12.0,0.0]
		SetColor COL_PIN_R,COL_PIN_G,COL_PIN_B
		SetBlend ALPHABLEND
		SetOrigin x-gxoff,y-gyoff
		SetRotation(r*4+45)
		sc = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale Float(move)/5.0,Float(move)/5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc,sc
		
		DrawPoly sqa
		
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		SetRotation(r*4)
		DrawImage pinkpinwheel,x-gxoff,y-gyoff
		SetRotation 0		
		return
