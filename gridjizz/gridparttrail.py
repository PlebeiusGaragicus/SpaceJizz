from random import randint, uniform
from math import sin, cos, pi, sqrt



# Import BRL.Random
# Import BRL.FileSystem
# Import "colordefs.bmx"
# Import "utils.bmx"
# Import "images.bmx"








debug: int = 0

moiAkt: float = 0.0
moiAkt2: float = 0.0

numgridstyles: int = 20
windowed: bool = False
MAXPARTICLES: int = 50000
MAXPARTICLELIFE: int = 80
numparticles: int = 2048
particlelife: int = 40
gravityparticles: int = 1
particledecay# = .95
particlestyle: int = 0
numparticlestyles: int = 3  #0,1,2,3
g_red: int = 32
g_green: int = 80
g_blue: int = 200
g_opacity: float = 0.85

fullgrid: bool = True

showstars: int = 300
MAXSTARS: int = 10000

slotcount: int #0 to numparticles-1

partarray:part[]
partarray = New part[MAXPARTICLES+1]

starx: int[MAXSTARS+1]
stary: int[MAXSTARS+1]
stard: float[MAXSTARS+1]

part_LIST:TList = New TList
trail_LIST:TList = New TList
gwlow: int
gwhi: int
ghlow: int
ghhi: int
gxoff: int
gyoff: int

scroll: bool = False
screensize: int = 0
screensizew: int = 1024
screensizeh: int = 768
playsize: int = 0
playsizew: int = 1024
playsizeh: int = 768
gridsize: int = 2
SCREENW: int = 1024
SCREENH: int = 768
PLAYFIELDW: int = 1024 #1280  '2^8*5
PLAYFIELDH: int = 768 #1024  '2^8*2*2
GRIDWIDTH: int = 16   #4,5,8,10,16,20,32,40,64
GRIDHEIGHT: int = 16  #4,8,16,32,64,128,256

GRIDHILIGHT: int = 4

NUMGPOINTSW: int = PLAYFIELDW / GRIDWIDTH # //?
NUMGPOINTSH: int = PLAYFIELDH / GRIDHEIGHT # //?

grid:gridpoint[,]
grid = New gridpoint[5120/4+2, 4096/4+2] # maximum size

a: int
b: int
# for a = 0 To 1920/4
for a in range(480):
	for b in range(300):
		grid[a,b] = New gridpoint


class gfxmode:
	Field w: int
	Field h: int
	Field desc$
	Field s$


gfxmodearr = gfxmode[100]
numgfxmodes: int = 0

playfieldsizes = [
	1024,768,
	512,384,
	640,480,
	720,400,
	720,480,
	720,576,
	800,600,
	1024,720,
	1024,768,
	1152,864,
	1152,870,
	1280,720,
	1280,768,
	1280,800,
	1280,854,
	1280,960,
	1280,1024,
	1440,900,
	1400,1050,
	1600,1024,
	1600,1200,
	1600,1280,
	1680,1050,
	1800,1440,
	1920,1080,
	1920,1200,
	2048,768,
	2048,1536,
	2560,1024,
	2560,1600,
	2560,2048,
	3200,2048,
	3200,2400,
	3840,2400,
	5120,4096
]
numplayfieldsizes: int = 34   #0-33

DefData "USER",   1024, 768
DefData "BWMac",  512,  384 
DefData "VGA",	640,  480
DefData "????",   720,  400
DefData "NTSCDVD",720,  480
DefData "PALDVD", 720,  576
DefData "SVGA",   800,  600
DefData "XGA-",   1024, 720
DefData "XGA",	1024, 768
DefData "XGA+",   1152, 864
DefData "XGA++",  1152, 870
DefData "720p",   1280, 720
DefData "WXGA",   1280, 768
DefData "WXGA+" , 1280, 800
DefData "WXGA++" , 1280, 854
DefData "WXGA+++", 1280, 960
DefData "SXGA",   1280, 1024
DefData "WSXGA",  1440, 900
DefData "SXGA+",  1400, 1050
DefData "WSXGA",  1600, 1024
DefData "UXGA",   1600, 1200
DefData "UXGA+",  1600, 1280
DefData "WSXGA+", 1680, 1050
DefData "?????",  1800, 1440
DefData "1080p",  1920, 1080
DefData "WUXGA",  1920, 1200
DefData "DUALW",  2048, 768
DefData "QXGA",   2048, 1536
DefData "DUALW+", 2560, 1024
DefData "WQXGA",  2560, 1600
DefData "QSXGA",  2560, 2048
DefData "WQSXGA", 3200, 2048
DefData "QUXGA",  3200, 2400
DefData "WQUXGA", 3840, 2400
DefData "HSXGA",  5120, 4096

