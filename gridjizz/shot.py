

# player bullets
class shot:

	Field x#,y#,dx#,dy#,sp#
	
	def Create( x#, y# ,xd#, yd#, sp#)
		if CountList(SHOT_list) < 500
			Local s:SHOT= New SHOT
			s.x = x
			s.y = y
			s.sp = sp
			s.dx = xd
			s.dy = yd
			#s.x1 = s.x2 + s.dx
			#s.y1 = s.y2 + s.dy
			SHOT_list.AddLast( s )
		
	
	
	def Update()
		Local kill:Int = False
		Local pass:Int
		
		for pass = 0 To 1
		x = x + dx/2
		y = y + dy/2
		if x < 0 Or x > PLAYFIELDW-1
			x = x - dx*2/2
			if bouncyshots = 0
				kill = True
			else:
				dx = -dx
			
		
		if y < 0 Or y > PLAYFIELDH-1
			y = y - dy*2/2		
			if bouncyshots = 0
				kill = True
			else:
				dy = -dy
			
		
		if Not kill
			if supershots > 0
				CheckCollisions()
			else:
				kill = CheckCollisions()				
			
		
		if Not kill Then blackhole()
		Local speed# = Sqr(dx*dx+dy*dy)
		if speed < sp/2 and speed > 0
			dx = dx/speed*sp/2
			dx = dx/speed*sp/2
				
		if kill
			if supershots > 0
				for Local t:Int = 0 To 3
					part.Create(x,y,0 ,COL_SHOT1_R,COL_SHOT1_G,COL_SHOT1_B)	
				
			else:
				if bouncyshots
					for Local t:Int = 0 To 3
						part.Create(x,y,0 ,COL_SHOT2_R,COL_SHOT2_G,COL_SHOT2_B)	
									
				else:
					for Local t:Int = 0 To 3
						part.Create(x,y,0 ,COL_SHOT_R,COL_SHOT_G,COL_SHOT_B)	
					
				
			
			SHOT_LIST.Remove(Self)
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(shot_hit_wall_snd, 1, pan, vol)	
			Exit # no need for 2nd pass
		else:
			gridpoint.Push(x+dx*2,y+dy*2,3,.025)
		
		
	
	
	def blackhole()
		Local n5:nme5
		for n5:nme5 = EachIn nme5_list
			if n5.active
				Toward(n5.x,n5.y,75+n5.sz*5,n5.sz/4)	
			
		
			

	def Toward(xx#,yy#,range:Int,di:Int)
		#diam = 1 to 16
		Local ddx# = xx-x
		Local ddy# = yy-y 
		if ddx*ddx + ddy*ddy < range * range and ddx*ddx + ddy*ddy > 32*32
			ddx# = -Sgn(ddx)/(26-di)
			ddy# = -Sgn(ddy)/(26-di)
			dx = dx + ddx
			dy = dy + ddy
		
	
	
	
	def Checkcollisions:Int()
		Local n:nme
		Local n1:nme1
		Local n2:nme2
		Local n3:nme3
		Local n4:nme4
		Local n5:nme5
		Local n6:nme6
		Local n7:nme7
		Local n8:nme8
		Local g:ge
		Local ll:le	
		Local distx#
		Local disty#
		Local dist#															
		for n5:nme5 = EachIn nme5_list
			distx# = x-n5.x
			disty# = y-n5.y
			dist# = (distx * distx + disty * disty)
			if dist < (12+n5.sz/2)*(12+n5.sz/2)
				n5.Kill()
				return True
			
		
		for n:nme = EachIn nme_list
			distx# = x-n.x
			disty# = y-n.y
			dist# = (distx * distx + disty * disty)
			if dist < 16*16+2*2
				n.Kill()
				return True
			else:
				n.RunAway(x,y,x+dx,y+dy)
			
		
		for n1:nme1 = EachIn nme1_list
			distx# = x-n1.x
			disty# = y-n1.y
			dist# = (distx * distx + disty * disty)
			if dist < 16*16+2*2
				n1.Kill()
				return True
						
		
		for n2:nme2 = EachIn nme2_list
			distx# = x-n2.x
			disty# = y-n2.y
			dist# = (distx * distx + disty * disty)
			if dist < 18*18+3*3
				n2.Kill()
				return True
			
		
		for n3:nme3 = EachIn nme3_list
			distx# = x-n3.x
			disty# = y-n3.y
			dist# = (distx * distx + disty * disty)
			if dist < 16*16+3*3 - n3.sz*3
				n3.Kill()
				return True
						
		
		for n4:nme4 = EachIn nme4_list
			distx# = x-n4.x
			disty# = y-n4.y
			dist# = (distx * distx + disty * disty)
			if dist < 12*12+2*2
				n4.Kill()
				return True
			
		
		for ll:le = EachIn le_list
			distx# = x-ll.x
			disty# = y-ll.y
			dist# = (distx * distx + disty * disty)
			if dist < 12*12+2*2
				ll.Kill(True,-dx*5,-dy*5) #x1-x2,y1-y2)
				return True
						
		
		for g:ge = EachIn ge_list
			distx# = x-g.x
			disty# = y-g.y
			dist# = (distx * distx + disty * disty)
			if dist < 12*12 + g.sz
				g.Kill()
				return True
			
		
		for n6:nme6 = EachIn nme6_list
			distx# = x-n6.x
			disty# = y-n6.y
			dist# = (distx * distx + disty * disty)
			if dist < 9*9 + n6.sz
				n6.Kill()
				return True
					
		
		for n7:nme7 = EachIn nme7_list
			distx# = x-n7.x
			disty# = y-n7.y
			dist# = (distx * distx + disty * disty)
			if dist < 64*64
				if abs(n7.rotdir) > 4
					#no shield up
					if dist < 12*12
						n7.Kill()
						return True
					
				else:
					# is it in the shield ? 
					if PointInTri(x,y, n7.x-dx, n7.y-dy, n7.xrgt,n7.yrgt,n7.xlft,n7.ylft)
						# just kill bullet
						return True
					else:
						# not in the shield - must be sides or back
						if dist < 12*12
							n7.Kill()
							return True
						
					
				
			
		
		for n8:nme8 = EachIn nme8_list
			distx# = x-n8.x
			disty# = y-n8.y
			dist# = (distx * distx + disty * disty)
			if dist < 10*10+2*2
				n8.Kill()
				return True
			
		
				
		return False		
				
	
	
	def DrawAllShots()
		Local s:shot	
		if supershots
			SetColor COL_SHOT1_R,COL_SHOT1_G,COL_SHOT1_B
		else:
			if bouncyshots
				SetColor COL_SHOT2_R,COL_SHOT2_G,COL_SHOT2_B			
			else:
				SetColor COL_SHOT_R,COL_SHOT_G,COL_SHOT_B
			
		
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		for s:shot = EachIn SHOT_list
			Local roti:Int = ATan2( s.dy,s.dx)+90
			SetRotation(roti)
			DrawImage yellowshot,s.x-gxoff,s.y-gyoff
		
		SetRotation 0			

	
	def Superbomb()
		Local t:Float
		Local z:Int = 1
		if numbombs > 0
			PlaySound2(super_bomb_snd)
			bombtime = 60
			numbombs:-1	
			for t = 0 To (z*360)-1
				part.Create(px,py,1,COL_BOMB_R,COL_BOMB_G,COL_BOMB_B, t/z)
				part.Create(px,py,9,COL_BOMB_R,COL_BOMB_G,COL_BOMB_B)
			
			DestroyAll()
			score.ResetMultiplier()
			gridpoint.Pull(px,py,60,60)
			player_shield = 65		
