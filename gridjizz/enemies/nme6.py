


#snake
class nme6
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field ishead:Int, die:Int
	Field tail:nme6, sz:Int
	Field head:nme6
	Field move:Int
	Field rot:Int,rotdir:Int
	Global segdir:Int = 20
	
	def Create:nme6( x#, y#, length:Int, freeze:Int, rr:Int=0, hdx#=0,hdy#=0, close:Int = 0 )
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		if CountList(nme6_list) > 16 * 24 Then return Null
		Local dir:Int,mag#
		Local n:nme6 = New nme6
		n.x = x
		n.y = y
		n.r = Rand(0,359)
		n.move = freeze
		n.sz = length
		n.die = False
		if length = 24
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme6_born_snd, 1, pan, vol)									
			n.ishead = True
			n.head = Null
			n.rot = n.r
			n.rotdir = Rand(0,1)
			mag# = Rnd(0.5,2)
			n.dx = Cos(n.rot)*mag
			n.dy = Sin(n.rot)*mag
			rr = n.rot+180
		else:
			n.ishead = False		
			n.dx = hdx
			n.dy = hdy
		
		if length > 0
			if length % 3 = 0 Then if Rand(0,1) = 1 Then segdir = -segdir 
			Local ndx:Int = 0#Cos(rr)*15
			Local ndy:Int = 0#Sin(rr)*15	
			n.tail = nme6.Create(x+ndx,y+ndy,length-1,freeze, rr+segdir, -ndx , -ndy, 0 )
			n.tail.head = n
		else:
			n.tail = Null
					
		nme6_list.AddLast( n )	
		return n
	
	
	def Update()
		Local speed#, distx#,disty#,dist#
		if move > 0
			move:-1
			if die 
				if tail <> Null
					tail.die = True
					tail.move = move	
				
				Explode()		
			
			return
		
		r = r + 1
		if head <> Null
			distx# = head.x-x
			disty# = head.y-y
			dist# = Sqr(distx * distx + disty * disty)
			if dist > 15
				dx = distx/dist*speed_nme6
				dy = disty/dist*speed_nme6
			else:
				if dist = 0 Then dist = 0.001
				dx = distx/dist/32
				dy = disty/dist/32
			
						
		if ishead
			dx = dx + Cos(rot)*speed_nme6
			dy = dy + Sin(rot)*speed_nme6
			if rotdir = 0 
				rot:+ 4
			else:
				rot:- 4
			
			if Rand(1,100) > 90 Then rotdir = 1 - rotdir		
				
		#Toward(px,py,400)
		if ishead Then BlackHole()
		speed# = Sqr(dx*dx+dy*dy)
		if speed >  speed_nme6
			dx = dx/speed*speed_nme6
			dy = dy/speed*speed_nme6
				
		x = x + dx
		y = y + dy
		if x < 8 
			dx = abs(dx)
			x = x + dx
			rot = rot + 90
		elif: x > PLAYFIELDW-8
			dx = -abs(dx)
			x = x + dx
			rot = rot + 90
		
		if y < 8
			dy = abs(dy)
			y = y + dy
			rot = rot + 90
		elif: y > PLAYFIELDH-8
			dy = -abs(dy)
			y = y + dy
			rot = rot + 90
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 24*24
			killer = True
			MarkKiller()
			if KillPlayer() Then nme6_LIST.Remove(Self)
					
	

	def Blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
			if n5.active			
				Local ddx# = n5.x-x
				Local ddy# = n5.y-y 
				Local dist# = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75+n5.sz*5
					dx = dx + ddx/dist/1024*(1200-dist)
					dy = dy + ddy/dist/1024*(1200-dist)
					if dist < 12+n5.sz/2
						Kill(False)
						n5.Grow(1)
						Exit
					
				
			
		
	
		
	def Kill(points:Int=True)
		Local t:Int
		if ishead
			if points
				score.IncScore(x,y,100)
				Local pan# = (x-px)/PLAYFIELDW
				Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
				PlaySound2(quarkhitsound, 1, pan, vol)				
					
			for t = 0 To 31
				part.Create(x,y,0 ,COL_SNAKE_R,COL_SNAKE_G,COL_SNAKE_B)	
			
			gridpoint.Shockwave(x,y)
			if tail <> Null
				tail.die = True
				if points
					tail.move = 30
				else:
					tail.move = 300				
				
			
			nme6_LIST.Remove(Self)
		else:
			if points
				Local pan# = (x-px)/PLAYFIELDW
				Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
				PlaySound2(nme6_tailhit_snd, 1, pan, vol)								
					
			for t = 0 To 7
				part.Create(x,y,0 ,COL_TAIL_R,COL_TAIL_G,COL_TAIL_B)	
			
		
	

	def MarkKiller()
		Local hd:nme6,tl:nme6
		# go up head and down tail marking killer
		hd = head
		while hd <> Null
			hd.killer = True
			hd = hd.head
		
		tl = tail
		while tl <> Null
			tl.killer = True
			tl = tl.tail
		
	
	

	def Explode()
		nme6_LIST.Remove(Self)
		if move < 50
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme6_tailexplode_snd, 1, pan, vol)										 
		
		for Local t:Int = 0 To 7
			part.Create(x,y,0 ,COL_TAIL_R,COL_TAIL_G,COL_TAIL_B)	
		
	

	def Draw()
		Local roti:Int
		roti = ATan2(dy,dx)+90
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		SetRotation(roti)
		if sz = 24
			DrawImage snakehead,x-gxoff,y-gyoff		
		else:
			DrawImage snaketail,x-gxoff,y-gyoff,sz
		
		SetRotation 0		
		return



