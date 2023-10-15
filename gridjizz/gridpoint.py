# TAKEN FROM gridparttrail

from random import randint, uniform
from math import sin, cos, pi, sqrt

from gridparttrail import *





 # the background dots
class gridpoint:

	Field ox#,oy#
	Field x#
	Field y#
	Field dx#,dy#
 # 	Field fx#,fy#

	def Update(self, xx: float, yy: float):

		if abs(xx-x) > 2:
			dx:+ Sgn(xx-x)
		if abs(yy-y) > 2:
			dy:+ Sgn(yy-y)

		if abs(ox-x) > 1:
			x = x + Sgn(ox-x)
			dx:+ Sgn(ox-x)/2
		else:
			x = ox

		if abs(oy-y) > 1:
			y = y + Sgn(oy-y)
			dy:+ Sgn(oy-y)/2
		else:
			y = oy


		dx = dx *.899  # .89
		dy = dy *.899  # .89

		x = x + dx
		y = y + dy



	def ResetAll(self):
		for a in range(NUMGPOINTSW):
			for b in range(NUMGPOINTSH):
				grid[a,b].ox = a*GRIDWIDTH
				grid[a,b].oy = b*GRIDHEIGHT
				grid[a,b].x = a*GRIDWIDTH
				grid[a,b].y = b*GRIDHEIGHT
				grid[a,b].dx = 0
				grid[a,b].dy = 0


	def disrupt(self, xx: float, yy: float):
			if abs(xx) > 8:
				xx = xx/16
			if abs(yy) > 8:
				yy = yy/16

			dx = dx + xx
			dy = dy + yy

			speed = dx*dx+dy*dy
			if speed > 160  #  128
				dx = dx/speed*128
				dy = dy/speed*128


	def Pull(self, x1: float, y1: float, sz: int = 4, amnt = 4):

		Local a: int = x1/GRIDWIDTH
		Local b: int = y1/GRIDHEIGHT

		for Local xx: int = -sz To sz
			for Local yy: int = -sz To sz
				if a+xx > 0:
					if a+xx <= NUMGPOINTSW: # -2
						if b+yy > 0:
							if b+yy <= NUMGPOINTSH: # -2
								if xx*xx + yy*yy < sz*sz:
									Local diffx# = grid[a+xx,b+yy].x-x1
									Local diffy# = grid[a+xx,b+yy].y-y1
									Local dist# = Sqr(diffx*diffx+diffy*diffy)

									if dist > 0:
	# 									grid[a+xx,b+yy].fx:- diffx*(1-(dist)/(sz*sz*4*256))
	# 									grid[a+xx,b+yy].fy:- diffy*(1-(dist)/(sz*sz*4*256))
										grid[a+xx,b+yy].dx:- diffx/dist*amnt   # *(1-(dist*dist)/(sz*sz*4*256))
										grid[a+xx,b+yy].dy:- diffy/dist*amnt   # *(1-(dist*dist)/(sz*sz*4*256))
	# 									grid[a+xx,b+yy].fx = - diffx/dist*(1-(dist*dist)/(sz*sz*4*256))
	# 									grid[a+xx,b+yy].fy = - diffy/dist*(1-(dist*dist)/(sz*sz*4*256))




	def Push(self, x1: float, y1: self, sz: int = 4, amnt=1):

		Local a: int = (x1/GRIDWIDTH)
		Local b: int = (y1/GRIDHEIGHT)

		for Local xx: int = -sz To sz:
			for Local yy: int = -sz To sz:
			 # 	if (xx*xx + yy*yy) < sz*sz
				if a+xx > 0:
					if a+xx <= NUMGPOINTSW:  # -2
						if b+yy > 0:
							if b+yy <= NUMGPOINTSH: # -2
								Local diffx# = grid[a+xx,b+yy].ox-x1
								Local diffy# = grid[a+xx,b+yy].oy-y1
								Local diffxo# = grid[a+xx,b+yy].ox-grid[a+xx,b+yy].x
								Local diffyo# = grid[a+xx,b+yy].oy-grid[a+xx,b+yy].y
								Local dist# = diffy*diffy+diffx*diffx
								Local disto# = diffyo*diffyo+diffxo*diffxo
								if dist > 1 and disto < 400:
									if dist < 50 * 50:
										grid[a+xx,b+yy].dx:+ diffx*amnt  # /dist*amnt
										grid[a+xx,b+yy].dy:+ diffy*amnt  # /dist*amnt



	def UpdateGrid(self):

		for Local a: int = 1 To NUMGPOINTSW-1
			for Local b: int = 1 To NUMGPOINTSH-1
				Local xx# = 0
				xx:+ grid[a-1,b].x
				xx:+ grid[a,b-1].x
				xx:+ grid[a,b+1].x
				xx:+ grid[a+1,b].x
				xx = xx / 4

				Local yy# = 0
				yy:+ grid[a-1,b].y
				yy:+ grid[a,b-1].y
				yy:+ grid[a,b+1].y
				yy:+ grid[a+1,b].y
				yy = yy / 4

				grid[a,b].update(xx,yy)



	 #  evil!
	def BombShockwave(self, x: int,y: int):
		Local a: int = x/GRIDWIDTH
		Local b: int = y/GRIDHEIGHT
		for Local xx: int = -300 To 300:
			for Local yy: int = -300 To 300:
				if xx*xx + yy*yy < 100000000:
				if a+xx > 0:
					if a+xx <= NUMGPOINTSW:
						if b+yy > 0:
							if b+yy <= NUMGPOINTSH:
								grid[a+xx,b+yy].disrupt(.6*(grid[a+xx,b+yy].x-x),.6*(grid[a+xx,b+yy].y-y))
	 #  /evil


	def Shockwave(self, x: int,y: int):

		Local a: int = x/GRIDWIDTH
		Local b: int = y/GRIDHEIGHT

		for Local xx: int = -3 To 3:
			for Local yy: int = -3 To 3:
				if xx*xx + yy*yy < 10:
				if a+xx > 0:
					if a+xx <= NUMGPOINTSW: # -1
						if b+yy > 0:
							if b + yy <= NUMGPOINTSH: # -1
								grid[a+xx,b+yy].disrupt(4*(grid[a+xx,b+yy].x-x),4*(grid[a+xx,b+yy].y-y))







	def DrawGrid(self, style: int,small: int = False):

		if fullgrid:
				gwlow = 0
				gwhi = NUMGPOINTSW
				ghlow = 0
				ghhi = NUMGPOINTSH
		else:
				gwlow = Max(gxoff/GRIDWIDTH,0)
				gwhi = Min(gwlow+(SCREENW/GRIDWIDTH)+GRIDHILIGHT,NUMGPOINTSW)
				ghlow = Max(gyoff/GRIDHEIGHT,0)
				ghhi = Min(ghlow+(SCREENH/GRIDHEIGHT)+GRIDHILIGHT,NUMGPOINTSH)

		if small:
				gxoff = -SCREENW/8
				gyoff = -SCREENH/8
				gwlow = 0
				gwhi = -gxoff/GRIDWIDTH*6
				ghlow = 0
				ghhi = -gyoff/GRIDHEIGHT*6

		Select style
			Case 0
					# points, 1 colour
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridPoints()
			Case 1
					# points, rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  #cycled colours
					SetBlend LIGHTBLEND
					DrawGridPoints()

			Case 2
					# points(bigger), solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridPointsC(g_opacity)
			Case 3
					# points(bigger), rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  #cycled colours
					SetBlend LIGHTBLEND
					DrawGridPointsC(g_opacity)

			Case 4
					# Lines, solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines()
			Case 5
					# Lines, rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  #cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines()

			Case 6
					# line quads, solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3(g_opacity)
			Case 7
					# line quads, rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  #cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines3(g_opacity)

			Case 8
					# dense mesh - solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines7b()
			Case 9
					# dense mesh - blue
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol
					SetBlend LIGHTBLEND
					DrawGridLines7()


			Case 10
					# draw lines [original,blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines6()
			Case 11
					# draw lines [grid,blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines4()
			Case 12
					# draw lines [diagonal,raspberry,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines5()
			Case 13
					# draw line_strip [rgb-split]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3c()


			Case 14
					# solid quads, 1 colour
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2b()
			Case 15
					# solid quads, rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  #cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines2b()
			Case 16
					# solid quads [blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2()
			Case 17
					# solid quads [sin colour]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2c()
			Case 18
					# draw triangles [moire]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines8()
			Case 19
					# draw line_strip [vcs like]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3b()
			Case 20
				#no grid
				pass


		SetScale 1,1
		SetAlpha 1
		SetLineWidth 2



	def DrawGridPoints(self):
		Local a: int,b: int
		Local boldw: int
		Local boldh: int

		boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
		boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

		SetScale 1,1
		SetLineWidth 1
		for a = gwlow To gwhi-1
			for b = ghlow To ghhi-1
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,2,2


		SetLineWidth 2
		for a = gwlow+boldw To gwhi-1 Step GRIDHILIGHT
			for b = ghlow To ghhi-1
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,3,3


		for a = gwlow To gwhi-1
			for b = ghlow+boldh To ghhi-1 Step GRIDHILIGHT
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,3,3




	def DrawGridPointsb(self):
		Local a: int,b: int
		Local boldw: int
		Local boldh: int

		boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
		boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

		SetScale 1,1
		SetLineWidth 2

		for a = gwlow+1 To gwhi-1
			for b = ghlow+1 To ghhi-1
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,2,2


		for a = gwlow+boldw+1 To gwhi-1 Step GRIDHILIGHT
			for b = ghlow+1 To ghhi-1
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,4,4


		for a = gwlow+1 To gwhi-1
			for b = ghlow+boldh+1 To ghhi-1 Step GRIDHILIGHT
				DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,4,4



	def DrawGridPointsC(alpha; float):
		Local a: int,b: int
		Local boldw: int
		Local boldh: int

		boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
		boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

		SetScale 1.5,1.5
		for a = gwlow + 1 To gwhi - 1
			for b = ghlow + 1 To ghhi - 1
				Local alp# = alpha
				if (b+boldh) Mod GRIDHILIGHT = 0
					alp:+ .25

				if (a+boldw) Mod GRIDHILIGHT = 0
					alp:+ .25

				SetAlpha alp
				DrawImage particleimg, grid[a , b].x - gxoff , grid[a , b].y - gyoff

		SetScale 1 , 1



	def DrawGridLines(self):
		Local a: int,b: int
		Local boldw: int
		Local boldh: int

		boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
		boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

		SetScale 1,1
		SetLineWidth 2
		SetAlpha .9
		for a = gwlow+boldw To gwhi-GRIDHILIGHT Step GRIDHILIGHT
			#DrawLine grid[a,b].x-gxoff, grid[a,b].y-gyoff, grid[a,b+GRIDHILIGHT].x-gxoff, grid[a,b+GRIDHILIGHT].y-gyoff
			glBegin GL_LINE_STRIP
			for b = ghlow+boldh-GRIDHILIGHT To ghhi-GRIDHILIGHT Step GRIDHILIGHT
				glVertex3f(grid[a,b].x-gxoff, grid[a,b].y-gyoff,	 0)
				glVertex3f(grid[a,b+GRIDHILIGHT].x-gxoff,   grid[a,b+GRIDHILIGHT].y-gyoff,   0)

			glEnd

		for b = ghlow+boldh To ghhi-GRIDHILIGHT Step GRIDHILIGHT
			#	   DrawLine grid[a,b].x-gxoff, grid[a,b].y-gyoff, grid[a+GRIDHILIGHT,b].x-gxoff, grid[a+GRIDHILIGHT,b].y-gyoff
			glBegin GL_LINE_STRIP
			for a = gwlow+boldw-GRIDHILIGHT To gwhi-GRIDHILIGHT Step GRIDHILIGHT
				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
				glVertex3f(grid[a+GRIDHILIGHT,b].x-gxoff,   grid[a+GRIDHILIGHT,b].y-gyoff,   0)

			glEnd


	def DrawGridLines2(self):
		Local a: int,b: int
		# draw grid
		SetScale 1,1
		SetLineWidth 1
		Local boldw: int
		Local boldh: int

		boldw = 2-(gwlow Mod 2)
		boldh = 2-(ghlow Mod 2)

		Local i: int=0,delX:Float=0.0,delY:Float=0.0
		Local xy#[8]
		#colAkt=(colAkt+.05) Mod 360.0

		for a = gwlow+boldw-2 To gwhi-1 Step 1
			for b = ghlow+boldh-2+(a Mod 2) To ghhi-1 Step 2
				xy[0] = grid[a,b].x-gxoff
				xy[1] = grid[a,b].y-gyoff

				xy[2] = grid[a+1,b].x-gxoff
				xy[3] = grid[a+1,b].y-gyoff

				xy[4] = grid[a+1,b+1].x-gxoff
				xy[5] = grid[a+1,b+1].y-gyoff

				xy[6] = grid[a,b+1].x-gxoff
				xy[7] = grid[a,b+1].y-gyoff

				#colA=50+50*sin((colAkt*360*a/gwhi*b/ghhi) Mod 360.0)

				delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16
				if delX<delY Then delX=delY
				if delX<0.0 Then delX=0.0
				if delX>90.0 Then delX=90.0
				Local colB#=sin(delX)
				SetColor(20+235*colB,20+100*colB,180-140*colB)
				#SetAlpha((1-colB)*.7+0.3)
				#SetAlpha((1-colB)*.7+0.3-colA/360.0)

				DrawPoly(xy)



	def DrawGridLines2b(self):
		Local a: int,b: int
		# draw grid
		SetScale 1,1
		SetLineWidth 1
		Local boldw: int
		Local boldh: int

		boldw = 2-(gwlow Mod 2)
		boldh = 2-(ghlow Mod 2)

		Local xy #[8]

		for a = gwlow+boldw-2 To gwhi-1 Step 1
			for b = ghlow+boldh-2+(a Mod 2) To ghhi-1 Step 2
				xy[0] = grid[a,b].x-gxoff
				xy[1] = grid[a,b].y-gyoff

				xy[2] = grid[a+1,b].x-gxoff
				xy[3] = grid[a+1,b].y-gyoff

				xy[4] = grid[a+1,b+1].x-gxoff
				xy[5] = grid[a+1,b+1].y-gyoff

				xy[6] = grid[a,b+1].x-gxoff
				xy[7] = grid[a,b+1].y-gyoff
				DrawPoly(xy)



	def DrawGridLines2c(self):
		Local a: int,b: int
		# draw grid
		SetScale 1,1
		SetLineWidth 1
		Local boldw: int
		Local boldh: int

		boldw = 2-(gwlow Mod 2)
		boldh = 2-(ghlow Mod 2)

		Local xy #[8]
		Local i: int=0,j: int=0

		for a = gwlow+boldw-2 To gwhi-1 Step 1
			j += 1
			for b = ghlow+boldh-2+(a Mod 2) To ghhi-1 Step 2
				i:+2
				xy[0] = grid[a,b].x-gxoff
				xy[1] = grid[a,b].y-gyoff
				xy[2] = grid[a+1,b].x-gxoff
				xy[3] = grid[a+1,b].y-gyoff
				xy[4] = grid[a+1,b+1].x-gxoff
				xy[5] = grid[a+1,b+1].y-gyoff
				xy[6] = grid[a,b+1].x-gxoff
				xy[7] = grid[a,b+1].y-gyoff
				SetAlpha(g_opacity-.25*(sin(gcol+i)+cos(j)))
				DrawPoly(xy)



	def DrawGridLines3(self, alpha: float):
		Local a: int,b: int
		Local boldw: int
		Local boldh: int

		boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
		boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

		SetScale 1,1
		SetLineWidth 1
		for a = gwlow To gwhi - 1
			if (a+boldh) Mod GRIDHILIGHT = 0
				SetAlpha alpha+.25
			else:
				SetAlpha alpha

			glBegin GL_LINE_STRIP
			for b = ghlow To ghhi-1
				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
				glVertex3f(grid[a,b+1].x-gxoff,   grid[a,b+1].y-gyoff,   0)

			glEnd

		for b = ghlow To ghhi - 1
			if (b+boldw) Mod GRIDHILIGHT = 0
				SetAlpha alpha+.25
			else:
				SetAlpha alpha

			glBegin GL_LINE_STRIP
			for a = gwlow To gwhi-1
				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
				glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)

			glEnd

