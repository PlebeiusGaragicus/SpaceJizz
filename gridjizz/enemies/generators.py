# generators
class ge
	Field x#,y#,r#,kind:Int,rate:Int,sz#,killer:Int=False
	Field move:Int
	
	def Create:ge( x#, y#, kind:Int, rate:Int, size:Int ,freeze:Int)
		SafeXY(x,y,px,py,160)
		Local pan# = (x-px)/PLAYFIELDW
		Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
		PlaySound2(ge_born_snd, 1, pan, vol)			
		Local g:ge = New ge
		g.x = x
		g.y = y
		g.sz = size
		g.r = Rand(0,359)
		g.rate = rate
		g.kind = kind
		g.move = freeze
		GENERATOR_LIST.AddLast( g )	
		return g
	
	
	def Update()
		if move > 0
			move:-1
			return
		
		r = r + 1
		Local distx# = x-px
		Local disty# = y-py
		Local dist# = (distx * distx + disty * disty)
		if dist < (12+sz/2)*(12+sz/2)+12*12
			killer = True		
			KillPlayer() 
		
		
		if r % (rate+42-sz) = 0 Then birth()

	
	
	def Birth()
		gridpoint.Push(x , y , 6 , .9)
		Select kind
			Case 1 # pink spinners
				nme1.create(x+Rand(-10,10),y+Rand(-10,10),5,1)
			Case 2 # blue diamonds
				nme2.create(x+Rand(-10,10),y+Rand(-10,10),5,1)
			Case 3 # green squares
				nme.create(x+Rand(-10,10),y+Rand(-10,10),5,1)
			Case 4 # purple cubes
				nme3.create(x+Rand(-10,10),y+Rand(-10,10),0,5,1)
			Case 5 # blue circles
				nme4.create(x+Rand(-10,10),y+Rand(-10,10),5,0,1)
			Case 6 # red circles
				nme5.create(x+Rand(-10,10),y+Rand(-10,10),10,5,1)
			Case 7 # orange triangles
				le.create(x+Rand(-10,10),y+Rand(-10,10),5,1)				
			Case 8 # snakes
				nme6.create(x+Rand(-10,10),y+Rand(-10,10),24,5,1)
			Case 9 # red clone
				nme7.create(x+Rand(-10,10),y+Rand(-10,10),5,1)
			Case 10 # butterflies
				nme8.create(x+Rand(-10,10),y+Rand(-10,10),5,1)
		End Select
		

	def Kill(points:Int=True)
		sz = sz - 1
		if points = False Then sz = 0
		for Local t:Int = 0 To 3 + (sz<1)*8 # 1 or 8
			Select kind
				Case 1 # pink spinners
					part.Create(x,y, 0 ,COL_PIN_R,COL_PIN_G,COL_PIN_B)	
				Case 2 # blue diamonds
					part.Create(x,y, 0 ,COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B)	
				Case 3 # green squares
					part.Create(x,y, 0 ,COL_SQUARE_R,COL_SQUARE_G,COL_SQUARE_B)	
				Case 4 # purple cubes
					part.Create(x,y, 0 ,COL_CUBE_R,COL_CUBE_G,COL_CUBE_B)	
				Case 5 # blue circles
					part.Create(x,y, 0 ,COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B)	
				Case 6 # red circles
					part.Create(x,y, 0 ,COL_SUN_R,COL_SUN_G,COL_SUN_B)	
				Case 7 # orange triangles
					part.Create(x,y, 0 ,COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B)	
				Case 8 # snake
					part.Create(x,y, 0 ,COL_SNAKE_R,COL_SNAKE_G,COL_SNAKE_B)	
				Case 9 # clone
					part.Create(x,y, 0 ,COL_CLONE_R,COL_CLONE_G,COL_CLONE_B)	
				Case 10 # butterfly
					part.Create(x,y, 0 ,COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B)	
			End Select
		

		if sz < 1
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(ge_killed_snd, 1, pan, vol)			
			if points Then score.IncScore(x,y,200)
			GENERATOR_LIST.Remove(Self)
		else:
			Local freq# = 1+(sz)/64
			Local pan# = (x-px)/PLAYFIELDW
			Local vol# = (1 - abs(pan)/10) * (1 - (abs(y-py)/PLAYFIELDH)/10)
			PlaySound2(ge_hit_snd, freq, pan, vol)			
			if points Then score.IncScore(x,y,1,False)			
		
	
	
	def Draw()
		Local sc#,scy#,scx#,zz#,zs#,t:Int
		Local x1#,x2#,x3#,x4#,y1#,y2#,y3#,y4#
		Local sqa#[]=[12.0,12.0, 12.0,-12.0, -12.0,-12.0, -12.0,12.0]
		Local diam#[]=[0.0,12.0, 12.0,0.0, 0.0,-12.0, -12.0,0.0]
		Local tri#[]=[0.0,8.0, 6.0,-4.0, -6.0,-4.0]
		Local staywhite:Int = False
		
		SetColor 255,255,255		
		if (r+8) % (rate+42-sz) < 8 Then staywhite = True
		
		Select kind
			Case 2 # blue diamonds
				if Not staywhite SetColor COL_DIAMOND_R,COL_DIAMOND_G,COL_DIAMOND_B
				SetScale sz/14,sz/14
				SetAlpha 0.1+sz/256		
				SetOrigin x-gxoff,y-gyoff
				DrawPoly diam
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0				
				DrawLine x-gxoff,y-gyoff-12-sz/4,x-gxoff+12+sz/4,y-gyoff,0
				DrawLine x-gxoff+12+sz/4,y-gyoff,x-gxoff,y-gyoff+12+sz/4,0
				DrawLine x-gxoff,y-gyoff+12+sz/4,x-gxoff-12-sz/4,y-gyoff,0
				DrawLine x-gxoff-12-sz/4,y-gyoff,x-gxoff,y-gyoff-12-sz/4,0
				DrawLine x-gxoff,y-gyoff-8,x-gxoff+8,y-gyoff,0
				DrawLine x-gxoff+8,y-gyoff,x-gxoff,y-gyoff+8,0
				DrawLine x-gxoff,y-gyoff+8,x-gxoff-8,y-gyoff,0
				DrawLine x-gxoff-8,y-gyoff,x-gxoff,y-gyoff-8,0				

			Case 3 # green squares
				if Not staywhite SetColor COL_SQUARE_R,COL_SQUARE_G,COL_SQUARE_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/16,sz/16
				SetAlpha 0.1+sz/256
				DrawPoly sqa
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zz = 8+sz/4
				x1 = x-zz-gxoff
				y1 = y-zz-gyoff
				x2 = x+zz-gxoff
				y2 = y-zz-gyoff
				x3 = x+zz-gxoff
				y3 = y+zz-gyoff
				x4 = x-zz-gxoff
				y4 = y+zz-gyoff				
				DrawLine x1,y1,x2,y2,0
				DrawLine x2,y2,x3,y3,0
				DrawLine x3,y3,x4,y4,0
				DrawLine x4,y4,x1,y1,0
				DrawLine x-gxoff-8,y-gyoff-8,x-gxoff+8,y-gyoff-8,0
				DrawLine x-gxoff+8,y-gyoff-8,x-gxoff+8,y-gyoff+8,0
				DrawLine x-gxoff+8,y-gyoff+8,x-gxoff-8,y-gyoff+8,0
				DrawLine x-gxoff-8,y-gyoff+8,x-gxoff-8,y-gyoff-8,0	
			
			Case 4 # purple cubes
				if Not staywhite SetColor COL_CUBE_R,COL_CUBE_G,COL_CUBE_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/16,sz/16
				SetAlpha 0.1+sz/256
				DrawPoly sqa
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zz = 8+sz/4
				x1 = x-zz-gxoff
				y1 = y-zz-gyoff
				x2 = x+zz-gxoff
				y2 = y-zz-gyoff
				x3 = x+zz-gxoff
				y3 = y+zz-gyoff
				x4 = x-zz-gxoff
				y4 = y+zz-gyoff		
				DrawLine x1,y1,x2,y2,0
				DrawLine x2,y2,x3,y3,0
				DrawLine x3,y3,x4,y4,0
				DrawLine x4,y4,x1,y1,0
				DrawLine x-gxoff-8,y-gyoff-8,x-gxoff+8,y-gyoff-8,0
				DrawLine x-gxoff+8,y-gyoff-8,x-gxoff+8,y-gyoff+8,0
				DrawLine x-gxoff+8,y-gyoff+8,x-gxoff-8,y-gyoff+8,0
				DrawLine x-gxoff-8,y-gyoff+8,x-gxoff-8,y-gyoff-8,0	
				
			Case 5 # blue circles
				if Not staywhite SetColor COL_SEEKER_R,COL_SEEKER_G,COL_SEEKER_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/8,sz/8
				SetAlpha 0.1+sz/256
				DrawPoly circ
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zs# = (1+sz/16)/1.1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0
				zs# = 1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0
					
			Case 6 # red circles
				if Not staywhite SetColor COL_SUN_R,COL_SUN_G,COL_SUN_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/8,sz/8
				SetAlpha 0.1+sz/256
				DrawPoly circ
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zs# = (1+sz/16)/1.1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0
				zs# = 1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0
					
			Case 7 # orange triangles
				if Not staywhite SetColor COL_TRIANGLE_R,COL_TRIANGLE_G,COL_TRIANGLE_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/8,sz/8
				SetAlpha 0.1-sc/256		
				DrawPoly tri
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				DrawLine x-gxoff,y-gyoff+12+sz/4,x-gxoff+9+sz/4,y-gyoff-4-sz/4,0
				DrawLine x-gxoff+9+sz/4,y-gyoff-4-sz/4,x-gxoff-9-sz/4,y-gyoff-4-sz/4,0
				DrawLine x-gxoff-9-sz/4,y-gyoff-4-sz/4,x-gxoff,y-gyoff+12+sz/4,0
				DrawLine x-gxoff,y-gyoff+12,x-gxoff+9,y-gyoff-4,0
				DrawLine x-gxoff+9,y-gyoff-4,x-gxoff-9,y-gyoff-4,0
				DrawLine x-gxoff-9,y-gyoff-4,x-gxoff,y-gyoff+12,0					
				
			Case 1 # pink spinners
				if Not staywhite SetColor COL_PIN_R,COL_PIN_G,COL_PIN_B
				SetScale sz/14,sz/14
				SetAlpha 0.1+sz/256		
				SetOrigin x-gxoff,y-gyoff
				DrawPoly diam
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				DrawLine x-gxoff,y-gyoff-12-sz/4,x-gxoff+12+sz/4,y-gyoff,0
				DrawLine x-gxoff+12+sz/4,y-gyoff,x-gxoff,y-gyoff+12+sz/4,0
				DrawLine x-gxoff,y-gyoff+12+sz/4,x-gxoff-12-sz/4,y-gyoff,0
				DrawLine x-gxoff-12-sz/4,y-gyoff,x-gxoff,y-gyoff-12-sz/4,0
				DrawLine x-gxoff,y-gyoff-8,x-gxoff+8,y-gyoff,0
				DrawLine x-gxoff+8,y-gyoff,x-gxoff,y-gyoff+8,0
				DrawLine x-gxoff,y-gyoff+8,x-gxoff-8,y-gyoff,0
				DrawLine x-gxoff-8,y-gyoff,x-gxoff,y-gyoff-8,0				

			Case 8 # purple snake
				if Not staywhite SetColor COL_SNAKE_R,COL_SNAKE_G,COL_SNAKE_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/8,sz/8
				SetAlpha 0.1+sz/256
				DrawPoly circ
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zs# = (1+sz/16)/1.1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0
				zs# = 1
				for t = 0 To 16
					DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
						x-gxoff+circ[t*2+2]*zs,y-gyoff+circ[t*2+1+2]*zs,0
				
				DrawLine x-gxoff+circ[t*2]*zs,y-gyoff+circ[t*2+1]*zs,..
					x-gxoff+circ[0]*zs,y-gyoff+circ[1]*zs,0

			Case 9 # red clone
				if Not staywhite SetColor COL_CLONE_R,COL_CLONE_G,COL_CLONE_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/16,sz/16
				SetAlpha 0.1+sz/256
				DrawPoly sqa
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				zz = 8+sz/4
				x1 = x-zz-gxoff
				y1 = y-zz-gyoff
				x2 = x+zz-gxoff
				y2 = y-zz-gyoff
				x3 = x+zz-gxoff
				y3 = y+zz-gyoff
				x4 = x-zz-gxoff
				y4 = y+zz-gyoff		
				DrawLine x1,y1,x2,y2,0
				DrawLine x2,y2,x3,y3,0
				DrawLine x3,y3,x4,y4,0
				DrawLine x4,y4,x1,y1,0
				DrawLine x-gxoff-8,y-gyoff-8,x-gxoff+8,y-gyoff-8,0
				DrawLine x-gxoff+8,y-gyoff-8,x-gxoff+8,y-gyoff+8,0
				DrawLine x-gxoff+8,y-gyoff+8,x-gxoff-8,y-gyoff+8,0
				DrawLine x-gxoff-8,y-gyoff+8,x-gxoff-8,y-gyoff-8,0	

			Case 10 # blue butterflies
				if Not staywhite SetColor COL_BUTTER_R,COL_BUTTER_G,COL_BUTTER_B
				SetOrigin x-gxoff,y-gyoff
				SetScale sz/8,sz/8
				SetAlpha 0.1-sc/256		
				DrawPoly tri
				SetAlpha 1
				SetScale 1,1
				SetOrigin 0,0
				DrawLine x-gxoff,y-gyoff+12+sz/4,x-gxoff+9+sz/4,y-gyoff-4-sz/4,0
				DrawLine x-gxoff+9+sz/4,y-gyoff-4-sz/4,x-gxoff-9-sz/4,y-gyoff-4-sz/4,0
				DrawLine x-gxoff-9-sz/4,y-gyoff-4-sz/4,x-gxoff,y-gyoff+12+sz/4,0
				DrawLine x-gxoff,y-gyoff+12,x-gxoff+9,y-gyoff-4,0
				DrawLine x-gxoff+9,y-gyoff-4,x-gxoff-9,y-gyoff-4,0
				DrawLine x-gxoff-9,y-gyoff-4,x-gxoff,y-gyoff+12,0					
