# TAKEN FROM gridparttrail

from random import randint, uniform
from math import sin, cos, pi, sqrt

from gridparttrail import *





 # trail
class trail:

	Field x#,y#,r: int,g: int,b: int
	Field dx#,dy#
	Field active: int

	def __init__(self, x: float, y: float, r: int, g: int, b: int, dx: float, dy: float):
		# p:trail = New trail
		self.x = x
		self.y = y
		self.dx = dx * 1.5
		self.dy = dy * 1.5
		self.r = r
		self.g = g
		self.b = b
		self.active = 40
		trail_list.addfirst( self )

	def Update(self):
		active -= 1

		if active < 28:
			r *= .91
			g *= .88
			b *= .86
			x += dx
			y += dy
			dx *= 0.999
			dy *= 0.999

		if active <= 0:
			trail_LIST.Remove( self )


	def DrawTrail(self):
		SetBlend lightblend
		SetScale 2,2
		SetAlpha .23

		for p in trail_list:
			SetColor p.r,p.g,p.b
			DrawRect p.x-gxoff,p.y-gyoff,1,1	# p.x-gxoff+p.dx,p.y-gyoff+p.dy

		for p in trail_list:
			SetColor p.r,p.g,p.b
			DrawImage particleimg,p.x-gxoff,p.y-gyoff

		SetAlpha 1
		SetScale 1,1


	def UpdateTrail(self):
		Local p:trail
		for p in trail_list:
			p.Update()