#		SetLineWidth 2.0
#		for a = gwlow+boldw To gwhi-1 Step GRIDHILIGHT
#			glBegin GL_LINE_STRIP
#			for b = ghlow To ghhi-1 #-1
#				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
#				glVertex3f(grid[a,b+1].x-gxoff,   grid[a,b+1].y-gyoff,   0)
#			glEnd

#		for b = ghlow+boldh To ghhi-1 Step GRIDHILIGHT
#			glBegin GL_LINE_STRIP
#			for a = gwlow To gwhi-1
#				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
#			glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)

#			glEnd


    def DrawGridLines3b(self):
        Local a: int,b: int
        Local boldw: int
        Local boldh: int

        boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
        boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

        # draw grid
        SetScale 1,1
        SetLineWidth 16#glLineWidth(i)
        for b = ghlow+1 To ghhi-1:
#			   SetAlpha(.46+uniform(.04))
            glBegin GL_LINE_STRIP
            for a = gwlow To gwhi-1:
                glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
                glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)
            glEnd



	   def DrawGridLines3c(self):
			Local a: int,b: int
			Local boldw: int
			Local boldh: int

			boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
			boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

			SetTransform 0,1,1#SetScale 1,1
			moiAkt2:+3
			if moiAkt2>=360:
				moiAkt2:-360

