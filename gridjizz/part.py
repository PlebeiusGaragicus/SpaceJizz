# TAKEN FROM gridparttrail

from random import randint, uniform
from math import sin, cos, pi, sqrt

from gridparttrail import *




# particles
class part:

	Field x#,y#,dx#,dy#,r: int,g: int,b: int
	Field active: int

	def CreateAll(self):
		for t in range(MAXPARTICLES-1):
			partarray[t] = New part
			partarray[t].x = 0
			partarray[t].y = 0
			partarray[t].r = 0
			partarray[t].g = 0
			partarray[t].b = 0
			partarray[t].active = 0
			partarray[t].dx = 0
			partarray[t].dy = 0
			Part_list.addlast( partarray[t] )

		slotcount = 0


#	def Create( x#, y# ,typ: int, r: int,g: int,b: int, rot: int = 0, sz: int = 1)
	def Create(self, x: float, y: float, typ: int, r: int, g: int, b: int, rot: float = 0, sz: int = 1):
			p:Part
			flag: int
			dir: int

			p:Part = partarray[slotcount]
			p.x = x
			p.y = y
			p.r = r
			p.g = g
			p.b = b
			p.active = randint(particlelife-20,particlelife)

			Select typ
				Case 0
					# random
					dir = randint(0,359)
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 1
					mag = 16
					p.dx = cos(rot)*mag
					p.dy = sin(rot)*mag
					p.active = 24
				Case 2
					dir = rot
					mag = 8
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 8
					# 3 dirs
					dir = 120*randint(0,2)+rot
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 3
					# 4 dirs
					dir = 90*randint(0,3)+rot
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 6
					# 8 dirs
					dir = 45*randint(0,7)+rot
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 7
					# any dir and speed
					mag = uniform(.5,1)
					p.dx = cos(rot)*mag
					p.dy = sin(rot)*mag
					# evil!
				Case 9
					# bomb internal particles
					dir = randint(0,359)
					mag = uniform(1,13)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
					# /evil



			p.dx = p.dx*2
			p.dy = p.dy*2
			p.x:+ p.dx*sz
			p.y:+ p.dy*sz

			slotcount += 1
			if slotcount > numparticles - 1:
				slotcount = 0



	def UpdateWide(self):
		if active > 0:
			x = x + dx
			y = y + dy

			if x =< dx:
				dx = abs(dx)
				x = x + dx*2

			if x > SCREENW-1-dx:
				dx = -abs(dx)
				x = x + dx*2

			if y <= dy:
				dy = abs(dy)
				y = y + dy*2

			if y > SCREENH-1-dy:
				dy = -abs(dy)
				y = y + dy*2

			dx = dx *particledecay
			dy = dy *particledecay
			active:-1
			if active < 20
				if active < 10
					r:*.8 # ;if r < 0 Then r = 0
					g:*.8 # ;if g < 0 Then g = 0
					b:*.8 # ;if b < 0 Then b = 0
				else:
					r:*.97 # ;if r < 0 Then r = 0
					g:*.97 # ;if g < 0 Then g = 0
					b:*.97 # ;if b < 0 Then b = 0

			else:if active > 200
				active = 200




	def Update(self):
		if active > 0:
			x = x + dx
			y = y + dy
			if x <= dx:
				dx = abs(dx)
				x = x + dx*2

			if x > PLAYFIELDW-1-dx:
				dx = -abs(dx)
				x = x + dx*2

			if y <= dy:
				dy = abs(dy)
				y = y + dy*2

			if y > PLAYFIELDH-1-dy:
				dy = -abs(dy)
				y = y + dy*2

			dx = dx * particledecay
			dy = dy * particledecay
			active:-1
			if active < 20:
				if active < 10:
					r *= .8 # ;if r < 0 Then r = 0
					g *= .8 # ;if g < 0 Then g = 0
					b *= .8 # ;if b < 0 Then b = 0
				else:
					r *= .97 # ;if r < 0 Then r = 0
					g *= .97 # ;if g < 0 Then g = 0
					b *= .97 # ;if b < 0 Then b = 0

			elif active > 200:
				active = 200



	def DrawParticles(self):
		Local p:part
		Local t: int

		Select particlestyle

			Case 0
				SetBlend lightblend
				SetScale 2,2
				SetAlpha 1
				SetLineWidth 1.0
				for t = 0 To numparticles-1
					p:part = partarray[t]
					if p.active > 0
						Local rr%,gg%,bb%
						rr = p.r*1.25;if rr>255 Then rr = 255
						gg = p.g*1.25;if gg>255 Then gg = 255
						bb = p.b*1.25;if bb>255 Then bb = 255
						SetColor rr,gg,bb
						DrawLine p.x-gxoff,p.y-gyoff,p.x-gxoff+p.dx,p.y-gyoff+p.dy

				SetAlpha 1
				SetLineWidth 2.0
				SetScale 1,1
			Case 1
				SetBlend lightblend
				SetScale 2,2  # 3,3
				SetAlpha .9
				SetLineWidth 2
				for t in range( numparticles-1 ):
					p:part = partarray[t]
					if p.active > 0
						Local rr%,gg%,bb%
						rr = p.r*1.25;if rr>255 Then rr = 255
						gg = p.g*1.25;if gg>255 Then gg = 255
						bb = p.b*1.25;if bb>255 Then bb = 255
						SetColor rr,gg,bb
						DrawLine p.x-gxoff,p.y-gyoff,p.x-gxoff+p.dx,p.y-gyoff+p.dy



				SetAlpha 1
				SetLineWidth 2.0
				SetScale 1,1
			Case 2
				SetBlend lightblend
				SetScale .5,.5
				for t in range ( numparticles-1 ):
					p:part = partarray[t]
					if p.active > 0:
						Local rr%,gg%,bb%
						rr = p.r*1.5;if rr>255 Then rr = 255
						gg = p.g*1.5;if gg>255 Then gg = 255
						bb = p.b*1.5;if bb>255 Then bb = 255
						SetColor rr,gg,bb
						 # SetAlpha .7
						 # DrawImage particleimg,p.x-gxoff,p.y-gyoff
						SetAlpha 1  # .9
						DrawImage particleimg,p.x-gxoff+p.dx,p.y-gyoff+p.dy


				SetAlpha 1
				SetScale 1,1
			Case 3   # bloom lines
				Local win:Float,px:Float,py:Float # ,dx:Float,dy:Float
				Local rr: int,gg: int,bb: int

				SetBlend lightblend
				SetLineWidth 2
				SetAlpha .8
				SetTransform 0,2,2

				for t in range ( numparticles-1 ):
					p:part = partarray[t]
					if p.active > 0:
						rr = p.r*1.25;if rr>255 Then rr = 255
						gg = p.g*1.25;if gg>255 Then gg = 255
						bb = p.b*1.25;if bb>255 Then bb = 255
						SetColor rr,gg,bb
						px=p.x-gxoff;py=p.y-gyoff
						DrawLine px,py,px+p.dx,py+p.dy


				for t in range ( numparticles-1 ):
					p:part = partarray[t]
					if p.active > 0:
						rr = p.r*1.25;if rr>255 Then rr = 255
						gg = p.g*1.25;if gg>255 Then gg = 255
						bb = p.b*1.25;if bb>255 Then bb = 255
						SetColor rr,gg,bb

						win=ATan(p.dy/p.dx)
						px=p.x-gxoff;py=p.y-gyoff
						SetAlpha .25
						SetTransform win,Sqr(p.dx*p.dx+p.dy*p.dy)*.4,1.2
						DrawImage particleimg,px+p.dx*1.0,py+p.dy*1.0


				SetAlpha 1
				SetTransform 0,1,1
				SetLineWidth 2.0



	def UpdateParticles(self, ww: int=0):
		p:part
		t: int
		if ww:
			for t in range ( numparticles-1 ):
				p:part = partarray[t]
				if p.active > 0:
					p.UpdateWide()
		else:
			for t in range ( numparticles-1 ):
				p:part = partarray[t]
				if p.active > 0:
					p.Update()




	def CreateFireWorks(self, style: int):
		t: int
		x: int
		y: int
		r: int
		g: int
		b: int

		r = randint(0,3)*64
		g = randint(0,3)*64
		b = randint(0,3)*64
		if style == 1:
			if randint(0,1):
				x = randint(100,SCREENW-100)
				y = 16
				if randint(0,1):
					y = SCREENH-16
				else:
					y = randint(50,SCREENH-50)
					x = 16

				if randint(0,1):
					x = SCREENW-16

		elif style == 2:
			x = SCREENW/2
			y = SCREENH/2
		else:
			x = randint(100,SCREENW-100)
			y = randint(50,SCREENH-50)

		for t in range(63):
			part.Create(x,y,0,r,g,b)



	def ResetAll(self):
		# Local p:Part
		# Local t: int

		for t in range( MAXPARTICLES ): # MAXPARTICLES-1, actually #TODO need to make consistent
			p:Part = partarray[t]
			p.x = 0
			p.y = 0
			p.r = 0
			p.g = 0
			p.b = 0
			p.active = 0
			p.dx = 0
			p.dy = 0

		slotcount = 0
