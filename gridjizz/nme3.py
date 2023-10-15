
# purple squares
Type nme3
	Field x#,y#,dx#,dy#,r#,sz:Int, killer:Int=False
	Field move:Int

	def Create:nme3( x#, y#, size:Int, freeze:Int, close:Int=0 )
		if CountList(nme3_list) > 100 Then return Null
		if size <> 0 Or close <> 0
			SafeXY(x,y,px,py,40,1)		
		else:
			SafeXY(x , y , px , py , 160)
		
		if size = 0 
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme3_born_snd,1, pan, vol)						
		
		Local dir:Int, mag#
		Local n:nme3 = New nme3
		n.x = x
		n.y = y
		n.sz = size
		n.r = Rand(0,359)
		dir = Rand(0,359)
		mag# = Rnd(.25,2.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		nme3_list.AddLast( n )	
		return n
	
	
	def Update()
		if move > 0
			move:-1
			return
		
		Local distx#
		Local disty#	
		Local dist#
		Local othern3:nme3
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
		for othern3:nme3 = EachIn nme3_list
			if othern3 <> Self
				distx# = othern3.x-x
				disty# = othern3.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 30*30 + 20*20 - sz*20
					dx = dx - Sgn(distx)
					dy = dy - Sgn(disty)
				
			
				
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed > (speed_nme3 - sz/4)
			dx = dx/speed*(speed_nme3 - sz/4)
			dy = dy/speed*(speed_nme3 - sz/4)
		
		x = x + Sin(r*(6+sz))*(sz)
		y = y + Cos(r*(6+sz))*(sz)
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < (12-sz)*(12-sz) + 12*12
			killer = True
			if KillPlayer() Then nme3_LIST.Remove(Self)
					
	
	
	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
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
					
				
			
		
	
															
	def Toward(xx#,yy#,range1#)
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range1
			dx = dx + ddx/dist*2.5
			dy = dy + ddy/dist*2.5
		
	
	
	def Kill(points:Int=True)
		Local t:Int, freq# = 1
		if points
			if sz = 0
				score.IncScore(x,y,100)
				freq = 1
			else:
				score.IncScore(x,y,50)
				freq = 1.25
			
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhitsound,freq, pan, vol)									
			if sz = 0
				for t = 0 To 2
					nme3.Create(x+Rand(-30,-30),y+Rand(-30,30),4,2,1)
				
					
		
		for t = 0 To 15
			part.Create(x,y,3 ,COL_CUBE_R,COL_CUBE_G,COL_CUBE_B,r)	
		
		gridpoint.Shockwave(x,y)
		nme3_LIST.Remove(Self)				
	

	def Draw()
		SetColor COL_CUBE_R,COL_CUBE_G,COL_CUBE_B
		SetRotation(r+45)
		SetOrigin x-gxoff,y-gyoff
		SetBlend ALPHABLEND		
		Local sc# = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale Float(move)/5.0,Float(move)/5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc,sc
		
		Local sqa#[]=[0.0,12.0-sz, 12.0-sz,0.0, 0.0,-12.0+sz, -12.0+sz,0.0]
		DrawPoly sqa
		
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		SetRotation(r)
		if sz = 0
			DrawImage purplesquare1,x-gxoff,y-gyoff
		else:
			DrawImage purplesquare2,x-gxoff,y-gyoff		
		
		SetRotation 0		
		return