#red
			Local xmax: int=gwhi-1,xmin: int=gwlow+1
			Local ymax: int=ghhi-1,ymin: int=ghlow+1
			Local sinAkt:Float=0.0,sinDel:Float=6.0,sca:Float=0.0
			Local xdel:Float=16,ydel:Float=16
			Local xoff:Float=-4,yoff:Float=-4
			Local rgb:Float=.05,rgbMin:Float=.3,rgbAmp:Float=.2
			Local bor:Float=1.0
			Local anz: int=ymax*.5-1,i: int=0,x: int=0,y: int=0

			sinAkt=moiAkt2
			SetLineWidth 2#1.5#glLineWidth(2)
			glBegin GL_LINE_STRIP
			for i=0 To anz
				#rechts
				for x=xmin To xmax Step 1:
					sinAkt:+sinDel
					if sinAkt>=360:
						sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(sca,rgb,rgb)
					if abs(grid[x,ymin].x-x*xdel)>bor:
						glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
					else:
						glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)


				ymin:+1
				#runter
				for y=ymin To ymax Step 1
					sinAkt:+sinDel
					if sinAkt>=360:
						sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(sca,rgb,rgb)
					if abs(grid[xmax,y].y-y*ydel)>bor Then
						glVertex2f(grid[xmax,y].x-gxoff+xoff,grid[xmax,y].y-gyoff+yoff)
					else:
						glVertex2f(grid[xmax,y].x-gxoff,grid[xmax,y].y-gyoff)


				#links
				for x=xmax To xmin Step -1
					sinAkt:+sinDel
					if sinAkt>=360:
						sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(sca,rgb,rgb)
					if abs(grid[x,ymax].x-x*xdel)>bor:
						glVertex2f(grid[x,ymax].x-gxoff+xoff,grid[x,ymax].y-gyoff+yoff)
					else:
						glVertex2f(grid[x,ymax].x-gxoff,grid[x,ymax].y-gyoff)

				xmax:-1
				ymax:-1
				#hoch
				for y=ymax To ymin Step -1
					sinAkt:+sinDel
					if sinAkt>=360:
						sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(sca,rgb,rgb)
					if abs(grid[xmin,y].y-y*ydel)>bor:
						glVertex2f(grid[xmin,y].x-gxoff+xoff,grid[xmin,y].y-gyoff+yoff)
					else:
						glVertex2f(grid[xmin,y].x-gxoff,grid[xmin,y].y-gyoff)

				xmin:+1

			#rechts
			for x=xmin To xmax Step 1
				sinAkt:+sinDel
				if sinAkt>=360:
					sinAkt:-360
				sca=rgbMin+rgbAmp*sin(sinAkt)
				glColor3f(sca,rgb,rgb)
				if abs(grid[x,ymin].x-x*xdel)>bor:
					glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
				else:
					glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)

			#ymin:+1
			glEnd

