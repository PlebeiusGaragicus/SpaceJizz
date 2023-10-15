

#red clone
class nme7
	Field x#,y#,dx#,dy#,r#,killer:Int=False
	Field move:Int
	Field rot:Int,rotdir:Int,lastplayed:Int
	Field xrgt#,yrgt#,xlft#,ylft#
	
	def Create( x#, y#, freeze:Int, close:Int = 0 )
		if close = 0
			SafeXY(x,y,px,py,160)
		else:
			SafeXY(x,y,px,py,40,1)		
				
		if CountList(NME7_LIST) > 3 and Rand(0,100) > 50 Then return
		if CountList(NME7_LIST) > 7 Then return
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(nme7_born_snd, 1, pan, vol)	
		Local dir:Int,mag#
		Local n:nme7 = New nme7
		n.move = freeze
		n.x = x
		n.y = y
		dir = Rand(0,359)
		mag# = Rnd(0.5,2)
		n.dx = Cos(dir)*mag
		n.dy = Sin(dir)*mag
		n.r = Rand(0,359)

		n.rot = n.r
		n.rotdir = TurnToFace(n.x,n.y,n.dx,n.dy,PLAYFIELDW/2,PLAYFIELDH/2) # turn towards center
		if abs(n.rotdir) < 16
			n.rotdir = 16
		
		NME7_LIST.AddLast( n )	
		return
	
	
	def Update()
		Local speed#, distx#,disty#,dist#,dx2#,dy2#
		if move > 0
			move:-1
			return
		
		r = (r + 16) % 360
		if Rand(1,100) > 95-speed_nme7*8
			rotdir = TurnToFace(x,y,dx,dy,px,py)
				
		if rotdir <> 0 
			rot:+ 4*Sgn(rotdir)
			rotdir = rotdir - Sgn(rotdir)
		
		if rotdir = 0 and lastplayed = 0
			lastplayed = 60
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(nme7_shield_snd, 1, pan, vol)				
		
		if lastplayed > 0 Then lastplayed:-1
		if abs(rotdir) < 20
			dx = dx + Cos(rot)*2	
			dy = dy + Sin(rot)*2
			gridpoint.Push(x+dx*8,y+dy*8,4,.1)
		else:
			dx = (dx + Cos(rot))*(0.265+speed_nme7/20)
			dy = (dy + Sin(rot))*(0.265+speed_nme7/20)
		
		x = x + dx
		y = y + dy
		if x < 16 
			x = x - dx
			y = y - dy
			#rotdir = rotdir + 180
		elif: x > PLAYFIELDW-16
			x = x - dx
			y = y - dy
			#rotdir = rotdir + 180
		
		if y < 16
			x = x - dx
			y = y - dy
			#rotdir = rotdir + 180
		elif: y > PLAYFIELDH-16
			x = x - dx
			y = y - dy
			#rotdir = rotdir + 180
		
		#Toward(px,py,400)
		BlackHole()
		for Local othern7:nme7 = EachIn NME7_LIST
			if othern7 <> Self
				distx# = othern7.x-x
				disty# = othern7.y-y
				dist# = (distx * distx + disty * disty)
				if dist < 20*20 + 20*20
					dx = dx - Sgn(distx)
					dy = dy - Sgn(disty)
				
			
		
		speed# = Sqr(dx*dx+dy*dy)
		if speed > speed_nme7
			dx = dx/speed*speed_nme7
			dy = dy/speed*speed_nme7
		
		distx# = x-px
		disty# = y-py
		dist# = (distx * distx + disty * disty)
		if dist < 24*24
			killer = True
			if KillPlayer() Then NME7_LIST.Remove(Self)
					
	

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
					if dist < 16+n5.sz/2
						Kill(False)
						n5.Grow(1)
						Exit
					
				
			
		
	
	
#	def Toward(xx#,yy#,range:Int)
#		Local ddx# = xx-x
#		Local ddy# = yy-y 
#		Local dist# = Sqr(ddx*ddx + ddy*ddy)
#		if dist < range and dist > 2
#			dx = dx + ddx/dist*32
#			dy = dy + ddy/dist*32
#		
#	
		
	def Kill(points:Int=True)
		Local t:Int
		if points
			score.IncScore(x,y,100)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(quarkhit2sound, 1, pan, vol)				
				
		for t = 0 To 15
			part.Create(x,y,6 ,COL_CLONE_R,COL_CLONE_G,COL_CLONE_B)	
		
		gridpoint.Shockwave(x,y)
		NME7_LIST.Remove(Self)
	

	def Draw()
		SetColor 255,255,255
		SetBlend lightblend
		SetRotation(rot+90)
		DrawImage redclone,x-gxoff,y-gyoff
		SetColor COL_CLONE_R,COL_CLONE_G,COL_CLONE_B		
		SetRotation 0
		Local xr#[8],yr#[8]
		xr[0] = x-6
		yr[0] = y
		xr[1] = x+6
		yr[1] = y
		xr[2] = x+6
		yr[2] = y+12
		xr[3] = x+12
		yr[3] = y+12
		xr[6] = x-12
		yr[6] = y+12
		TFormR(x,y, rot+270, xr[0] ,yr[0] )		
		TFormR(x,y, rot+270, xr[1] ,yr[1] )		
		TFormR(x,y, rot+270, xr[2] ,yr[2] )		
		TFormR(x,y, rot+270, xr[3] ,yr[3] )		
		TFormR(x,y, rot+270, xr[6] ,yr[6] )		
		Local pry# = yr[2]-yr[1]
		Local prx# = xr[2]-xr[1]
		if abs(rotdir) <= 4 
			for Local t# = 1.5+r/360 To 3.5+r/360
				DrawLine xr[3]+prx*t+(xr[0]-x)*t*1.5-gxoff,..
				yr[3]+pry*t+(yr[0]-y)*t*1.5-gyoff,..
				xr[6]+prx*t+(xr[1]-x)*t*1.5-gxoff,..
				yr[6]+pry*t+(yr[1]-y)*t*1.5-gyoff,0
			
		
		Local xn#,yn#
		Local sz# = Sqr(dx*dx + dy*dy)
		if sz = 0
			xn# = 1
			yn# = 1
		else:
			xn# = -dy/sz
			yn# = dx/sz
		
		xrgt# = x+yn*64+xn*36
		yrgt# = y-xn*64+yn*36
		xlft# = x+yn*64-xn*36
		ylft# = y-xn*64-yn*36	
		return


