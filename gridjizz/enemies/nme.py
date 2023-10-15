
class Nme:
    def __init__(self, x, y, r, move):
        self.x = x
        self.y = y
        self.r = r
        self.move = move

    def draw(self, screen, gxoff, gyoff):
        sc = (self.r // 16) % 8 + 0.5
        sqa = [0.0, 12.0, 12.0, 0.0, 0.0, -12.0, -12.0, 0.0]

        # Set the color (COL_SQUARE_R, COL_SQUARE_G, COL_SQUARE_B)
        color = (255, 0, 0)  # Replace with your desired color

        # Calculate the rotation in degrees
        rotation = math.degrees(self.r + math.radians(45))

        # Calculate scaling based on the 'move' value
        if self.move > 0:
            scale = min(float(self.move) / 5.0, 1.0)
        else:
            scale = sc

        # Create a rotated and scaled copy of the polygon
        scaled_sqa = [s * scale for s in sqa]
        rotated_sqa = []
        for i in range(0, len(scaled_sqa), 2):
            x = scaled_sqa[i]
            y = scaled_sqa[i + 1]
            x_rot = x * cos(self.r) - y * sin(self.r)
            y_rot = x * sin(self.r) + y * cos(self.r)
            rotated_sqa.extend([x_rot, y_rot])

        # Create a surface for the rotated and scaled polygon
        polygon_surface = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.polygon(polygon_surface, color, rotated_sqa)

        # Blit the polygon surface onto the screen
        screen.blit(polygon_surface, (self.x - gxoff, self.y - gyoff))








class nme:
	""" green square """
	x: float
	y: float
	dx: float
	dy: float
	r: float
	move: int

	def __init__(self, x: float, y: float, freeze:bool, close:int = 0):

		if close == 0:
			SafeXY(x,y,px,py,160)
		else
			SafeXY(x,y,px,py,40,1)

		pan: float = (x-px) / PLAYFIELDW
		vol: float = (1 - abs(pan)/10) * (1 - (abs(y-py) / PLAYFIELDH) / 10)

		PlaySound2(nme_born_snd,1, pan, vol)
		
		dir: int
		mag: float

		self.killer:bool = False
		self.x = x
		self.y = y
		self.r =  90 # Rand(0,359)
		self.dir = random.randint(0,359)
		self.mag = random.uniform(2,4)
		self.dx = cos(dir) * mag
		self.dy = sin(dir) * mag
		self.move = freeze
		NME_LIST.AddLast( self )
		# return n


	def update(self):
		if self.move > 0:
			self.move -= 1
			return

		distx: float
		disty: float	
		dist: float
		othern: nme

		r = r + 1
		x = x + dx
		y = y + dy
		if x < 12:
			dx = abs(dx)
			x = x + dx
		elif x > PLAYFIELDW - 12:
			dx = -abs(dx)
			x = x + dx

		if y < 12:
			dy = abs(dy)
			y = y + dy
		elif y > PLAYFIELDH - 12:
			dy = -abs(dy)
			y = y + dy

		self.toward(px,py,PLAYFIELDW)
		self.blackHole()

		for othernme in NME_LIST:
			if othern != self:
				distx: float = othern.x-x
				disty: float = othern.y-y
				dist: float = (distx * distx + disty * disty)
				if dist < 30 * 30 + 24 * 24:
					self.dx -= distx / 4
					self.dy -= disty / 4


		speed: float = sqrt(dx*dx+dy*dy)
		if speed > speed_nme:
			dx = dx/speed * speed_nme
			dy = dy/speed * speed_nme

		distx: float = x-px
		disty: float = y-py
		dist:float = (distx * distx + disty * disty)
		if dist < 24 * 24:
			killer = True
			if self.KillPlayer():
				NME_LIST.Remove( self )

	
	def blackhole(self):
		n5:nme5
		for n5 in NME5_LIST:
			if n5.active:
				ddx: float = n5.x-x
				ddy: float = n5.y-y 
				dist: float = Sqr(ddx*ddx + ddy*ddy) + 0.001
				if dist < 75 + n5.sz * 8:
					dx = dx + ddx/dist/512*(1200-dist)
					dy = dy + ddy/dist/512*(1200-dist)
					if dist < 12 + n5.sz / 2:
						self.Kill(False)
						n5.Grow(1)


	def toward(self, xx:float, yy: float, range: int):
		ddx: float = xx - self.x
		ddy: float = yy-y 
		dist: float = sqrt(ddx*ddx + ddy*ddy)+0.001
		if dist < range:
			dx = dx + ddx / dist
			dy = dy + ddy / dist


	def runAway(self, x1: float, y1: float, x2: float, y2: float):
		ddx: float = x1- self.x - (x1-x2) * 4
		ddy: float = y1- self.y - (y1-y2) * 4
		bdx: float = x1 - x2
		bdy: float = y1 - y2

		distd: float = sqrt(ddx*ddx + ddy*ddy)+0.001
		distb: float = sqrt(bdx*bdx + bdy*bdy)+0.001

		if distd < 100:
			ddx = -ddx/distd*30
			ddy = -ddy/distd*30
			ddx += bdx/distb*30
			ddy += bdy/distb*30
			dx = dx + ddx
			dy = dy + ddy

			speed: float = sqrt(self.dx * self.dx + self.dy * self.dy)
			if speed > speed_nme * 1.1:
				self.dx = self.dx / speed * speed_nme*1.1
				self.dy = self.dy / speed * speed_nme*1.1


		
	def Kill(self, points: bool = True):
		if points:
			score.IncScore(self.x, self.y, 100)

			pan: float = (self.x-px)/PLAYFIELDW
			vol: float = (1 - abs(pan)/10) * (1 - (abs(self.y - py) / PLAYFIELDH) / 10)
			PlaySound2(quarkhitsound,1.1, pan, vol)

		for t in range(0, 15):
			part.Create(self.x, self.y, 6, COL_SQUARE_R, COL_SQUARE_G, COL_SQUARE_B)

		gridpoint.Shockwave(self.x, self.y)
		NME_LIST.remove( self )


	def draw(self):
		sc: float
		sqa = [0.0,12.0, 12.0,0.0, 0.0,-12.0, -12.0,0.0]
		SetColor COL_SQUARE_R,COL_SQUARE_G,COL_SQUARE_B
		SetBlend ALPHABLEND
		SetOrigin x-gxoff,y-gyoff
		SetRotation(r+45)
		sc = (self.r/16) % 8 + 0.5

		if move > 0:
			SetAlpha move / 40.0
			SetScale move / 5.0, move / 5.0
		else:
			SetAlpha 0.5-sc/8		
			SetScale sc,sc

		DrawPoly sqa
		
		SetColor 255,255,255
		SetOrigin 0,0
		SetAlpha 1
		SetScale 1,1		
		SetBlend lightblend
		SetRotation(r)
		DrawImage greensquare, self.x - gxoff, self.y - gyoff
		SetRotation 0