#green

			xmax=gwhi-1;xmin=gwlow+1
			ymax=ghhi-1;ymin=ghlow+1
			sinAkt=moiAkt2
			anz=ymax*.5-1;i=0;x=0;y=0

			SetLineWidth 2#1.5
			glBegin GL_LINE_STRIP
			for i=0 To anz
				#rechts
				for x=xmin To xmax Step 1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,sca,rgb)
					glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)

				ymin:+1
				#runter
				for y=ymin To ymax Step 1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,sca,rgb)
					glVertex2f(grid[xmax,y].x-gxoff,grid[xmax,y].y-gyoff)

				#links
				for x=xmax To xmin Step -1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,sca,rgb)
					glVertex2f(grid[x,ymax].x-gxoff,grid[x,ymax].y-gyoff)

				xmax:-1
				ymax:-1
				#hoch
				for y=ymax To ymin Step -1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,sca,rgb)
					glVertex2f(grid[xmin,y].x-gxoff,grid[xmin,y].y-gyoff)

				xmin:+1
				#rechts
				for x=xmin To xmax Step 1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,sca,rgb)
					glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)

			#ymin:+1
			glEnd


#blue
			xmax=gwhi-1;xmin=gwlow+1
			ymax=ghhi-1;ymin=ghlow+1
			sinAkt=moiAkt2
			xoff=0;yoff=0
			anz=ymax*.5-1;i=0;x=0;y=0

			SetLineWidth 2#1.5
			glBegin GL_LINE_STRIP
			for i=0 To anz
					#rechts
					for x=xmin To xmax Step 1
							sinAkt:+sinDel
							if sinAkt>=360 Then sinAkt:-360
							sca=rgbMin+rgbAmp*sin(sinAkt)
							glColor3f(rgb,rgb,sca)
							glVertex2f(x*xdel-gxoff+xoff,ymin*ydel-gyoff)
							#glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)

					ymin:+1
					#runter
					for y=ymin To ymax Step 1
							sinAkt:+sinDel
							if sinAkt>=360 Then sinAkt:-360
							sca=rgbMin+rgbAmp*sin(sinAkt)
							glColor3f(rgb,rgb,sca)
							glVertex2f(xmax*xdel-gxoff,y*ydel-gyoff)
							#glVertex2f(grid[xmax,y].x-gxoff+xoff,grid[xmax,y].y-gyoff+yoff)

					#links
					for x=xmax To xmin Step -1
							sinAkt:+sinDel
							if sinAkt>=360 Then sinAkt:-360
							sca=rgbMin+rgbAmp*sin(sinAkt)
							glColor3f(rgb,rgb,sca)
							glVertex2f(x*xdel-gxoff,ymax*ydel-gyoff)
							#glVertex2f(grid[x,ymax].x-gxoff+xoff,grid[x,ymax].y-gyoff+yoff)

					xmax:-1
					ymax:-1
					#hoch
					for y=ymax To ymin Step -1
							sinAkt:+sinDel
							if sinAkt>=360 Then sinAkt:-360
							sca=rgbMin+rgbAmp*sin(sinAkt)
							glColor3f(rgb,rgb,sca)
							glVertex2f(xmin*xdel-gxoff,y*ydel-gyoff)
							#glVertex2f(grid[xmin,y].x-gxoff+xoff,grid[xmin,y].y-gyoff+yoff)

					xmin:+1

			#rechts
			for x=xmin To xmax Step 1
					sinAkt:+sinDel
					if sinAkt>=360 Then sinAkt:-360
					sca=rgbMin+rgbAmp*sin(sinAkt)
					glColor3f(rgb,rgb,sca)
					glVertex2f(x*xdel-gxoff,ymin*ydel-gyoff)
					#glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)

			#ymin:+1
			glEnd



	   def DrawGridLines4(self):
			Local a: int,b: int
			# draw grid
			SetScale 1,1
			Local boldw: int
			Local boldh: int
			Local colB:Float=0.0

			boldw = 2-(gwlow Mod 2)
			boldh = 2-(ghlow Mod 2)

			Local delX:Float=0.0,delY:Float=0.0
			Local xy#[8]

			#glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

			for a = gwlow+boldw-2 To gwhi-1 Step 1
				for b = ghlow+boldh-2+(a Mod 2) To ghhi-1 Step 2
					xy[0] = grid[a,b].x-gxoff
					xy[1] = grid[a,b].y-gyoff
					xy[2] = grid[a+1,b].x-gxoff
					xy[3] = grid[a+1,b].y-gyoff
					xy[4] = grid[a+1,b+1].x-gxoff
					xy[5] = grid[a+1,b+1].y-gyoff
					xy[6] = grid[a,b+1].x-gxoff
					xy[7] = grid[a,b+1].y-gyoff

					delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16

					if delX<delY:
						delX=delY

					if delX<0:
						colB=0.0
					elif:
						delX>90:
						colB=1.0
					else:
						colB=sin(delX)


					SetColor(20+235*colB,20+100*colB,180-140*colB)
					SetAlpha((1-colB)*.3+0.7)
					SetLineWidth(1+colB*2)
					DrawLine(xy[0],xy[1],xy[2],xy[3],0)
					DrawLine(xy[2],xy[3],xy[4],xy[5],0)
					DrawLine(xy[4],xy[5],xy[6],xy[7],0)
					DrawLine(xy[6],xy[7],xy[0],xy[1],0)




	   def DrawGridLines5(self):
			   Local a: int,b: int
			   # draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   #glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

			   for a = gwlow+boldw-2 To gwhi-1 Step 1
					   for b = ghlow+boldh-2+(a Mod 2) To ghhi-1 Step 2
							   xy[0] = grid[a,b].x-gxoff
							   xy[1] = grid[a,b].y-gyoff
							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff
							   xy[6] = grid[a,b+1].x-gxoff
							   xy[7] = grid[a,b+1].y-gyoff

							   delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16
							   if delX<delY Then delX=delY
							   if delX<0 Then
									   colB=0.0
							   else: if delX>90 Then
									   colB=1.0
							   else:
									   colB=sin(delX)


							   SetColor(128+127*colB,15+105*colB,63-23*colB)
							   SetAlpha(colB*.2+0.6)
							   SetLineWidth(1+colB*1.5)
							   DrawLine(xy[0],xy[1],xy[4],xy[5],0)
							   DrawLine(xy[6],xy[7],xy[2],xy[3],0)




	   def DrawGridLines6(self):

			   Local a: int,b: int
			   # draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0
			   Local alpha:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   #glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

			   for b = ghlow+boldh-2 To ghhi-1 Step 1
					   y:+1
					   x=0
					   for a = gwlow+boldw-2 To gwhi-1 Step 1
							   x:+1
							   Rem
							   if x>1 Then
									   xy[6] = xy[4]
									   xy[7] = xy[5]
							   else:
									   xy[6] = grid[a,b+1].x-gxoff
									   xy[7] = grid[a,b+1].y-gyoff

							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff

							   delX=xy[2]-xy[6]-16;delY=xy[7]-xy[3]-16
							   End Rem
							   if x>1 Then
									   xy[0] = xy[2]
									   xy[1] = xy[3]
									   xy[6] = xy[4]
									   xy[7] = xy[5]
							   else:
									   xy[0] = grid[a,b].x-gxoff
									   xy[1] = grid[a,b].y-gyoff
									   xy[6] = grid[a,b+1].x-gxoff
									   xy[7] = grid[a,b+1].y-gyoff

							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff

							   delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16
							   if delX<delY Then delX=delY
							   if delX<0 Then
									   colB=0.0
							   else: if delX>90 Then
									   colB=1.0
							   else:
									   colB=sin(delX)

							   #colB=sin(Min(90,Max(0,Max(delX,delY))))

							   SetColor(20+235*colB,20+100*colB,180-140*colB)
							   SetLineWidth(1+colB*1.5)#2?
							   alpha=(1-colB)*.0+.5
							   if a<gwhi-1 Then
									   if (x Mod 4)>0 Then
											   SetAlpha(alpha)
									   else:
											   SetAlpha(alpha+.5)

									   DrawLine(xy[2],xy[3],xy[4],xy[5],0)

							   if b<ghhi-1 Then
									   if (y Mod 4)>0 Then
											   SetAlpha(alpha)
									   else:
											   SetAlpha(alpha+.5)

									   DrawLine(xy[4],xy[5],xy[6],xy[7],0)




	   def DrawGridLines6b(self, alpha: float):
				Local a: int,b: int
				# draw grid
				Local boldw: int
				Local boldh: int

				boldw = 2-(gwlow Mod 2)
				boldh = 2-(ghlow Mod 2)

				Local x: int=0,y: int=0
				Local xy#[8]
				SetLineWidth 2

			   for b = ghlow+boldh-2 To ghhi-1 Step 1
					   y:+1
					   x=0
					   for a = gwlow+boldw-2 To gwhi-1 Step 1
							   x:+1
							   if x>1 Then
								   xy[0] = xy[2]
								   xy[1] = xy[3]
								   xy[6] = xy[4]
								   xy[7] = xy[5]
							   else:
								   xy[0] = grid[a,b].x-gxoff
								   xy[1] = grid[a,b].y-gyoff
								   xy[6] = grid[a,b+1].x-gxoff
								   xy[7] = grid[a,b+1].y-gyoff

							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff

							   if a<gwhi-1 Then