numgfxmodes: int = 34  # 0-33



gridparttrail_code = """

Function GetGfxModes()
	Local desc$,w: int,h: int

	for Local cnt: int = 0 To numgfxmodes
		Local g:gfxmode = New gfxmode
		ReadData desc$,w,h
		g.w = w
		g.h = h
		g.desc$ = desc$
		g.s$ = g.w+"X"+g.h
		gfxmodearr[cnt] = g
	Next
	 #  set first entry to what the user has in config
	gfxmodearr[0].w = screensizew 
	gfxmodearr[0].h = screensizeh
		
End Function




Function FindSetting()

	screensize = 0  #  pick first one
	playsize = 0  #  use the defaul/file settings
	playfieldsizes[0] = playsizew 
	playfieldsizes[1] = playsizeh
	
	for Local t = 0 To numgfxmodes
		 #  or find the one that matches file 
		if gfxmodearr[t].w = screensizew And gfxmodearr[t].h = screensizeh
			screensize = t
		
	Next
	
End Function


Function SetDimensions()

	SCREENW = gfxmodearr[screensize].w
	SCREENH = gfxmodearr[screensize].h
				
	PLAYFIELDW = playfieldsizes[playsize*2]
	PLAYFIELDH = playfieldsizes[playsize*2+1]
	
	screensizew = gfxmodearr[screensize].w 
	screensizeh = gfxmodearr[screensize].h 
	
	playsizew = PLAYFIELDW 
	playsizeh = PLAYFIELDH
		
End Function


Function SetUp() -> int:

	Local ret: int = True
	
	SetDimensions()

	if windowed 
		if GraphicsModeExists( SCREENW,SCREENH )
			Graphics(SCREENW, SCREENH, 0)
		else:
			Local fh:TStream = WriteFile("errors.txt")
			WriteLine(fh,"Can not set graphics mode: Windowed - "+SCREENW+"X"+SCREENH)
			CloseFile fh 
			ret = False
		
	else:
		Local sucess: int = False
		for Local dep: int = 32 To 16 Step -8
			if GraphicsModeExists( SCREENW,SCREENH,dep)
				Graphics(SCREENW, SCREENH, dep, 60)
				sucess = True
				Exit
			
		Next
		if Not sucess
			Local fh:TStream = WriteFile("errors.txt")
			WriteLine(fh,"Could not set graphics mode: Fullscreen - "+SCREENW+"X"+SCREENH)
			CloseFile fh 
			ret = False 
				
	

	if ret = True
		Select gridsize
			Case 0
				GRIDWIDTH = 4
				GRIDHEIGHT = 4 
			Case 1
				GRIDWIDTH = 8
				GRIDHEIGHT = 8 
			Case 2
				GRIDWIDTH = 16
				GRIDHEIGHT = 16 
			Case 3
				GRIDWIDTH = 32
				GRIDHEIGHT = 32 
		End Select	
			
		NUMGPOINTSW = PLAYFIELDW/GRIDWIDTH
		NUMGPOINTSH = PLAYFIELDH/GRIDHEIGHT
		gridpoint.ResetAll()
	
		LoadImages()
		if PLAYFIELDW > SCREENW Or PLAYFIELDH > SCREENH Then scroll = True
 # 		if PLAYFIELDW <= SCREENW And PLAYFIELDH <= SCREENH Then scroll = False
		gxoff = 0
		gyoff = 0
		
		capturedimg:TImage = CreateImage(SCREENW,SCREENH)
		SetLineWidth 2
		glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST	
		
		CreateStars() 
	
		
	Return ret
	
End Function


 # the background dots
Type gridpoint

	Field ox#,oy#
	Field x#
	Field y#	
	Field dx#,dy#
 # 	Field fx#,fy#
	
	Method Update(xx#,yy#)
	
		if abs(xx-x) > 2 Then dx:+ Sgn(xx-x) 
		if abs(yy-y) > 2 Then dy:+ Sgn(yy-y) 
					
		if abs(ox-x) > 1
			x = x + Sgn(ox-x)
			dx:+ Sgn(ox-x)/2 	
		else:
			x = ox
		
		if abs(oy-y) > 1
			y = y + Sgn(oy-y)
			dy:+ Sgn(oy-y)/2 
		else:
			y = oy
		

		dx = dx *.899  # .89
		dy = dy *.899  # .89

		x = x + dx
		y = y + dy
			
	End Method
	
	
	Function ResetAll()
		Local a: int,b: int
		
		for a = 0 To NUMGPOINTSW
			for b = 0 To NUMGPOINTSH
				grid[a,b].ox = a*GRIDWIDTH
				grid[a,b].oy = b*GRIDHEIGHT
				grid[a,b].x = a*GRIDWIDTH
				grid[a,b].y = b*GRIDHEIGHT
				grid[a,b].dx = 0
				grid[a,b].dy = 0
			Next
		Next
	End Function	

	Method disrupt(xx#,yy#)
			if abs(xx) > 8 Then xx = xx/16
			if abs(yy) > 8 Then yy = yy/16
			dx = dx + xx
			dy = dy + yy
			Local speed# = dx*dx+dy*dy
			if speed > 160  #  128
				dx = dx/speed*128
				dy = dy/speed*128
			
 # 		
	End Method
	
	Function Pull(x1#,y1#, sz: int = 4,amnt#=4)

		Local a: int = x1/GRIDWIDTH
		Local b: int = y1/GRIDHEIGHT
		for Local xx: int = -sz To sz
			for Local yy: int = -sz To sz
				if a+xx > 0
					if a+xx =< NUMGPOINTSW # -2
						if b+yy > 0
							if b+yy =< NUMGPOINTSH # -2
								if xx*xx + yy*yy < sz*sz							
									Local diffx# = grid[a+xx,b+yy].x-x1
									Local diffy# = grid[a+xx,b+yy].y-y1
									Local dist# = Sqr(diffx*diffx+diffy*diffy)
									if dist > 0
 # 									grid[a+xx,b+yy].fx:- diffx*(1-(dist)/(sz*sz*4*256))
 # 									grid[a+xx,b+yy].fy:- diffy*(1-(dist)/(sz*sz*4*256))
									grid[a+xx,b+yy].dx:- diffx/dist*amnt   # *(1-(dist*dist)/(sz*sz*4*256))
									grid[a+xx,b+yy].dy:- diffy/dist*amnt   # *(1-(dist*dist)/(sz*sz*4*256))
 # 									grid[a+xx,b+yy].fx = - diffx/dist*(1-(dist*dist)/(sz*sz*4*256))
 # 									grid[a+xx,b+yy].fy = - diffy/dist*(1-(dist*dist)/(sz*sz*4*256))
									
								
							
						
					
				
			Next
		Next	
	
	End Function


	Function Push(x1#,y1#, sz: int = 4,amnt#=1)
	
		Local a: int = (x1/GRIDWIDTH)
		Local b: int = (y1/GRIDHEIGHT)
		for Local xx: int = -sz To sz
			for Local yy: int = -sz To sz
			 # 	if (xx*xx + yy*yy) < sz*sz
				if a+xx > 0
					if a+xx =< NUMGPOINTSW  # -2
						if b+yy > 0
							if b+yy =< NUMGPOINTSH # -2
								Local diffx# = grid[a+xx,b+yy].ox-x1
								Local diffy# = grid[a+xx,b+yy].oy-y1
								Local diffxo# = grid[a+xx,b+yy].ox-grid[a+xx,b+yy].x
								Local diffyo# = grid[a+xx,b+yy].oy-grid[a+xx,b+yy].y								
								Local dist# = diffy*diffy+diffx*diffx
								Local disto# = diffyo*diffyo+diffxo*diffxo
								if dist > 1 And disto < 400
									if dist < 50*50
										grid[a+xx,b+yy].dx:+ diffx*amnt  # /dist*amnt
										grid[a+xx,b+yy].dy:+ diffy*amnt  # /dist*amnt
																			
								
							
						
					
				 # 
				
			Next
		Next	
	
	End Function

		
	Function UpdateGrid()
	
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
				
			Next
		Next
	End Function
	
	 #  evil!	
	Function BombShockwave(x: int,y: int)
		Local a: int = x/GRIDWIDTH
		Local b: int = y/GRIDHEIGHT
		for Local xx: int = -300 To 300
			for Local yy: int = -300 To 300
				if xx*xx + yy*yy < 100000000
				if a+xx > 0
					if a+xx =< NUMGPOINTSW
						if b+yy > 0
							if b+yy =< NUMGPOINTSH
								grid[a+xx,b+yy].disrupt(.6*(grid[a+xx,b+yy].x-x),.6*(grid[a+xx,b+yy].y-y))
							
						
					
				
				
			Next
		Next	
	End Function
	 #  /evil	
	
	Function Shockwave(x: int,y: int)
		Local a: int = x/GRIDWIDTH
		Local b: int = y/GRIDHEIGHT
		for Local xx: int = -3 To 3
			for Local yy: int = -3 To 3
				if xx*xx + yy*yy < 10
				if a+xx > 0
					if a+xx =< NUMGPOINTSW # -1
						if b+yy > 0
							if b + yy =< NUMGPOINTSH # -1
								grid[a+xx,b+yy].disrupt(4*(grid[a+xx,b+yy].x-x),4*(grid[a+xx,b+yy].y-y))								
							
						
					
				
				
			Next
		Next	
	End Function
	























	
Function DrawGrid(style: int,small: int = False)

		if fullgrid
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
					' points, 1 colour
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridPoints()
			Case 1
					' points, rainbow 
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  'cycled colours
					SetBlend LIGHTBLEND
					DrawGridPoints()
			
			Case 2
					' points(bigger), solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridPointsC(g_opacity)
			Case 3
					' points(bigger), rainbow
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  'cycled colours
					SetBlend LIGHTBLEND
					DrawGridPointsC(g_opacity)		
			
			Case 4
					' Lines, solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines()
			Case 5
					' Lines, rainbow 
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  'cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines()
			
			Case 6
					' line quads, solid 
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3(g_opacity)
			Case 7
					' line quads, rainbow 
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  'cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines3(g_opacity)
			
			Case 8
					' dense mesh - solid
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines7b()
			Case 9
					' dense mesh - blue
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol			
					SetBlend LIGHTBLEND
					DrawGridLines7()
			
			
			Case 10
					' draw lines [original,blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines6()
			Case 11
					' draw lines [grid,blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines4()
			Case 12
					' draw lines [diagonal,raspberry,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines5()
			Case 13
					' draw line_strip [rgb-split]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3c()
			
			
			Case 14
					' solid quads, 1 colour
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2b()
			Case 15
					' solid quads, rainbow 
					SetAlpha abs(g_opacity)
					SetColor rcol,gcol,bcol  'cycled colours
					SetBlend LIGHTBLEND
					DrawGridLines2b()
			Case 16
					' solid quads [blue,stretch]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2()
			Case 17
					' solid quads [sin colour]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines2c()
			Case 18
					' draw triangles [moire]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines8()			
			Case 19
					' draw line_strip [vcs like]
					SetAlpha abs(g_opacity)
					SetColor g_red,g_green,g_blue
					SetBlend LIGHTBLEND
					DrawGridLines3b()
			Case 20
					'no grid
		End Select
		
		SetScale 1,1
		SetAlpha 1
		SetLineWidth 2
	
	End Function	
	
	Function DrawGridPoints()
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
					   Next
			   Next
			   SetLineWidth 2
			   for a = gwlow+boldw To gwhi-1 Step GRIDHILIGHT
					   for b = ghlow To ghhi-1
							   DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,3,3
					   Next
			   Next
			   for a = gwlow To gwhi-1
					   for b = ghlow+boldh To ghhi-1 Step GRIDHILIGHT
							   DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,3,3
					   Next
			   Next
	   End Function


	   Function DrawGridPointsb()
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
					   Next
			   Next
			   for a = gwlow+boldw+1 To gwhi-1 Step GRIDHILIGHT
					   for b = ghlow+1 To ghhi-1
							   DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,4,4
					   Next
			   Next
			   for a = gwlow+1 To gwhi-1
					   for b = ghlow+boldh+1 To ghhi-1 Step GRIDHILIGHT
							   DrawRect grid[a,b].x-gxoff, grid[a,b].y-gyoff,4,4
					   Next
			   Next
 End Function

	Function DrawGridPointsC(alpha#)
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
			Next
		Next
		SetScale 1 , 1
		
	End Function

	   Function DrawGridLines()
			   Local a: int,b: int
			   Local boldw: int
			   Local boldh: int

			   boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
			   boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

			   SetScale 1,1
			   SetLineWidth 2
			   SetAlpha .9
			   for a = gwlow+boldw To gwhi-GRIDHILIGHT Step GRIDHILIGHT
					   'DrawLine grid[a,b].x-gxoff, grid[a,b].y-gyoff, grid[a,b+GRIDHILIGHT].x-gxoff, grid[a,b+GRIDHILIGHT].y-gyoff
					   glBegin GL_LINE_STRIP
					   for b = ghlow+boldh-GRIDHILIGHT To ghhi-GRIDHILIGHT Step GRIDHILIGHT
							   glVertex3f(grid[a,b].x-gxoff, grid[a,b].y-gyoff,	 0)
							   glVertex3f(grid[a,b+GRIDHILIGHT].x-gxoff,   grid[a,b+GRIDHILIGHT].y-gyoff,   0)
					   Next
					   glEnd
			   Next
			   for b = ghlow+boldh To ghhi-GRIDHILIGHT Step GRIDHILIGHT
					   '	   DrawLine grid[a,b].x-gxoff, grid[a,b].y-gyoff, grid[a+GRIDHILIGHT,b].x-gxoff, grid[a+GRIDHILIGHT,b].y-gyoff
					   glBegin GL_LINE_STRIP
					   for a = gwlow+boldw-GRIDHILIGHT To gwhi-GRIDHILIGHT Step GRIDHILIGHT
							   glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
							   glVertex3f(grid[a+GRIDHILIGHT,b].x-gxoff,   grid[a+GRIDHILIGHT,b].y-gyoff,   0)
					   Next
					   glEnd
			   Next
	   End Function


	   Function DrawGridLines2()
			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   SetLineWidth 1
			   Local boldw: int
			   Local boldh: int

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local i: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]
			   'colAkt=(colAkt+.05) Mod 360.0

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

							   'colA=50+50*sin((colAkt*360*a/gwhi*b/ghhi) Mod 360.0)

							   delX=xy[4]-xy[0]-16;delY=xy[5]-xy[1]-16
							   if delX<delY Then delX=delY
							   if delX<0.0 Then delX=0.0
							   if delX>90.0 Then delX=90.0
							   Local colB#=sin(delX)
							   SetColor(20+235*colB,20+100*colB,180-140*colB)
							   'SetAlpha((1-colB)*.7+0.3)
							   'SetAlpha((1-colB)*.7+0.3-colA/360.0)

							   DrawPoly(xy)
					   Next
			   Next

	   End Function


	   Function DrawGridLines2b()
			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   SetLineWidth 1
			   Local boldw: int
			   Local boldh: int

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local xy#[8]

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
					   Next
			   Next
	   End Function


	   Function DrawGridLines2c()
			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   SetLineWidth 1
			   Local boldw: int
			   Local boldh: int

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local xy#[8]
			   Local i: int=0,j: int=0

			   for a = gwlow+boldw-2 To gwhi-1 Step 1
					   j:+1
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
					   Next
			   Next
	   End Function


	Function DrawGridLines3(alpha#)
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
			Next
			glEnd
		Next
		for b = ghlow To ghhi - 1
			if (b+boldw) Mod GRIDHILIGHT = 0
				SetAlpha alpha+.25		
			else:	
				SetAlpha alpha
			
			glBegin GL_LINE_STRIP
			for a = gwlow To gwhi-1
				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
				glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)
			Next
			glEnd
		Next
'		SetLineWidth 2.0
'		for a = gwlow+boldw To gwhi-1 Step GRIDHILIGHT
'			glBegin GL_LINE_STRIP
'			for b = ghlow To ghhi-1 '-1
'				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
'				glVertex3f(grid[a,b+1].x-gxoff,   grid[a,b+1].y-gyoff,   0)
'			Next
'			glEnd
'		Next
'		for b = ghlow+boldh To ghhi-1 Step GRIDHILIGHT
'			glBegin GL_LINE_STRIP
'			for a = gwlow To gwhi-1
'				glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
'			glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)
'			Next
'			glEnd
'		Next
	End Function

	   Function DrawGridLines3b()
			   Local a: int,b: int
			   Local boldw: int
			   Local boldh: int

			   boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
			   boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

			   ' draw grid
			   SetScale 1,1
			   SetLineWidth 16'glLineWidth(i)
			   for b = ghlow+1 To ghhi-1
'			   SetAlpha(.46+uniform(.04))
					   glBegin GL_LINE_STRIP
					   for a = gwlow To gwhi-1
							   glVertex3f(grid[a,b].x-gxoff,	 grid[a,b].y-gyoff,	 0)
							   glVertex3f(grid[a+1,b].x-gxoff,   grid[a+1,b].y-gyoff,   0)
					   Next
					   glEnd
			   Next
	   End Function


	   Function DrawGridLines3c()
			   Local a: int,b: int
			   Local boldw: int
			   Local boldh: int

			   boldw = GRIDHILIGHT-(gwlow Mod GRIDHILIGHT)
			   boldh = GRIDHILIGHT-(ghlow Mod GRIDHILIGHT)

			   SetTransform 0,1,1'SetScale 1,1
			   moiAkt2:+3
			   if moiAkt2>=360 Then moiAkt2:-360

'red
			   Local xmax: int=gwhi-1,xmin: int=gwlow+1
			   Local ymax: int=ghhi-1,ymin: int=ghlow+1
			   Local sinAkt:Float=0.0,sinDel:Float=6.0,sca:Float=0.0
			   Local xdel:Float=16,ydel:Float=16
			   Local xoff:Float=-4,yoff:Float=-4
			   Local rgb:Float=.05,rgbMin:Float=.3,rgbAmp:Float=.2
			   Local bor:Float=1.0
			   Local anz: int=ymax*.5-1,i: int=0,x: int=0,y: int=0

			   sinAkt=moiAkt2
			   SetLineWidth 2'1.5'glLineWidth(2)
			   glBegin GL_LINE_STRIP
			   for i=0 To anz
					   'rechts
					   for x=xmin To xmax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(sca,rgb,rgb)
							   if abs(grid[x,ymin].x-x*xdel)>bor Then
									   glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
							   else:
									   glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)
							   
					   Next
					   ymin:+1
					   'runter
					   for y=ymin To ymax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(sca,rgb,rgb)
							   if abs(grid[xmax,y].y-y*ydel)>bor Then
									   glVertex2f(grid[xmax,y].x-gxoff+xoff,grid[xmax,y].y-gyoff+yoff)
							   else:
									   glVertex2f(grid[xmax,y].x-gxoff,grid[xmax,y].y-gyoff)
							   
					   Next
					   'links
					   for x=xmax To xmin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(sca,rgb,rgb)
							   if abs(grid[x,ymax].x-x*xdel)>bor  Then
									   glVertex2f(grid[x,ymax].x-gxoff+xoff,grid[x,ymax].y-gyoff+yoff)
							   else:
									   glVertex2f(grid[x,ymax].x-gxoff,grid[x,ymax].y-gyoff)
							   
					   Next
					   xmax:-1
					   ymax:-1
					   'hoch
					   for y=ymax To ymin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(sca,rgb,rgb)
							   if abs(grid[xmin,y].y-y*ydel)>bor Then
									   glVertex2f(grid[xmin,y].x-gxoff+xoff,grid[xmin,y].y-gyoff+yoff)
							   else:
									   glVertex2f(grid[xmin,y].x-gxoff,grid[xmin,y].y-gyoff)
							   
					   Next
					   xmin:+1
			   Next
			   'rechts
			   for x=xmin To xmax Step 1
					   sinAkt:+sinDel
					   if sinAkt>=360 Then sinAkt:-360
					   sca=rgbMin+rgbAmp*sin(sinAkt)
					   glColor3f(sca,rgb,rgb)
					   if abs(grid[x,ymin].x-x*xdel)>bor Then
							   glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
					   else:
							   glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)
					   
			   Next
			   'ymin:+1
			   glEnd

'green

			   xmax=gwhi-1;xmin=gwlow+1
			   ymax=ghhi-1;ymin=ghlow+1
			   sinAkt=moiAkt2
			   anz=ymax*.5-1;i=0;x=0;y=0

			   SetLineWidth 2'1.5
			   glBegin GL_LINE_STRIP
			   for i=0 To anz
					   'rechts
					   for x=xmin To xmax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,sca,rgb)
							   glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)
					   Next
					   ymin:+1
					   'runter
					   for y=ymin To ymax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,sca,rgb)
							   glVertex2f(grid[xmax,y].x-gxoff,grid[xmax,y].y-gyoff)
					   Next
					   'links
					   for x=xmax To xmin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,sca,rgb)
							   glVertex2f(grid[x,ymax].x-gxoff,grid[x,ymax].y-gyoff)
					   Next
					   xmax:-1
					   ymax:-1
					   'hoch
					   for y=ymax To ymin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,sca,rgb)
							   glVertex2f(grid[xmin,y].x-gxoff,grid[xmin,y].y-gyoff)
					   Next
					   xmin:+1
			   Next
			   'rechts
			   for x=xmin To xmax Step 1
					   sinAkt:+sinDel
					   if sinAkt>=360 Then sinAkt:-360
					   sca=rgbMin+rgbAmp*sin(sinAkt)
					   glColor3f(rgb,sca,rgb)
					   glVertex2f(grid[x,ymin].x-gxoff,grid[x,ymin].y-gyoff)
			   Next
			   'ymin:+1
			   glEnd

'blue

			   xmax=gwhi-1;xmin=gwlow+1
			   ymax=ghhi-1;ymin=ghlow+1
			   sinAkt=moiAkt2
			   xoff=0;yoff=0
			   anz=ymax*.5-1;i=0;x=0;y=0

			   SetLineWidth 2'1.5
			   glBegin GL_LINE_STRIP
			   for i=0 To anz
					   'rechts
					   for x=xmin To xmax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,rgb,sca)
							   glVertex2f(x*xdel-gxoff+xoff,ymin*ydel-gyoff)
							   'glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
					   Next
					   ymin:+1
					   'runter
					   for y=ymin To ymax Step 1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,rgb,sca)
							   glVertex2f(xmax*xdel-gxoff,y*ydel-gyoff)
							   'glVertex2f(grid[xmax,y].x-gxoff+xoff,grid[xmax,y].y-gyoff+yoff)
					   Next
					   'links
					   for x=xmax To xmin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,rgb,sca)
							   glVertex2f(x*xdel-gxoff,ymax*ydel-gyoff)
							   'glVertex2f(grid[x,ymax].x-gxoff+xoff,grid[x,ymax].y-gyoff+yoff)
					   Next
					   xmax:-1
					   ymax:-1
					   'hoch
					   for y=ymax To ymin Step -1
							   sinAkt:+sinDel
							   if sinAkt>=360 Then sinAkt:-360
							   sca=rgbMin+rgbAmp*sin(sinAkt)
							   glColor3f(rgb,rgb,sca)
							   glVertex2f(xmin*xdel-gxoff,y*ydel-gyoff)
							   'glVertex2f(grid[xmin,y].x-gxoff+xoff,grid[xmin,y].y-gyoff+yoff)
					   Next
					   xmin:+1
			   Next
			   'rechts
			   for x=xmin To xmax Step 1
					   sinAkt:+sinDel
					   if sinAkt>=360 Then sinAkt:-360
					   sca=rgbMin+rgbAmp*sin(sinAkt)
					   glColor3f(rgb,rgb,sca)
					   glVertex2f(x*xdel-gxoff,ymin*ydel-gyoff)
					   'glVertex2f(grid[x,ymin].x-gxoff+xoff,grid[x,ymin].y-gyoff+yoff)
			   Next
			   'ymin:+1
			   glEnd
	   End Function


	   Function DrawGridLines4()
			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   'glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

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
							   

							   SetColor(20+235*colB,20+100*colB,180-140*colB)
							   SetAlpha((1-colB)*.3+0.7)
							   SetLineWidth(1+colB*2)
							   DrawLine(xy[0],xy[1],xy[2],xy[3],0)
							   DrawLine(xy[2],xy[3],xy[4],xy[5],0)
							   DrawLine(xy[4],xy[5],xy[6],xy[7],0)
							   DrawLine(xy[6],xy[7],xy[0],xy[1],0)
					   Next
			   Next

	   End Function


	   Function DrawGridLines5()
			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   'glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

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
					   Next
			   Next

	   End Function


	   Function DrawGridLines6()

			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0
			   Local alpha:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   'glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

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
							   
							   'colB=sin(Min(90,Max(0,Max(delX,delY))))

							   SetColor(20+235*colB,20+100*colB,180-140*colB)
							   SetLineWidth(1+colB*1.5)'2?
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
							   
					   Next
			   Next

	End Function
	
	   Function DrawGridLines6b(alpha#)

			   Local a: int,b: int
			   ' draw grid
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
'									   if (x Mod 4)>0 Then
 '											  SetAlpha (alpha)
  '									 else:
   '											SetAlpha(alpha+.25)
	'								   
									   DrawLine(xy[2],xy[3],xy[4],xy[5],0)
							   
							   if b<ghhi-1 Then
  '									 if (y Mod 4)>0 Then
   '											SetAlpha(alpha)
	'								   else:
	 '										  SetAlpha(alpha+.25)
	  '								 
									   DrawLine(xy[4],xy[5],xy[6],xy[7],0)
							   
					   Next
			   Next

	End Function
	

	   Function DrawGridLines7()

			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local colB:Float=0.0
			   Local rgbR:Float=0,rgbG:Float=0,rgbB:Float=0


			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   'glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST

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
									   'glColor3f(.3,.1,.05)
									   'glColor3f(.3,.1,.2)
									   glVertex2f(xy[2],xy[3])
									   glVertex2f(xy[4],xy[5])
									   glVertex2f(xy[6],xy[7])
							   glEnd
							   glBegin GL_LINES
									   glColor3f(.005,.05,.3)
									   'glColor3f(.3,.1,.05)
									   'glColor3f(.3,.1,.2)
									   glVertex2f(xy[0],xy[1])
									   glVertex2f(xy[4],xy[5])
							   glEnd

					   Next
			   Next

	   End Function


	Function DrawGridLines7b()
		Local a: int,b: int
		' draw grid
		SetScale 1,1
		Local boldw: int
		Local boldh: int
		
		boldw = 2-(gwlow Mod 2)
		boldh = 2-(ghlow Mod 2)
		
'		Local xy#[8]
'		Local xold:Float=0
'		Local dif:Float=0
		
		'Local rgbR: int=95,rgbG: int=23,rgbB: int=23
'		Local rgbR: int=104,rgbG: int=26,rgbB: int=23
'		Local rgbfR:Float= Float(rgbR/256),rgbfG:Float= Float(rgbG/256),rgbfB:Float= Float(rgbB/256)
		
		'glEnable GL_LINE_SMOOTH; glHint GL_LINE_SMOOTH, GL_NICEST
		
'		SetAlpha 1
'		SetColor rgbR,rgbG,rgbB
		glLineWidth(2)
		'horizontal
		for b = ghlow+boldh-2 To ghhi-1 Step 1
			glBegin GL_LINE_STRIP
			for a = gwlow+boldw-2 To gwhi Step 1
				'glColor3f(.005,.05,.3)
				if a>0 Then
'					dif=Min(50,abs(grid[a,b].x-grid[a-1,b].x-16))*0.02
'					glColor3f(rgbfR+.6*dif,rgbfG+.2*dif,rgbfB-.1*dif)
				
				glVertex2f(grid[a,b].x-gxoff,grid[a,b].y-gyoff)
			Next
			glEnd
		Next
		'vertikal
'		SetColor rgbR,rgbG,rgbB
		for a = gwlow+boldw-2 To gwhi-1 Step 1
			glBegin GL_LINE_STRIP
			for b = ghlow+boldh-2 To ghhi Step 1
				'glColor3f(.005,.05,.3)
'				if b>0 Then
'					dif=Min(50,grid[a,b].y-grid[a,b-1].y-16)*0.02
'					glColor3f(rgbfR+.2*dif,rgbfG+.6*dif,rgbfB-.1*dif)
'				
				glVertex2f(grid[a,b].x-gxoff,grid[a,b].y-gyoff)
			Next
			glEnd
		Next
		glLineWidth(1.5)
		'diagonal rechts
'		SetColor rgbR,rgbG,rgbB
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
				'glColor3f(.005,.05,.3)
				glVertex2f(grid[x,y].x-gxoff,grid[x,y].y-gyoff)
				x:+1
				y:+1
			Next
			glEnd
		Next
		'diagonal links
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
				'glColor3f(.005,.05,.3)
				glVertex2f(grid[x,y].x-gxoff,grid[x,y].y-gyoff)
				x:-1
				y:+1
			Next
			glEnd
		Next		
	End Function


	Function DrawGridLines8()

			   Local a: int,b: int
			   ' draw grid
			   SetScale 1,1
			   Local boldw: int
			   Local boldh: int
			   Local sca:Float=0.0,sinAkt:Float=0.0

			   boldw = 2-(gwlow Mod 2)
			   boldh = 2-(ghlow Mod 2)

			   Local x: int=0,y: int=0,delX:Float=0.0,delY:Float=0.0
			   Local xy#[8]

			   'glEnable GL_POLYGON_SMOOTH; glHint GL_POLYGON_SMOOTH, GL_NICEST

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

					   Next
			   Next

	   End Function	
		
EndType



"""


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


