

#blue circles
Type nme4
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field move:Int
	Field mean:Int 
	
	def Create:nme4( x# , y# , freeze:Int , m:Int = 0, close:Int = 0)
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme4_born_snd,1, pan, vol)									
		Local n:nme4 = New nme4
		n.x = x
		n.y = y
		n.mean = m
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(3.0,6.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		NME4_LIST.AddLast( n )	
		return n
	
	
	def Update()
		if move > 0
			move:-1
			return
		
		Local distx#
		Local disty#	
		Local dist#
		Local othern4:nme4
		Local speed#
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
		Toward(px,py,PLAYFIELDW)
		blackhole()
		for othern4:nme4 = EachIn NME4_LIST
			if othern4 <> Self
				distx# = othern4.x-x
				disty# = othern4.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 24*24 + 20*20
					dx = dx - Sgn(distx)
					dy = dy - Sgn(disty)
				
			
		
		speed# = Sqr(dx*dx+dy*dy)
		if speed > (speed_nme4+mean)
			dx = dx/speed*(speed_nme4+mean)
			dy = dy/speed*(speed_nme4+mean)
		
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 12*12 + 12*12
			killer = True		
			if KillPlayer() Then NME4_LIST.Remove(Self)
		
	

	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn NME5_LIST
			if n5.active
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75+n5.sz*6
					dx = dx + ddx/dist/1024*(700-dist)
					dy = dy + ddy/dist/1024*(700-dist)
					if dist < n5.sz/2
						Kill(False)
						n5.Grow(1)
						Exit
					
				
			
		
	
			
	def Toward(xx#,yy#,range1:Int)
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range1 
			dx = dx + ddx/dist*4
			dy = dy + ddy/dist*4
		
	
	
	def Kill(points:Int=True)
		if points
			score.IncScore(x,y,10)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhitsound,1, pan, vol)
		
		for Local t:Int = 0 To 15
			part.Create(x,y, 2 ,COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B,t*24+r)	
		
		gridpoint.Shockwave(x,y)
		NME4_LIST.Remove(Self)				
	

	def Draw()
		SetColor COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B
		SetOrigin x-gxoff,y-gyoff
		SetBlend ALPHABLEND
		Local sc# = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale Float(move)/5.0,Float(move)/5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc,sc
		
		DrawPoly circ
	
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		DrawImage bluecircle,x-gxoff,y-gyoff
		return