#									   if (x Mod 4)>0 Then
 #											  SetAlpha (alpha)
  #									 else:
   #											SetAlpha(alpha+.25)
	#
									   DrawLine(xy[2],xy[3],xy[4],xy[5],0)

							   if b<ghhi-1 Then
  #									 if (y Mod 4)>0 Then
   #											SetAlpha(alpha)
	#								   else:
	 #										  SetAlpha(alpha+.25)
	  #
									   DrawLine(xy[4],xy[5],xy[6],xy[7],0)



	   Function DrawGridLines7()

			   Local a: int,b: int
			   # draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0
			   Local rgbR:Float=0,rgbG:Float=0,rgbB:Float=0


			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   #glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

			   for b = ghlow+boldh-2 To ghhi-1 Step 1
					   for a = gwlow+boldw-2 To gwhi-1 Step 1
							   if x>1 Then
									   xy[0] = xy[2]
									   xy[1] = xy[3]
									   xy[6] = xy[4]
									   xy[7] = xy[5]
							   else:
									   xy[0] = grid[a,b].x-gxoff
									   xy[1] = grid[a,b].y-gyoff
									   xy[6] = grid[a,b+1].x-gxoff
									   xy[7] = grid[a,b+1].y-gyoff

							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff

							   delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16
							   if delX<delY Then delX=delY
							   if delX<0 Then
									   colB=0.0
							   else: if delX>90 Then
									   colB=1.0
							   else:
									   colB=sin(delX)

							   SetLineWidth(1+colB*1.0)

							   glBegin GL_LINE_LOOP
									   glColor3f(.005,.05,.3)
									   #glColor3f(.3,.1,.05)
									   #glColor3f(.3,.1,.2)
									   glVertex2f(xy[2],xy[3])
									   glVertex2f(xy[4],xy[5])
									   glVertex2f(xy[6],xy[7])
							   glEnd
							   glBegin GL_LINES
									   glColor3f(.005,.05,.3)
									   #glColor3f(.3,.1,.05)
									   #glColor3f(.3,.1,.2)
									   glVertex2f(xy[0],xy[1])
									   glVertex2f(xy[4],xy[5])
							   glEnd





	def DrawGridLines7b(self):
		Local a: int,b: int
		# draw grid
		SetScale 1,1
		Local boldw: int
		Local boldh: int

		boldw = 2-(gwlow Mod 2)
		boldh = 2-(ghlow Mod 2)

