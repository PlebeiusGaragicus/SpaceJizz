
#blue butterflies
class nme8:
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field move:Int
	
	def Create:nme8( x# , y# , freeze:Int , close:Int = 0)
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme8_born_snd, 1, pan, vol)						
		Local n:nme8 = New nme8
		n.x = x
		n.y = y
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(3.0,6.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.move = freeze
		nme8_list.AddLast( n )	
		return n
	
	
	def Update()
		if move > 0
			move:-1
			return
		
		Local distx#
		Local disty#	
		Local dist#
		Local othern8:nme8
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
		for othern8:nme8 = EachIn nme8_list
			if othern8 <> Self
				distx# = othern8.x-x
				disty# = othern8.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 16*16 + 16*16
					dx = dx - Sgn(distx)/8
					dy = dy - Sgn(disty)/8
				
			
		
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed > speed_nme8
			dx = dx/speed*speed_nme8
			dy = dy/speed*speed_nme8
		
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 12*12 + 12*12
			killer = True		
			if KillPlayer() Then nme8_LIST.Remove(Self)
		
	

	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
			if n5.active			
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75+n5.sz*5
					dx = dx + ddx/dist/2048*(500-dist)
					dy = dy + ddy/dist/2048*(500-dist)
					if dist < 12+n5.sz
						Kill(False)
						n5.Grow(1)
						Exit
					
				
			
		
	
			
	def Toward(xx#,yy#,range1#)
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range1
			dx = dx + ddx/dist*2
			dy = dy + ddy/dist*2
		
	
	
	def Kill(points:Int=True)
		if points
			score.IncScore(x,y,10)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhitsound, 1, pan, vol)	
		
		for Local t:Int = 0 To 8
			part.Create(x,y, 8 ,COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B,t*120+r)	
		
		gridpoint.Shockwave(x,y)
		nme8_LIST.Remove(Self)				
	

	def Draw()
		Local sc#
		Local tri#[]=[0.0,-10.0, 8.0,6.0, -8.0,6.0]
		SetColor COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B
		SetBlend alphablend
		SetOrigin x-gxoff,y-gyoff
		SetRotation(r*8)
		sc = (r/16) % 8  + 0.5
		if move > 0
			SetAlpha Float(move)/40.0
			SetScale Float(move)/5.0,Float(move)/5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc,sc
		
		DrawPoly tri
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		SetRotation(r*8)
		DrawImage indigotriangle,x-gxoff,y-gyoff
		SetRotation 0		
		return
