
# blue diamonds
Type nme2
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field move:Int

	def Create:nme2( x#, y#,freeze:Int, close:Int = 0 )
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme2_born_snd,1, pan, vol)			
		Local dir:Int, mag#
		Local n:nme2 = New nme2
		n.x = x
		n.y = y
		n.r = Rand(0,359)
		dir = Rand(0,359)
		mag# = Rnd(.25,1.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		NME2_LIST.AddLast( n )	
		return n

	
	def Update()
		Local othern:nme2,distx#,disty#,dist#
		if move > 0
			move:-1
			return
		
		r = r + 1
		x = x + dx
		y = y + dy
		if Rand(0,1) Then dx = dx + Rand(-0.2,0.2);dy = dy + Rand(-0.2,0.2)
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
		blackhole()
		Toward(px,py,PLAYFIELDW)
		for othern:nme2 = EachIn NME2_LIST
			if othern <> Self
				distx# = othern.x-x
				disty# = othern.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 30*30 + 20*20
					dx = dx - Sgn(distx)
					dy = dy - Sgn(disty)
				
			
				
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed > speed_nme2
			dx = dx/speed*speed_nme2
			dy = dy/speed*speed_nme2
		

		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 24*24
			killer = True		
			if KillPlayer() Then NME2_LIST.Remove(Self)	
		
	

	def Blackhole()
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
					
				
			
		
	
		
	def Toward(xx#,yy#,range:Int)
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range
			dx = dx + ddx/dist/2
			dy = dy + ddy/dist/2
		
	
	
	def Kill(points:Int=True)
		if points
			score.IncScore(x,y,50)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhitsound,.98, pan, vol)						
		
		for Local t:Int = 0 To 15
			part.Create(x+Rand(-8,8),y+Rand(-8,8),3 ,COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B)	
		
		gridpoint.Shockwave(x,y)
		NME2_LIST.Remove(Self)				
	

	def Draw()
	
		Local sc%,scy#,scx#
		sc = r % (256)
		if sc > 127
			scy = sc-127
			if sc > 127+63 Then scy = 255-sc
			scx = 0
		else:
			scx = sc
			if sc > 63 Then scx = 127-sc
			scy = 0
		
		SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
		SetOrigin x-gxoff,y-gyoff
		SetBlend ALPHABLEND
		Local scc# = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale 1+Float(move)/5.0,1+Float(move)/5.0
		else:
			SetAlpha 0.5-scc/8		
			SetScale 1.5+scx/16.0,1.5+scy/16.0 #scc,scc
		
		Local diam#[]=[0.0,12.0+scy/32, 12.0+scx/32,0.0, 0.0,-12.0-scy/32, -12.0-scx/32,0.0]
		DrawPoly diam
		
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetBlend lightblend
		SetScale 1+scx/80.0,1+scy/80.0
		DrawImage bluediamond,x-gxoff,y-gyoff		
		SetScale 1,1
		return