#		Local xy#[8]
#		Local xold:Float=0
#		Local dif:Float=0

		#Local rgbR: int=95,rgbG: int=23,rgbB: int=23
#		Local rgbR: int=104,rgbG: int=26,rgbB: int=23
#		Local rgbfR:Float= Float(rgbR/256),rgbfG:Float= Float(rgbG/256),rgbfB:Float= Float(rgbB/256)

		#glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

#		SetAlpha 1
#		SetColor rgbR,rgbG,rgbB
		glLineWidth(2)
		#horizontal
		for b = ghlow+boldh-2 To ghhi-1 Step 1
			glBegin GL_LINE_STRIP
			for a = gwlow+boldw-2 To gwhi Step 1
				#glColor3f(.005,.05,.3)
				if a>0 Then
#					dif=Min(50,abs(grid[a,b].x-grid[a-1,b].x-16))*0.02
#					glColor3f(rgbfR+.6*dif,rgbfG+.2*dif,rgbfB-.1*dif)

				glVertex2f(grid[a,b].x-gxoff,grid[a,b].y-gyoff)

			glEnd

		#vertikal
#		SetColor rgbR,rgbG,rgbB
		for a = gwlow+boldw-2 To gwhi-1 Step 1
			glBegin GL_LINE_STRIP
			for b = ghlow+boldh-2 To ghhi Step 1
				#glColor3f(.005,.05,.3)
