
#line end
class le:
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field attached:Int, le2:le, strength#
	Field checked:Int
	Field move:Int, resist:Int = False

	def Create:le( x#, y#,freeze:Int, close:Int = 0 )
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(le_born_snd, 1, pan, vol)	
		Local n:le = New le
		n.x = x
		n.y = y
		n.r = Rand(0,359)
		Local dir:Int = Rand(0,359)
		Local mag# = Rnd(.25,1.0)		
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.attached = False
		n.le2 = Null
		n.move = freeze
		le_list.AddLast( n )	
		return n
	
	
	def Update()
		Local distx#
		Local disty#
		Local dist#
		if move > 0
			move:-1
			return
		
		checked = False
		r = r + 2
		Local ll:le 
		for ll:le = EachIn le_list
			if ll <> Self
				if attached = False
					distx# = x-ll.x
					disty# = y-ll.y
					dist# = (distx * distx + disty * disty)
					if dist < 32*32
						if ll.attached = False
							attached = True
							strength = 25
							le2 = ll
							ll.attached = True
							ll.le2 = Self
							ll.strength = 25
						
					
				
			
		
		if attached = True
			TowardPartner(le2.x,le2.y)
			if resist = False Then BlackHole2()
		else:
			toward(px,py,300)
			BlackHole()
		
		
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed > speed_le
			dx = dx/speed*speed_le
			dy = dy/speed*speed_le
		
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
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 24*24
			killer = True		
			if KillPlayer()
				if le2 <> Null
					le2.attached = False
					le2.resist = False
					le2.le2 = Null
				
				le2 = Null
				attached = False
				resist = False
				le_LIST.Remove(Self)
			else:
				killer = False
			
				
	
	
	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
			if n5.active			
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 25+n5.sz*5
					dx = dx + ddx/dist/1024*(500-dist)
					dy = dy + ddy/dist/1024*(500-dist)
					if dist < n5.sz/2
						Kill(False,0,0)
						n5.Grow(1)
						Exit
					
				
			
		
	
		
	def Blackhole2()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
			# it gets pulled in, partner spins around
			if le2 <> Null Then le2.resist = True else: Exit
			Toward(n5.x,n5.y,100+n5.sz*10)
			Local distx# = x-n5.x
			Local disty# = y-n5.y
			Local dist# = (distx * distx + disty * disty)
			if dist < (12)*(12) + n5.sz*n5.sz*4
				if le2.Spin(Cos(n5.r*2)*16,Sin(n5.r*2)*16)
					# free it
					le2.attached = False
					le2.resist = False
					le2.le2 = Null
					le2.strength = 0
					le2 = Null
					attached = False
					resist = False
					strength = 0
					le_LIST.Remove(Self)
					n5.Grow(1)
					Exit
				#else:
				#	strength = le2.strength				
				
			
		
		
	
	def TowardPartner(xx#,yy#)
		Local speed#
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist > 150
			dx = dx + ddx/dist*32
			dy = dy + ddy/dist*32
		elif: dist < 64
			dx = dx -ddx/dist*32
			dy = dy -ddy/dist*32
		
		
	
	def Toward(xx#,yy#,range:Int)	
		Local ddx# = xx-x
		Local ddy# = yy-y 
		Local dist# = Sqr(ddx*ddx + ddy*ddy)+0.001
		if dist < range 
			dx = dx + ddx/dist
			dy = dy + ddy/dist
		
	

	def Spin:Int(vx#,vy#)
		Local t:Int
		dx = dx - vx/2
		dy = dy - vy/2
		strength:-0.25
		if strength <= 0
			return True
		else:
			return False
		
	
			
	def Kill(points:Int=True,vx#,vy#)
		Local t:Int
		for t = 0 To 3
			part.Create(x,y, 8 ,20+strength*4,220-strength*4,0,r)	
		
		if points = False Then attached = False
		if attached 
			dx = dx - vx/16
			dy = dy - vy/16
			strength:-2.5
			if strength <= 0
				strength = 0
				if le2 <> Null
					le2.attached = False
					le2.le2 = Null
					le2.strength = 0
				
				le2 = Null
				attached = False
			
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(le_hit_snd, 1, pan, vol)				
		else:
			if points = True score.IncScore(x,y,150)		
			gridpoint.ShockWave(x,y)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(le_killed_snd, 1, pan, vol)	
			for t = 0 To 31
				part.Create(x,y, 8 ,COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B)
			
			le_LIST.Remove(Self)
		
	

	def Draw()
		Local sc#
		Local tri#[]=[0.0,-10.0, 8.0,6.0, -8.0,6.0]
		SetColor COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B
		SetBlend alphablend
		SetOrigin x-gxoff,y-gyoff
		SetRotation(r*2)
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
		SetRotation(r*2)
		DrawImage orangetriangle,x-gxoff,y-gyoff
		if attached 
			SetRotation(r*4+180)		
			DrawImage orangetriangle,x-gxoff,y-gyoff
		
		SetRotation 0		
		return
	
	
	def DrawBond(self):
		if attached and not killer:
			SetColor 20+strength*8,220-strength*8,0
			DrawLine (x-gxoff,y-gyoff,le2.x-gxoff,le2.y-gyoff,0)