#	Function Create( x#, y# ,typ: int, r: int,g: int,b: int, rot: int = 0, sz: int = 1)
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
					' random
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
					' 3 dirs
					dir = 120*randint(0,2)+rot
					mag = uniform(3,10)			
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 3
					' 4 dirs
					dir = 90*randint(0,3)+rot
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 6
					' 8 dirs
					dir = 45*randint(0,7)+rot
					mag = uniform(3,10)
					p.dx = cos(dir)*mag
					p.dy = sin(dir)*mag
				Case 7
					' any dir and speed
					mag = uniform(.5,1)			
					p.dx = cos(rot)*mag
					p.dy = sin(rot)*mag
					' evil!
				Case 9
					' bomb internal particles
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
					
				Next	
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

	



def CreateStars():
	for t in range(MAXSTARS):
		starx[t] = randint(-100, max(PLAYFIELDW,SCREENW)+100)
		stary[t] = randint(-100, max(PLAYFIELDH,SCREENH)+100)
		stard[t] = 2 + float(t % 8)/4


def DrawStars():
	if showstars > 0:
		SetBlend lightblend		
		SetScale 2,2
		SetAlpha .8
		SetLineWidth 2.0

		for t in showstars:
			SetColor 480/stard[t],480/stard[t],480/stard[t]		
			DrawRect starx[t]-gxoff/stard[t],stary[t]-gyoff/stard[t],1,1

		SetAlpha 1
		SetScale 1,1