#				if b>0 Then
#					dif=Min(50,grid[a,b].y-grid[a,b-1].y-16)*0.02
#					glColor3f(rgbfR+.2*dif,rgbfG+.6*dif,rgbfB-.1*dif)
#
				glVertex2f(grid[a,b].x-gxoff,grid[a,b].y-gyoff)

			glEnd

		glLineWidth(1.5)
		#diagonal rechts
#		SetColor rgbR,rgbG,rgbB
		Local xmax: int=gwhi,ymax: int=ghhi
		Local anz: int=xmax+ymax,i: int=0,j: int=0,anzB: int=0,xa: int=0,ya: int=ymax+1,x: int=0,y: int=0
		for i=0 To anz-1
			if i<=ymax Then
				anzB:+1
				ya:-1
			else:
				anzB=Min(ymax+1,xmax-xa)
				xa:+1

			x=xa
			y=ya
			glBegin GL_LINE_STRIP
			for j=1 To anzB
				#glColor3f(.005,.05,.3)
				glVertex2f(grid[x,y].x-gxoff,grid[x,y].y-gyoff)
				x:+1
				y:+1

			glEnd

		#diagonal links
		anzB=0;xa=-1;ya=0;x=0;y=0
		for i=0 To anz-1
			if i<=xmax Then
				anzB=Min(ymax+1,anzB+1)
				xa:+1
			else:
				anzB:-1
				ya:+1

			x=xa
			y=ya
			glBegin GL_LINE_STRIP
			for j=1 To anzB
				#glColor3f(.005,.05,.3)
				glVertex2f(grid[x,y].x-gxoff,grid[x,y].y-gyoff)
				x:-1
				y:+1

			glEnd



	def DrawGridLines8()

			   Local a: int,b: int
			   # draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local sca:Float=0.0,sinAkt:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   #glEnable GL_POLYGON_SMOOTH; glHint GL_POLYGON_SMOOTH, GL_NICEST

			   moiAkt:+.05
			   if moiAkt>=360 Then moiAkt:-360
			   sinAkt=36*sin(moiAkt)
			   for b = ghlow+boldh-2 To ghhi-1 Step 1
					   for a = gwlow+boldw-2 To gwhi-1 Step 1
							   if x>1 Then
									   xy[6] = xy[4]
									   xy[7] = xy[5]
							   else:
									   xy[6] = grid[a,b+1].x-gxoff
									   xy[7] = grid[a,b+1].y-gyoff

							   xy[2] = grid[a+1,b].x-gxoff
							   xy[3] = grid[a+1,b].y-gyoff
							   xy[4] = grid[a+1,b+1].x-gxoff
							   xy[5] = grid[a+1,b+1].y-gyoff

							   sca=.5+.25*sin(sinAkt*a*b)
							   glBegin GL_TRIANGLES
									   glColor3f(.3,.3,.3)
									   glVertex2f(xy[2],xy[5]+(xy[3]-xy[5])*sca)
									   glColor3f(.3,.3,.0)
									   glVertex2f(xy[4],xy[5])
									   glColor3f(.3,0,0)
									   glVertex2f(xy[4]+(xy[6]-xy[4])*sca,xy[7])
							   glEnd

