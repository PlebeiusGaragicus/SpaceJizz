# import PUB.FreeJoy

from sound import *
from gridparttrail import *
from vectorfont import *

#### GLOBALS #############

g_style: int = 0
info: str = " "
infotimer: int
mx: int
my: int
ax: int
assigning: bool = False
assigningoption: bool = False
assigningbomb: bool = False
bombtime: int = 30
jdmx: float = 0
jdmy: float = 0
jdfx: float = 0
jdfy: float = 0
playgame: bool = False
startingdifficulty: int = 1
laststartingdifficulty: int = 1
numplayers: int = 3
numbombs: int = 3
EXTRALIFE: int = 100000
POWERUP: int = 2500
EXTRABOMB: int = 150000
mbut$[] = ["None", "Left", "Right", "Middle"]
onoff$[] = ["Off","On"]
difficulty$[] = ["Easy","Medium","Hard"]
NUMGFXSETS: int = 5-1
lowmedhigh = ["Solid","Low","Med","High","User"]
soundsets = ["original", "User"]

exbomb = [100000,150000,250000]
exlife = [75000,100000,200000]

#### END GLOBAL #############




Type bbjoypad
	Field x1id: int
	Field y1id: int
	Field x2id: int
	Field y2id: int
	Field x1invert: int
	Field y1invert: int
	Field x2invert: int
	Field y2invert: int
	Field x1scale#
	Field y1scale#
	Field x2scale#
	Field y2scale#
	Field x1center#
	Field y1center#
	Field x2center#
	Field y2center#
	Field x1dz#
	Field y1dz#
	Field x2dz#
	Field y2dz#
	Field optionbutton%
	Field bombbutton%
End Type

j:bbjoypad[4]

for Local port: int = 0 To 3
	j[port] = New bbjoypad
	j[port].x1id = 1
	j[port].y1id = 2
	j[port].x2id = 4
	j[port].y2id = 3
	j[port].x1invert = 1 #toggles between 1 and -1
	j[port].y1invert = 1
	j[port].x2invert = 1
	j[port].y2invert = 1
	j[port].x1scale: float = 1
	j[port].y1scale: float = 1
	j[port].x2scale: float = 1
	j[port].y2scale: float = 1
	j[port].x1center: float = 0
	j[port].y1center: float = 0
	j[port].x2center: float = 0
	j[port].y2center: float = 0
	j[port].x1dz: float = 0
	j[port].y1dz: float = 0
	j[port].x2dz: float = 0
	j[port].y2dz: float = 0
	j[port].optionbutton% = 1
	j[port].bombbutton% = 2


joy_label$[16]
joy_label[0] = "null"
joy_label[1] = "JoyX()"
joy_label[2] = "JoyY()"
joy_label[3] = "JoyZ()"
joy_label[4] = "JoyR()"
joy_label[5] = "JoyU()"
joy_label[6] = "JoyV()"
joy_label[7] = "JoyYaw()"
joy_label[8] = "JoyPitch()"
joy_label[9] = "JoyRoll()"
joy_label[10] = "JoyHat()"
joy_label[11] = "JoyWheel()"
joy_label[12] = "JoyAxis12()"
joy_label[13] = "JoyAxis13()"
joy_label[14] = "JoyAxis14()"
joy_label[15] = "JoyAxisl5()"

control_method$[5]
control_method[0] = "Dual Analog"
control_method[1] = "Mouse"
control_method[2] = "Keyboard"
control_method[3] = "Joypad"
control_method[4] = "Hybrid"


#defaults
controltype: int = 0
deadbandadjust: int  = 0

joyport: int = 0
autofire: int = 0

axis_move_x: int = 0
axis_move_y: int = 1
axis_fire_x: int = 3
axis_fire_y: int = 2
axis_move_x_inv: int = 1   #1 or -1
axis_move_y_inv: int = 1
axis_fire_x_inv: int = 1
axis_fire_y_inv: int = 1
axis_move_x_sc# = 1   #1, 128, 255
axis_move_y_sc# = 1
axis_fire_x_sc# = 1
axis_fire_y_sc# = 1
axis_move_x_center# = 0   #-0.9 to .9
axis_move_y_center# = 0
axis_fire_x_center# = 0
axis_fire_y_center# = 0
axis_move_x_dz# = 0.05
axis_move_y_dz# = 0.05
axis_fire_x_dz# = 0.05
axis_fire_y_dz# = 0.05
j_d_bomb: int = 5
j_d_option: int = 4

h_config: int = 0

j_config: int = 0
j_pad_1: int = 0
j_pad_2: int = 1
j_pad_3: int = 2
j_pad_4: int = 3
j_pad_bomb: int = 4
j_pad_option: int = 0

k_bomb: int = KEY_SPACE
k_move_left: int = KEY_S
k_move_right: int = KEY_D
k_move_up: int = KEY_E
k_move_down: int = KEY_X
k_fire_left: int = KEY_LEFT
k_fire_right: int = KEY_RIGHT
k_fire_up: int = KEY_UP
k_fire_down: int = KEY_DOWN

m_sensitivity# = .5
m_bomb: int = 2
m_fire: int = 1
inertia# = 0.0




def DrawTarget(x%,y%,cnt%,sz%=7):

	if cnt % 30 > 14
		SetColor 255,255,32
	else:
		SetColor 255,32,32

#	DrawLine x-12,y,x+12,y
#	DrawLine x,y-12,x,y+12

	for Local a%=0 Until 359 Step 45
		SetRotation ((cnt*8) % 360)+a
		DrawLine x-sz,y-sz,x+sz,y+sz

	SetRotation 0





def LoadConfig() -> bool:

	Local fh:TStream, fn$
	Local pv$, pm$

	fn$ = "Config.txt"
	fh = OpenFile(fn$)
	if fh != None
		while not Eof(fh)
			# read each line
			pm$ = ReadLine(fh)
			pv$ = ReadLine(fh)
			Select pm$
				Case "[Windowed]"
					if Pv.toupper() = "TRUE"
						windowed = True
					else:
						windowed = False

				Case "[Control Type]"
					if Pv.toupper() = control_method[0].toupper()
						controltype = 0 #dual analog
					elif Pv.toupper() = control_method[1].toupper()
						controltype = 1 #mouse
					elif Pv.toupper() = control_method[2].toupper()
						controltype = 2 #keys
					elif Pv.toupper() = control_method[3].toupper()
						controltype = 3	#joypad
					elif Pv.toupper() = control_method[4].toupper()
						controltype = 4	#hybrid

				Case "[Autofire]"
					autofire = Int(pv$)

				Case "[Hybrid Config]"
					h_config = Int(pv$)

				Case "[Joypad Config]"
					j_config = Int(pv$)
				Case "[Joypad Left]"
					j_pad_1 = Int(pv$)
				Case "[Joypad Up]"
					j_pad_2 = Int(pv$)
				Case "[Joypad Right]"
					j_pad_3 = Int(pv$)
				Case "[Joypad Down]"
					j_pad_4 = Int(pv$)
				Case "[Joypad Option]"
					j_pad_option = Int(pv$)
				Case "[Joypad Bomb]"
					j_pad_bomb = Int(pv$)

				Case "[Key Bomb]"
					k_bomb = Int(pv$)
				Case "[Key Move Left]"
					k_move_left = Int(pv$)
				Case "[Key Move Right]"
					k_move_right = Int(pv$)
				Case "[Key Move Up]"
					k_move_up = Int(pv$)
				Case "[Key Move Down]"
					k_move_down = Int(pv$)
				Case "[Key Fire Left]"
					k_fire_left = Int(pv$)
				Case "[Key Fire Right]"
					k_fire_right = Int(pv$)
				Case "[Key Fire Up]"
					k_fire_up = Int(pv$)
				Case "[Key Fire Down]"
					k_fire_down = Int(pv$)

				Case "[SFX Volume]" #0-100
					sfxvol# = Float(pv$)/100.0
				Case "[Music Volume]" #0-100
					musicvol# = Float(pv$)/100.0
				Case "[Sound Set]"
					soundset = Int(pv$)
					if soundset < 0 or soundset > 1: soundset = 0

				Case "[Grid Style]"
					g_style = Int(pv$)

				Case "[Grid Red]"
					g_red = Int(pv$)
				Case "[Grid Green]"
					g_green = Int(pv$)
				Case "[Grid Blue]"
					g_blue = Int(pv$)
				Case "[Grid Opacity]" #0-100
					g_opacity# = Float(pv$)/100.0
				Case "[Grid Spacing]"
					gridsize = Int(pv$)
				Case "[Full Grid]"
					fullgrid = Int(pv$)
					if fullgrid < 0 or fullgrid > 1: fullgrid = 0
				Case "[Gfx Set]"
					gfxset = Int(pv$)
					if gfxset < 0 or gfxset > NUMGFXSETS: gfxset = 0

				Case "[Mouse Sensitivity]"
					m_sensitivity = Float(pv$)/100.0
				Case "[Mouse Fire]"
					m_fire = Int(pv$)
				Case "[Mouse Bomb]"
					m_bomb = Int(pv$)

				Case "[Show Stars]"
					showstars = Int(pv$)
				Case "[Scroll]"
					scroll = Int(pv$)
				Case "[Playfield Width]"
					playsizew = Int(pv$)
				Case "[Playfield Height]"
					playsizeh = Int(pv$)
				Case "[Screen Width]"
					screensizew = Int(pv$)
				Case "[Screen Height]"
					screensizeh = Int(pv$)

				Case "[Particle Count]"
					numparticles = Int(pv$)
					if numparticles > MAXPARTICLES: numparticles = MAXPARTICLES
				Case "[Particle Life]"
					particlelife = Int(pv$)
					if particlelife > 500: particlelife = 500
				Case "[Particle Gravity]"
					gravityparticles = Int(pv$)
				Case "[Particle Decay]"
					particledecay# = Float(pv$)
					if particledecay < .01: particledecay = .01
					if particledecay > .9999: particledecay = .9999
				Case "[Particle Style]"
					particlestyle = Int(pv$)

				Case "[Difficulty]"
					startingdifficulty = Int(pv$)

				Case "[Inertia]"
					inertia# = Float(pv$)/100.0

				Case "[Used Port]"
					joyport = Int(pv$)
				Case "[Joy Port]"
					Local port: int = Int(pv$)
					for Local t: int = 0 To 21
						Local ax$ = ReadLine(fh)
						Local cn$ = ReadLine(fh)
						Select ax$
							Case "[Joy Move X]"
								j[port].x1id = Int(cn$)
							Case "[Joy Move Y]"
								j[port].y1id = Int(cn$)
							Case "[Joy Fire X]"
								j[port].x2id = Int(cn$)
							Case "[Joy Fire Y]"
								j[port].y2id = Int(cn$)

							Case "[Joy Move X Inverted]"
								j[port].x1invert = Int(cn$)
								if abs(j[port].x1invert) != 1: j[port].x1invert = 1
							Case "[Joy Move Y Inverted]"
								j[port].y1invert = Int(cn$)
								if abs(j[port].y1invert) != 1: j[port].y1invert = 1
							Case "[Joy Fire X Inverted]"
								j[port].x2invert = Int(cn$)
								if abs(j[port].x2invert) != 1: j[port].x2invert = 1
							Case "[Joy Fire Y Inverted]"
								j[port].y2invert = Int(cn$)
								if abs(j[port].y2invert) != 1: j[port].y2invert = 1

							Case "[Joy Move X Scale]"
								j[port].x1scale = Int(cn$)
								if j[port].x1scale = 0: j[port].x1scale = 1
							Case "[Joy Move Y Scale]"
								j[port].y1scale = Int(cn$)
								if j[port].y1scale = 0: j[port].y1scale = 1
							Case "[Joy Fire X Scale]"
								j[port].x2scale = Int(cn$)
								if j[port].x2scale = 0: j[port].x2scale = 1
							Case "[Joy Fire Y Scale]"
								j[port].y2scale = Int(cn$)
								if j[port].y2scale = 0: j[port].y2scale = 1

							Case "[Joy Move X Center]"
								j[port].x1center = Float(cn$)
								if abs(j[port].x1center) > 1: j[port].x1center = 0
							Case "[Joy Move Y Center]"
								j[port].y1center = Float(cn$)
								if abs(j[port].y1center) > 1: j[port].y1center = 0
							Case "[Joy Fire X Center]"
								j[port].x2center = Float(cn$)
								if abs(j[port].x2center) > 1: j[port].x2center = 0
							Case "[Joy Fire Y Center]"
								j[port].y2center = Float(cn$)
								if abs(j[port].y2center) > 1: j[port].y2center = 0

							Case "[Joy Move X Dead Zone]"
								j[port].x1dz = Float(cn$)
								if abs(j[port].x1dz) > 1: j[port].x1dz = 0
							Case "[Joy Move Y Dead Zone]"
								j[port].y1dz = Float(cn$)
								if abs(j[port].y1dz) > 1: j[port].y1dz = 0
							Case "[Joy Fire X Dead Zone]"
								j[port].x2dz = Float(cn$)
								if abs(j[port].x2dz) > 1: j[port].x2dz = 0
							Case "[Joy Fire Y Dead Zone]"
								j[port].y2dz = Float(cn$)
								if abs(j[port].y2dz) > 1: j[port].y2dz = 0
							Case "[Joy Option]"
								j[port].optionbutton = Int(cn$)
							Case "[Joy Bomb]"
								j[port].bombbutton = Int(cn$)





		info$ = "Config file loaded."
		infotimer = 30*4
		CloseFile fh
		return True
	else:
		info$ = "Config load failed."
		infotimer = 30*4
		return False







def SaveConfig() -> bool:

	Local fh:TStream, fn$

	fn$ = "Config.txt"
	fh = WriteFile(fn$)
	if fh != None
		WriteLine (fh,"[Windowed]")
		if windowed
			WriteLine(fh,"True")
		else:
			WriteLine(fh,"False")

		WriteLine(fh,"[Control Type]")
		WriteLine(fh,control_method[controltype])

		WriteLine(fh,"[Hybrid Config]")
		WriteLine(fh,h_config)

		WriteLine(fh,"[Joypad Config]")
		WriteLine(fh,j_config)
		WriteLine(fh,"[Joypad Left]")
		WriteLine(fh,j_pad_1)
		WriteLine(fh,"[Joypad Up]")
		WriteLine(fh,j_pad_2)
		WriteLine(fh,"[Joypad Right]")
		WriteLine(fh,j_pad_3)
		WriteLine(fh,"[Joypad Down]")
		WriteLine(fh,j_pad_4)
		WriteLine(fh,"[Joypad Option]")
		WriteLine(fh,j_pad_option)
		WriteLine(fh,"[Joypad Bomb]")
		WriteLine(fh,j_pad_bomb)

		WriteLine(fh,"[Autofire]")
		WriteLine(fh,autofire)

		WriteLine(fh,"[Key Bomb]")
		WriteLine(fh,k_bomb)
		WriteLine(fh,"[Key Move Left]")
		WriteLine(fh,k_move_left)
		WriteLine(fh,"[Key Move Right]")
		WriteLine(fh,k_move_right)
		WriteLine(fh,"[Key Move Up]")
		WriteLine(fh,k_move_up)
		WriteLine(fh,"[Key Move Down]")
		WriteLine(fh,k_move_down)
		WriteLine(fh,"[Key Fire Left]")
		WriteLine(fh,k_fire_left)
		WriteLine(fh,"[Key Fire Right]")
		WriteLine(fh,k_fire_right)
		WriteLine(fh,"[Key Fire Up]")
		WriteLine(fh,k_fire_up)
		WriteLine(fh,"[Key Fire Down]")
		WriteLine(fh,k_fire_down)

		WriteLine(fh,"[SFX Volume]")
		WriteLine(fh,Int(sfxvol#*100))
		WriteLine(fh,"[Music Volume]")
		WriteLine(fh,Int(musicvol#*100))
		WriteLine(fh,"[Sound Set]")
		WriteLine(fh,soundset)

		WriteLine(fh,"[Grid Style]")
		WriteLine(fh,g_style)

		WriteLine(fh,"[Grid Red]")
		WriteLine(fh,g_red)
		WriteLine(fh,"[Grid Green]")
		WriteLine(fh,g_green)
		WriteLine(fh,"[Grid Blue]")
		WriteLine(fh,g_blue)
		WriteLine(fh,"[Grid Opacity]")
		WriteLine(fh,Int(g_opacity#*100))
		WriteLine(fh,"[Grid Spacing]")
		WriteLine(fh,gridsize)
		WriteLine(fh,"[Full Grid]")
		WriteLine(fh,fullgrid)
		WriteLine(fh,"[Gfx Set]")
		WriteLine(fh,gfxset)

		WriteLine(fh,"[Show Stars]")
		WriteLine(fh,showstars)
		WriteLine(fh,"[Scroll]")
		WriteLine(fh,scroll)

		WriteLine(fh,"[Playfield Width]")
		WriteLine(fh,playsizew)
		WriteLine(fh,"[Playfield Height]")
		WriteLine(fh,playsizeh)
		WriteLine(fh,"[Screen Width]")
		WriteLine(fh,screensizew)
		WriteLine(fh,"[Screen Height]")
		WriteLine(fh,screensizeh)

		WriteLine(fh,"[Particle Count]")
		WriteLine(fh,numparticles)
		WriteLine(fh,"[Particle Life]")
		WriteLine(fh,particlelife)
		WriteLine(fh,"[Particle Gravity]")
		WriteLine(fh,gravityparticles)
		WriteLine(fh,"[Particle Decay]")
		WriteLine(fh,particledecay)
		WriteLine(fh,"[Particle Style]")
		WriteLine(fh,particlestyle)

		WriteLine(fh,"[Mouse Sensitivity]")
		WriteLine(fh,Int(m_sensitivity#*100))
		WriteLine(fh,"[Mouse Fire]")
		WriteLine(fh,m_fire)
		WriteLine(fh,"[Mouse Bomb]")
		WriteLine(fh,m_bomb)

		WriteLine(fh,"[Difficulty]")
		WriteLine(fh,startingdifficulty)

		WriteLine(fh,"[Inertia]")
		WriteLine(fh,Int(inertia#*100))

		WriteLine(fh,"[Used Port]")
		WriteLine(fh, joyport)
		for Local port: int = 0 To 3
			WriteLine(fh,"[Joy Port]")
			WriteLine(fh, port)
			WriteLine(fh,"[Joy Move X]")
			WriteLine(fh,j[port].x1id)
			WriteLine(fh,"[Joy Move Y]")
			WriteLine(fh,j[port].y1id)
			WriteLine(fh,"[Joy Fire X]")
			WriteLine(fh,j[port].x2id)
			WriteLine(fh,"[Joy Fire Y]")
			WriteLine(fh,j[port].y2id)

			WriteLine(fh,"[Joy Move X Inverted]")
			WriteLine(fh,j[port].x1invert)
			WriteLine(fh,"[Joy Move Y Inverted]")
			WriteLine(fh,j[port].y1invert)
			WriteLine(fh,"[Joy Fire X Inverted]")
			WriteLine(fh,j[port].x2invert)
			WriteLine(fh,"[Joy Fire Y Inverted]")
			WriteLine(fh,j[port].y2invert)

			WriteLine(fh,"[Joy Move X Scale]")
			WriteLine(fh,Int(j[port].x1scale))
			WriteLine(fh,"[Joy Move Y Scale]")
			WriteLine(fh,Int(j[port].y1scale))
			WriteLine(fh,"[Joy Fire X Scale]")
			WriteLine(fh,Int(j[port].x2scale))
			WriteLine(fh,"[Joy Fire Y Scale]")
			WriteLine(fh,Int(j[port].y2scale))

			WriteLine(fh,"[Joy Move X Center]")
			WriteLine(fh,(j[port].x1center))
			WriteLine(fh,"[Joy Move Y Center]")
			WriteLine(fh,(j[port].y1center))
			WriteLine(fh,"[Joy Fire X Center]")
			WriteLine(fh,(j[port].x2center))
			WriteLine(fh,"[Joy Fire Y Center]")
			WriteLine(fh,(j[port].y2center))

			WriteLine(fh,"[Joy Move X Dead Zone]")
			WriteLine(fh,j[port].x1dz)
			WriteLine(fh,"[Joy Move Y Dead Zone]")
			WriteLine(fh,j[port].y1dz)
			WriteLine(fh,"[Joy Fire X Dead Zone]")
			WriteLine(fh,j[port].x2dz)
			WriteLine(fh,"[Joy Fire Y Dead Zone]")
			WriteLine(fh,j[port].y2dz)

			WriteLine(fh,"[Joy Option]")
			WriteLine(fh,j[port].optionbutton)
			WriteLine(fh,"[Joy Bomb]")
			WriteLine(fh,j[port].bombbutton)


		info$ = "Config file saved."
		infotimer = 30*4
		CloseFile fh
		return True
	else:
		return False






# def SaveColours() -> bool:

# 	Local fh:TStream, fn$

# 	fn$ = "Colours.txt"
# 	fh = WriteFile(fn$)
# 	if fh != None
# 		WriteLine(fh,"squares")
# 		WriteLine(fh,COL_SQUARE_R)
# 		WriteLine(fh,COL_SQUARE_G)
# 		WriteLine(fh,COL_SQUARE_B)
# 		WriteLine(fh,"pinwheels")
# 		WriteLine(fh,COL_PIN_R)
# 		WriteLine(fh,COL_PIN_G)
# 		WriteLine(fh,COL_PIN_B)
# 		WriteLine(fh,"diamonds")
# 		WriteLine(fh,COL_DIAMOND_R)
# 		WriteLine(fh,COL_DIAMOND_G)
# 		WriteLine(fh,COL_DIAMOND_B)
# 		WriteLine(fh,"cubes")
# 		WriteLine(fh,COL_CUBE_R)
# 		WriteLine(fh,COL_CUBE_G)
# 		WriteLine(fh,COL_CUBE_B)
# 		WriteLine(fh,"circles")
# 		WriteLine(fh,COL_SEEKER_R)
# 		WriteLine(fh,COL_SEEKER_G)
# 		WriteLine(fh,COL_SEEKER_B)
# 		WriteLine(fh,"butterflies")
# 		WriteLine(fh,COL_BUTTER_R)
# 		WriteLine(fh,COL_BUTTER_G)
# 		WriteLine(fh,COL_BUTTER_B)
# 		WriteLine(fh,"blackholes")
# 		WriteLine(fh,COL_SUN_R)
# 		WriteLine(fh,COL_SUN_G)
# 		WriteLine(fh,COL_SUN_B)
# 		WriteLine(fh,"clone")
# 		WriteLine(fh,COL_CLONE_R)
# 		WriteLine(fh,COL_CLONE_G)
# 		WriteLine(fh,COL_CLONE_B)
# 		WriteLine(fh,"snake head")
# 		WriteLine(fh,COL_SNAKE_R)
# 		WriteLine(fh,COL_SNAKE_G)
# 		WriteLine(fh,COL_SNAKE_B)
# 		WriteLine(fh,"snake tail")
# 		WriteLine(fh,COL_TAIL_R)
# 		WriteLine(fh,COL_TAIL_G)
# 		WriteLine(fh,COL_TAIL_B)
# 		WriteLine(fh,"triangles")
# 		WriteLine(fh,COL_TRIANGLE_R)
# 		WriteLine(fh,COL_TRIANGLE_G)
# 		WriteLine(fh,COL_TRIANGLE_B)
# 		WriteLine(fh,"player")
# 		WriteLine(fh,COL_PLAYER_R)
# 		WriteLine(fh,COL_PLAYER_G)
# 		WriteLine(fh,COL_PLAYER_B)
# 		WriteLine(fh,"shots")
# 		WriteLine(fh,COL_SHOT_R)
# 		WriteLine(fh,COL_SHOT_G)
# 		WriteLine(fh , COL_SHOT_B)
# 		WriteLine(fh,"super shots")
# 		WriteLine(fh,COL_SHOT1_R)
# 		WriteLine(fh,COL_SHOT1_G)
# 		WriteLine(fh,COL_SHOT1_B)
# 		WriteLine(fh,"bouncy shots")
# 		WriteLine(fh,COL_SHOT2_R)
# 		WriteLine(fh,COL_SHOT2_G)
# 		WriteLine(fh , COL_SHOT2_B)
# 		WriteLine(fh,"bomb")
# 		WriteLine(fh,COL_BOMB_R)
# 		WriteLine(fh,COL_BOMB_G)
# 		WriteLine(fh,COL_BOMB_B)
# 		WriteLine(fh,"scores")
# 		WriteLine(fh,COL_SCORE_R)
# 		WriteLine(fh,COL_SCORE_G)
# 		WriteLine(fh,COL_SCORE_B)
# 		WriteLine(fh,"powerups")
# 		WriteLine(fh,COL_POWERUP_R)
# 		WriteLine(fh,COL_POWERUP_G)
# 		WriteLine(fh,COL_POWERUP_B)
# 		WriteLine(fh,"trail")
# 		WriteLine(fh,COL_TRAIL_R)
# 		WriteLine(fh,COL_TRAIL_G)
# 		WriteLine(fh,COL_TRAIL_B)

# 		info$ = "Colour file saved."
# 		infotimer = 30*4
# 		CloseFile fh
# 		return True
# 	else:
# 		return False






# def LoadColours() -> bool:

# 	Local fh:TStream, fn$
# 	Local com$

# 	fn$ = "Colours.txt"
# 	fh = OpenFile(fn$)
# 	if fh != None
# 		com$ = ReadLine(fh)
# 		COL_SQUARE_R = Int(ReadLine(fh))
# 		COL_SQUARE_G = Int(ReadLine(fh))
# 		COL_SQUARE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_PIN_R = Int(ReadLine(fh))
# 		COL_PIN_G = Int(ReadLine(fh))
# 		COL_PIN_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_DIAMOND_R = Int(ReadLine(fh))
# 		COL_DIAMOND_G = Int(ReadLine(fh))
# 		COL_DIAMOND_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_CUBE_R = Int(ReadLine(fh))
# 		COL_CUBE_G = Int(ReadLine(fh))
# 		COL_CUBE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SEEKER_R = Int(ReadLine(fh))
# 		COL_SEEKER_G = Int(ReadLine(fh))
# 		COL_SEEKER_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_BUTTER_R = Int(ReadLine(fh))
# 		COL_BUTTER_G = Int(ReadLine(fh))
# 		COL_BUTTER_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SUN_R = Int(ReadLine(fh))
# 		COL_SUN_G = Int(ReadLine(fh))
# 		COL_SUN_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_CLONE_R = Int(ReadLine(fh))
# 		COL_CLONE_G = Int(ReadLine(fh))
# 		COL_CLONE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SNAKE_R = Int(ReadLine(fh))
# 		COL_SNAKE_G = Int(ReadLine(fh))
# 		COL_SNAKE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_TAIL_R = Int(ReadLine(fh))
# 		COL_TAIL_G = Int(ReadLine(fh))
# 		COL_TAIL_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_TRIANGLE_R = Int(ReadLine(fh))
# 		COL_TRIANGLE_G = Int(ReadLine(fh))
# 		COL_TRIANGLE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_PLAYER_R = Int(ReadLine(fh))
# 		COL_PLAYER_G = Int(ReadLine(fh))
# 		COL_PLAYER_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SHOT_R = Int(ReadLine(fh))
# 		COL_SHOT_G = Int(ReadLine(fh))
# 		COL_SHOT_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SHOT1_R = Int(ReadLine(fh))
# 		COL_SHOT1_G = Int(ReadLine(fh))
# 		COL_SHOT1_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SHOT2_R = Int(ReadLine(fh))
# 		COL_SHOT2_G = Int(ReadLine(fh))
# 		COL_SHOT2_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_BOMB_R = Int(ReadLine(fh))
# 		COL_BOMB_G = Int(ReadLine(fh))
# 		COL_BOMB_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_SCORE_R = Int(ReadLine(fh))
# 		COL_SCORE_G = Int(ReadLine(fh))
# 		COL_SCORE_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_POWERUP_R = Int(ReadLine(fh))
# 		COL_POWERUP_G = Int(ReadLine(fh))
# 		COL_POWERUP_B = Int(ReadLine(fh) )

# 		com$ = ReadLine(fh)
# 		COL_TRAIL_R = Int(ReadLine(fh))
# 		COL_TRAIL_G = Int(ReadLine(fh))
# 		COL_TRAIL_B = Int(ReadLine(fh) )

# 		info$ = "Colour file loaded."
# 		infotimer = 30*4
# 		CloseFile fh
# 		return True
# 	else:
# 		info$ = "Colour file load failed."
# 		infotimer = 30*4
# 		return False




# def CaptureScreen():
# 	GrabImage(capturedimg,0,0)



# def DrawAllStatic(sz: float=1):

# 	SetColor 64,64,128
# 	SetBlend SOLIDBLEND
# 	if capturedimg is not None:
# 		SetScale sz,sz
# 		DrawImage capturedimg,SCREENW/2,SCREENH/2

# 	SetScale 1,1




# TODO - this is an odd one, it returns a number for the option or False
# TODO - it also takes what is essentially a bool but as an int
def Options(showgame: int) -> int:

	Local xx:Int, yy:Int, cnt:Int
	Local ret:Int = 0
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 2+showgame
	Local s#,x:Int
	Local ignorejoy:Int
	Local tim:Int
	Local lsp:Int = 40

	if showgame:
		CaptureScreen()
	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(1+(showgame>0))+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()
		SetLineWidth 2
		tim = time()
		if showgame:
			DrawAllStatic(.9)
		SetColor 255,0,0
		DrawString("Options",SCREENW/2-280,SCREENH/2-lsp*3,6)

		if RectsOverlap(xx-8,yy-8,16,16,0, SCREENH/2-lsp,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Exit Program",SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Settings",SCREENW/2-280,SCREENH/2,4)
		if showgame:
			if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 2
			if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
			DrawString("End Game",SCREENW/2-280,SCREENH/2+lsp,4)

			if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 3
			if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
			DrawString("Continue",SCREENW/2-280,SCREENH/2+lsp*2,4)
		else:
			if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 2
			if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
			DrawString("Continue",SCREENW/2-280,SCREENH/2+lsp,4)

		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		Flip 1
		cnt += 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 2+showgame
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 2+showgame: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if jdmy != 0: ignorejoy = True
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER) or MouseHit(1): done = True
		if KeyHit(KEY_ESCAPE) or KeyHit(KEY_LEFT): sel = 2+showgame;done = True;bombtime = 20
		if KeyHit(KEY_RIGHT): done = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 10
		if sel = 1 and done = True
			ret = Settings(showgame)
			MoveMouse(SCREENW/2-280-20,SCREENH/2+20)
			done = False
			looper = 0
			bombtime = 20
			if ret = 2 and showgame
				FlushKeys()
				FlushMouse()
				return 2


		if showgame
			if sel = 2 and done = True
				if conf(showgame,"End Game?")
					bombtime = 20
					FlushKeys()
					FlushMouse()
					return 2
				else:
					done = False
					bombtime = 20



		if sel = 0 and done = True
			if conf(showgame,"Sure?")
				bombtime = 20
				FlushKeys()
				FlushMouse()
				return 1
			else:
				done = False
				bombtime = 20

		looper += 8

	FlushKeys()
	FlushMouse()
	# return False
	return 0





def conf:Int(showgame:Int, st$="")

	Local xx:Int, yy:Int, cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 1
	Local ignorejoy:Int
	Local tim:Int
	Local lsp:Int = 40

	if st$ = "": st$ = "Confirm"

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp+10)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.8)

		SetColor 255,0,0
		DrawString(st$,SCREENW/2-280,SCREENH/2-lsp*2,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Yes",SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("No",SCREENW/2-280,SCREENH/2+lsp,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		Flip 1
		cnt += 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 1
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 1: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)


		if jdmy != 0: ignorejoy = True
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER) or KeyHit(KEY_ESCAPE) or MouseHit(1): done = True
		if KeyHit(KEY_RIGHT): done = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0:
			bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8:
			done = True
			bombtime = 20
		looper += 8

	if sel = 0:
		return True
	else:
		return False





def Settings:Int(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local ret:Int = 0
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 4
	Local s#,x:Int
	Local ignorejoy:Int
	Local tim:Int
	Local lsp:Int = 40

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*3+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.8)
		SetColor 255,0,0
		DrawString("Settings",SCREENW/2-280,SCREENH/2-lsp*3,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Audio",SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Video",SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Controls",SCREENW/2-280,SCREENH/2+lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Game",SCREENW/2-280,SCREENH/2+lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*3,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		Flip 1
		cnt += 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 4
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 4: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)


		if jdmy != 0: ignorejoy = True
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER) or MouseHit(1): done = True
		if KeyHit(KEY_ESCAPE)  or KeyHit(KEY_LEFT): done = True;sel = 4;bombtime = 20
		if KeyHit(KEY_RIGHT): done = True

		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True
		if done = True
			Select sel
				Case 0 #audio
					AudioSettings(showgame)
					MoveMouse(SCREENW/2-280-20,SCREENH/2-lsp+20)
					done = False
					looper = 0
					bombtime = 20
				Case 1 #video
					ret = VideoSettings(showgame)
					MoveMouse(SCREENW/2-280-20,SCREENH/2+20)
					done = False
					looper = 0
					bombtime = 20
				Case 2 #controller
					ret = ControllerSettings(showgame)
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp+20)
					SetController()
					done = False
					looper = 0
					bombtime = 20
				Case 3 #game settings
					ret = GameSettings(showgame)
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*2+20)
					done = False
					looper = 0
					bombtime = 20
				Case 4 # done
					bombtime = 20

			FlushKeys()
			FlushMouse()

		looper += 8

	return ret







def VideoSettings:Int(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 10 # done
	Local s#,x:Int
	Local ignorejoy:Int, ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40
	if SCREENH =< 480:
		lsp = 32

	Local old_scroll:Int = scroll
	Local old_screensize:Int = screensize
	Local old_playsize:Int = playsize
	Local old_gfxset:Int = gfxset
	Local old_windowed:Int = windowed
	Local bright: float = g_opacity*120
	Local col_pick:Int = 0

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*6+20)
	while not done:
		Cls
		xx = MouseX()
		yy = MouseY()
		SetLineWidth 2
		tim = time()
		if showgame:
			DrawAllStatic(.7)
		SetColor 255,0,0
		DrawString("Video Settings",SCREENW/2-280,SCREENH/2-lsp*6,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*4,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Scroll: "+onoff$[scroll],SCREENW/2-280,SCREENH/2-lsp*4,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*3,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Screen Size: "+(screensize+1)+"/"+numgfxmodes+" "+gfxmodearr[screensize].desc$+" ("+gfxmodearr[screensize].s$+")",SCREENW/2-280,SCREENH/2-lsp*3,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*2,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Playfield Size: "+(playsize+1)+"/"+numplayfieldsizes+" "+playfieldsizes[playsize*2]+"X"+playfieldsizes[playsize*2+1],SCREENW/2-280,SCREENH/2-lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Gfx Set: "+lowmedhigh$[gfxset],SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*0,SCREENW,5*4): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Windowed: "+onoff$[windowed],SCREENW/2-280,SCREENH/2+lsp*0,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*1,SCREENW,5*4): sel = 5
		if sel = 5 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Grid Style: "+g_style,SCREENW/2-280,SCREENH/2+lsp*1,4)
		if sel = 5 or sel = 7 or sel = 8 or sel = 9
			if (cnt % 60 = 0): gridpoint.Pull(Rand(0,20)*GRIDWIDTH,Rand(0,20)*GRIDHEIGHT,8,24)

		CycleColours()
		gridpoint.UpdateGrid()
		gridpoint.DrawGrid(g_style, True)
		gxoff = 0
		gyoff = 0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4):
			sel = 6

		if sel == 6:
			SetColor 255,255,(cnt*8) % 255
		else:
			SetColor 0,200,0

		DrawString("Number of Stars: "+showstars,SCREENW/2-280,SCREENH/2+lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 7
		if sel = 7 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Particle Style: "+particlestyle,SCREENW/2-280,SCREENH/2+lsp*3,4)
		if sel = 7
			if Rand(0,100) > 94: part.CreateFireworks(2)

		part.UpdateParticles(1)
		part.DrawParticles()

		SetColor 255,255,255
		SetScale 2,2
		DrawImage colourpick,SCREENW/2+74,SCREENH/2+lsp*4+14,1
		DrawImage colourpick,SCREENW/2+74,SCREENH/2+lsp*5+14,0
		SetScale 1,1
		SetColor 100,255,100
		DrawRect SCREENW/2+74+2-122+col_pick*2,SCREENH/2+lsp*4+20,2,8
		DrawRect SCREENW/2+74+2-122+bright*2,SCREENH/2+lsp*5+20,2,8
		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*4,SCREENW,5*4): sel = 8
		if sel = 8 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Grid Colour:",SCREENW/2-280,SCREENH/2+lsp*4,4)
		if sel = 8
			SetScale 2,2
			DrawImage colourpick,SCREENW/2+74,SCREENH/2+lsp*4+14,2
			SetScale 1,1


		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*5,SCREENW,5*4): sel = 9
		if sel = 9 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Grid Bright:",SCREENW/2-280,SCREENH/2+lsp*5,4)
		if sel = 9
			SetScale 2,2
			DrawImage colourpick,SCREENW/2+74,SCREENH/2+lsp*5+14,2
			SetScale 1,1


		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*6,SCREENW,5*4): sel = 10
		if sel = 10 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*6,4)


		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 10
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-4)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 10: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-4)+20)


		if jdmy != 0: ignorejoy = True
		if jdmx != 0: ignorexjoy = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20
		if KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 10;bombtime = 20
		if (KeyDown(KEY_LEFT) or MouseDown(1)) and bombtime = 0: jdmx = -1;bombtime = 20
		if (KeyDown(KEY_RIGHT) or MouseDown(2)) and bombtime = 0: jdmx = 1;bombtime = 20
		Select sel
			Case 0
				if jdmx != 0
					scroll = 1-scroll

				done = False
			Case 1
				if jdmx < 0
					screensize -= 1
					if screensize < 0: screensize = numgfxmodes
					bombtime = 8

				if jdmx > 0
					screensize += 1
					if screensize > numgfxmodes: screensize = 0
					bombtime = 8

				done = False
			Case 2
				if jdmx < 0
					playsize -= 1
					if playsize < 0: playsize = numplayfieldsizes
					bombtime = 8

				if jdmx > 0
					playsize += 1
					if playsize > numplayfieldsizes: playsize = 0
					bombtime = 8

				done = False
			Case 3
				if jdmx < 0
					gfxset -= 1
					if gfxset < 0: gfxset = NUMGFXSETS

				if jdmx > 0
					gfxset += 1
					if gfxset > NUMGFXSETS: gfxset = 0

				done = False
			Case 4
				if jdmx != 0
					windowed = 1-windowed

				done = False
			Case 5
				if jdmx > 0
					g_style += 1
					if g_style > numgridstyles: g_style = 0

				if jdmx < 0
					g_style -= 1
					if g_style < 0: g_style = numgridstyles

			Case 6
				if jdmx > 0
					showstars += 100
					if showstars > MAXSTARS: showstars = 0
					bombtime = 8

				if jdmx < 0
					showstars -= 100
					if showstars < 0: showstars = MAXSTARS
					bombtime = 8

			Case 7
				if jdmx > 0
					particlestyle += 1
					if particlestyle > numparticlestyles: particlestyle = 0

				if jdmx < 0
					particlestyle -= 1
					if particlestyle < 0: particlestyle = numparticlestyles

			Case 8 # colour
				if jdmx < 0
					col_pick -= 1
					if col_pick < 0: col_pick = 0
					SetGridColours(col_pick)
					bombtime = 2

				if jdmx > 0
					col_pick += 1
					if col_pick > 119: col_pick = 119
					SetGridColours(col_pick)
					bombtime = 2

				done = False
			Case 9 # brightness
				if jdmx < 0
					bright -= 1
					if bright < 0: bright= 0
					g_opacity = bright/119
					bombtime = 2

				if jdmx > 0
					bright += 1
					if bright> 119: bright= 119
					g_opacity = bright/119
					bombtime = 2

				done = False
			Case 10
				if jdmx != 0: done=True
				#exit this menu

		looper  += 8

	if 	(old_scroll != scroll or old_screensize != screensize or old_playsize != playsize or old_gfxset != gfxset or old_windowed != windowed):
		if conf(showgame,"Keep Changes?"):
			# reload gfx, resize grid
			if setup():
				return 2
			else:
				# can#t set mode - reset to old
				scroll  = old_scroll
				screensize  = old_screensize
				playsize  = old_playsize
				gfxset = old_gfxset
				windowed = old_windowed
				SetDimensions()
				Cls
				SetColor 0,255,255
				DrawString("Unable to set Gfx %e",20,64,3)
				DrawString("Reverting to old settings: "+gfxmodearr[screensize].s$,20,64+30,3)
				Flip 1
				Delay 2000

		else:
			scroll  = old_scroll
			screensize  = old_screensize
			playsize  = old_playsize
			gfxset = old_gfxset
			windowed = old_windowed


	return False





def SetGridColours(ind:Int)
	Local rgb:Int
	Local pm:TPixmap = LockImage:TPixmap(colourpick,1)
	rgb = ReadPixel(pm,1+ind,2)
	UnlockImage(colourpick,1)

	g_red = (rgb Shr 16) & $FF
	g_green = (rgb Shr 8) & $FF
	g_blue = rgb & $FF






def GameSettings:Int(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 5 # done
	Local s#,x:Int
	Local ignorejoy:Int, ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40

	Local old_startingdifficulty:Int = startingdifficulty
	Local old_exlife:Int = exlife[startingdifficulty]
	Local old_exbomb:Int = exbomb[startingdifficulty]
	Local old_autofire:Int = autofire
	Local old_inertia# = inertia
	Local old_scroll:Int = scroll

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*3+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.7)
		SetColor 255,0,0
		DrawString("Game Settings",SCREENW/2-280,SCREENH/2-lsp*4,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*2,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Starting Level: "+difficulty$[startingdifficulty],SCREENW/2-280,SCREENH/2-lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Free Player: "+exlife[startingdifficulty],SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Free Bomb: "+exbomb[startingdifficulty],SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("AutoFire: "+onoff$[autofire],SCREENW/2-280,SCREENH/2+lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Inertia:",SCREENW/2-280,SCREENH/2+lsp*2,4)
		rect SCREENW/2-360+240+1,SCREENH/2+lsp*2+1,inertia*300,24-2,1
		SetColor 255,255,0
		rect SCREENW/2-360+240,SCREENH/2+lsp*2,302,24,0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 5
		if sel = 5 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*3,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 5
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-2)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 5: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-2)+20)

		if jdmy != 0: ignorejoy = True
		if jdmx != 0: ignorexjoy = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20
		if KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 5;bombtime = 20
		if (KeyDown(KEY_LEFT) or MouseDown(1)) and bombtime = 0: jdmx = -1;bombtime = 20
		if (KeyDown(KEY_RIGHT) or MouseDown(2)) and bombtime = 0: jdmx = 1;bombtime = 20
		Select sel
			Case 0
				if jdmx < 0
					startingdifficulty -= 1
					if startingdifficulty < 0: startingdifficulty = 0

				if jdmx > 0
					startingdifficulty += 1
					if startingdifficulty > 2: startingdifficulty = 2

				done = False
			Case 1
				if jdmx < 0
					exlife[startingdifficulty] -= 25000
					if exlife[startingdifficulty]< 25000: exlife[startingdifficulty]= 25000

				if jdmx > 0
					exlife[startingdifficulty] += 25000
					if exlife[startingdifficulty]> 300000: exlife[startingdifficulty]= 300000

				done = False
			Case 2
				if jdmx < 0
					exbomb[startingdifficulty] -= 25000
					if exbomb[startingdifficulty] < 25000: exbomb[startingdifficulty]= 25000

				if jdmx > 0
					exbomb[startingdifficulty] += 25000
					if exbomb[startingdifficulty]> 300000: exbomb[startingdifficulty]= 300000

				done = False
			Case 3
				if jdmx != 0
					autofire = 1-autofire

				done = False
			Case 4
				#inertia
				if jdmx < 0
					inertia -=  0.05
					if inertia< 0: inertia = 0

				if jdmx > 0
					inertia +=  0.05
					if inertia > 1: inertia = 1

				done = False
			Case 5
				if jdmx != 0: done=True
				#exit this menu

		looper += 8

	if 	(old_startingdifficulty != startingdifficulty or old_exlife != exlife[startingdifficulty] or old_exbomb != exbomb[startingdifficulty] or old_autofire != autofire or old_inertia != inertia):
		if conf(showgame,"Keep Changes?"):
			return 2
		else:
			startingdifficulty = old_startingdifficulty
			exlife[startingdifficulty] = old_exlife
			exbomb[startingdifficulty] = old_exbomb
			autofire  = old_autofire
			inertia  = old_inertia

	return False



def AudioSettings(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local done: bool = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 3
	Local s#,x:Int
	Local ignoreyjoy:Int,ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40
	Local oldsoundset:Int = soundset

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*3+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.7)
		SetColor 255,0,0
		DrawString("Audio Settings",SCREENW/2-280,SCREENH/2-lsp*2,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 0
		if sel = 0
			SetColor 0,200,0
			rect SCREENW/2+2,SCREENH/2+2,sfxvol*200,24-2,1
			SetColor 255,255,(cnt*8) % 255
		else:
			SetColor 0,100,0
			rect SCREENW/2+1,SCREENH/2+1,sfxvol*200,24-2,1
			SetColor 0,200,0

		DrawString("SFX Volume:",SCREENW/2-280,SCREENH/2,4)
		rect SCREENW/2,SCREENH/2,202,24,0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 1
		if sel = 1
			SetColor 0,200,0
			rect SCREENW/2+1,SCREENH/2+lsp+1,musicvol*200,24-2,1
			SetColor 255,255,(cnt*8) % 255
		else:
			SetColor 0,100,0
			rect SCREENW/2+1,SCREENH/2+lsp+1,musicvol*200,24-2,1
			SetColor 0,200,0

		DrawString("Music Volume:",SCREENW/2-280,SCREENH/2+lsp,4)
		rect SCREENW/2,SCREENH/2+lsp,202,24,0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Sound Set: "+soundsets$[soundset],SCREENW/2-280,SCREENH/2+lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 3
		if sel = 3: SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*3,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim


		jdmy = GetJoyByAxis(joyport, axis_move_y,axis_move_y_inv,axis_move_y_sc,axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignoreyjoy = False
		if ignoreyjoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x,axis_move_x_inv,axis_move_x_sc,axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 3
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 3: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)

		if (KeyDown(KEY_LEFT) or MouseDown(1)) and bombtime = 0: jdmx = -1;bombtime = 20
		if (KeyDown(KEY_RIGHT) or MouseDown(2)) and bombtime = 0: jdmx = 1;bombtime = 20
		Select sel
			Case 0 # sfxvol
				if jdmx < 0
					sfxvol -=  0.05
					if sfxvol < 0: sfxvol = 0
					AdjustVolume()

				if jdmx > 0
					sfxvol +=  0.05
					if sfxvol > 1: sfxvol = 1
					AdjustVolume()

			Case 1 # musicvol
				if jdmx < 0
					musicvol -=  0.05
					if musicvol < 0: musicvol = 0
					SetMusicVolume()

				if jdmx > 0
					musicvol +=  0.05
					if musicvol > 1: musicvol = 1
					SetMusicVolume()

			Case 2
				if jdmx < 0
					soundset -= 1
					if soundset < 0: soundset = 1

				if jdmx > 0
					soundset += 1
					if soundset > 1: soundset = 0

				done = False
			Case 3 # done
				if jdmx != 0: done=True


		if jdmy != 0: ignoreyjoy = True
		if jdmx != 0: ignorexjoy = True
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 2;bombtime = 20
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True

		looper  += 8

	if soundset != oldsoundset
		LoadSounds()








def ControllerSettings(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 2
	Local s#,x:Int
	Local ignoreyjoy:Int
	Local ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*2+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.7)
		SetColor 255,0,0
		DrawString("Controller Selection",SCREENW/2-280,SCREENH/2-lsp*2,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 0
		if sel = 0: SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Type: "+control_method[controltype],SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 1
		if sel = 1: SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Configure Controls",SCREENW/2-280,SCREENH/2+lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 2
		if sel = 2: SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*2,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignoreyjoy = False
		if ignoreyjoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x,axis_move_x_inv,axis_move_x_sc,axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 2
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 2: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)


		if jdmy != 0: ignoreyjoy = True
		if jdmx != 0: ignorexjoy = True
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 2;bombtime = 20
		if KeyHit(KEY_LEFT) or MouseHit(1): jdmx = -1
		if KeyHit(KEY_RIGHT) or MouseHit(2): jdmx = 1
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20

		Select sel
			Case 0 # control type
				if jdmx < 0 or done = True
					controltype  -=  1
					if controltype < 0: controltype = 4
					done = False

				if jdmx > 0
					controltype  +=  1
					if controltype > 4: controltype = 0

			Case 1 #controller config
				if done = True or jdmx != 0
					Select controltype
						Case 0 #dual analog
							DualAnalogControllerSettings()
						Case 1 #mouse
							MouseControllerSettings(showgame)
						Case 2 #key
							KeyboardControllerSettings(showgame)
						Case 3 #joypad
							JoypadControllerSettings(showgame)
						Case 4 #hybrid
							HybridControllerSettings(showgame)

					SetController()
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel)+20)
					done = False
					looper = 0
					bombtime = 20
					FlushKeys()
					FlushMouse()

			Case 2 # done
				if jdmx != 0: done=True


		looper  += 8





def HybridControllerSettings(showgame:Int)

	Local xx:Int, yy:Int, cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 4
	Local s#,x:Int
	Local ignorejoy:Int,ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*3+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.6)
		SetColor 255,0,0
		DrawString("Hybrid Control",SCREENW/2-280,SCREENH/2-lsp*3,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		Select h_config
			Case 0
				DrawString("Move: Keys* - Aim: Mouse Relative",SCREENW/2-280,SCREENH/2-lsp,4)
			Case 1
				DrawString("Move: Mouse - Fire: Keys*",SCREENW/2-280,SCREENH/2-lsp,4)
			Case 2
				DrawString("Move: Keys* - Aim: Mouse Centered",SCREENW/2-280,SCREENH/2-lsp,4)


		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Fire: "+mbut$[m_fire]+" Mouse Button",SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Bomb: "+mbut$[m_bomb]+" Mouse Button",SCREENW/2-280,SCREENH/2+lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2+100+1,SCREENH/2+lsp*2+1,m_sensitivity*200,24-2,1
		DrawString("Mouse Sensitivity:",SCREENW/2-280,SCREENH/2+lsp*2,4)
		SetColor 255,255,0
		rect SCREENW/2+100,SCREENH/2+lsp*2,202,24,0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*3,4)

		SetColor 0,200,0
		DrawString("* configure in Keys Control",SCREENW/2-280,SCREENH/2+lsp*4,4)

		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 4
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 4: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if jdmy != 0: ignorejoy = True
		if jdmx != 0: ignorexjoy = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 7
			jb = jb + JoyDown(i,joyport)

		if (KeyDown(KEY_LEFT) or MouseDown(1)) and bombtime = 0: jdmx = -1;bombtime = 20
		if (KeyDown(KEY_RIGHT) or MouseDown(2)) and bombtime = 0: jdmx = 1;bombtime = 20
		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 4;bombtime = 20
		Select sel
			Case 0
				if jdmx != 0
					h_config += 1
					if h_config > 2: h_config = 0

				done = False
			Case 1
				if jdmx != 0
					m_fire += 1
					if m_fire > 3: m_fire = 1

				done = False
			Case 2
				if jdmx != 0
					m_bomb += 1
					if m_bomb > 3: m_bomb = 1

				done = False
			Case 3
				if jdmx < 0
					m_sensitivity -=  0.05
					if m_sensitivity< 0: m_sensitivity= 0

				if jdmx > 0
					m_sensitivity +=  0.05
					if m_sensitivity> 1: m_sensitivity= 1

				done = False
			Case 4
				if jdmx != 0: done = True

		looper  += 8







def MouseControllerSettings(showgame:Int)

	Local cnt:Int, xx:Int, yy:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 3
	Local s#,x:Int
	Local ignorejoy:Int,ignorexjoy:Int
	Local tim:Int
	Local lsp:Int = 40

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*2+20)
	while not done
		Cls
		xx = MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.6)
		SetColor 255,0,0
		DrawString("Mouse Control",SCREENW/2-280,SCREENH/2-lsp*3,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Fire: "+mbut$[m_fire]+" Mouse Button",SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Bomb: "+mbut$[m_bomb]+" Mouse Button",SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2+100+1,SCREENH/2+lsp+1,m_sensitivity*200,24-2,1
		DrawString("Mouse Sensitivity:",SCREENW/2-280,SCREENH/2+lsp,4)
		SetColor 255,255,0
		rect SCREENW/2+100,SCREENH/2+lsp,202,24,0

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*2,4)
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 3
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 3: sel = 0
			MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-1)+20)

		if jdmy != 0: ignorejoy = True
		if jdmx != 0: ignorexjoy = True
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 7
			jb = jb + JoyDown(i,joyport)

		if (KeyDown(KEY_LEFT) or MouseDown(1)) and bombtime = 0: jdmx = -1;bombtime = 20
		if (KeyDown(KEY_RIGHT) or MouseDown(2)) and bombtime = 0: jdmx = 1;bombtime = 20
		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20
		if KeyHit(k_bomb) or KeyHit(KEY_ENTER): done = True
		if KeyHit(KEY_ESCAPE): done = True;sel = 4;bombtime = 20
		Select sel
			Case 0
				if jdmx != 0
					m_fire += 1
					if m_fire > 3: m_fire = 1

				done = False
			Case 1
				if jdmx != 0
					m_bomb += 1
					if m_bomb > 3: m_bomb = 1

				done = False
			Case 2
				if jdmx < 0
					m_sensitivity -=  0.05
					if m_sensitivity< 0: m_sensitivity= 0

				if jdmx > 0
					m_sensitivity +=  0.05
					if m_sensitivity> 1: m_sensitivity= 1

				done = False
			Case 3
				if jdmx != 0: done=True

		looper  += 8







def KeyboardControllerSettings(showgame:Int)
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 9
	Local s#,x:Int
	Local ignorejoy:Int
	Local key:Int = -10
	Local flash$
	Local tim:Int
	Local cnt:Int
	Local lsp:Int = 40
	Local xx:Int
	Local yy:Int
	if (SCREENH<600):
		lsp = 32

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*5+20)
	while not done:
		Cls
		xx = MouseX()
		yy = MouseY()
		tim = time()
		if showgame:
			DrawAllStatic(.6)
		SetColor 255,0,0
		DrawString("Keyboard Control",SCREENW/2-280,SCREENH/2-lsp*6,6)

		if key = -10:
			if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*4,SCREENW,5*4):
				sel = 0
		if sel == 0:
			SetColor 255,255,(cnt*8) % 255
		else:
			SetColor 0,200,0
		flash$ = keystring[k_move_left]
		if key == -1 and sel = 0 and looper % 30 < 15: flash = ""
		DrawString("Move Left : "+flash$,SCREENW/2-280,SCREENH/2-lsp*4,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*3,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_move_right];if key = -1 and sel = 1 and looper % 30 < 15: flash = ""
		DrawString("Move Right: "+flash$,SCREENW/2-280,SCREENH/2-lsp*3,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*2,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_move_up];if key = -1 and sel = 2 and looper % 30 < 15: flash = ""
		DrawString("Move Up   : "+flash$,SCREENW/2-280,SCREENH/2-lsp*2,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*1,SCREENW,5*4): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_move_down];if key = -1 and sel = 3 and looper % 30 < 15: flash = ""
		DrawString("Move Down : "+flash$,SCREENW/2-280,SCREENH/2-lsp*1,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*0,SCREENW,5*4): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_fire_left];if key = -1 and sel = 4 and looper % 30 < 15: flash = ""
		DrawString("Fire Left : "+flash$,SCREENW/2-280,SCREENH/2-lsp*0,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*1,SCREENW,5*4): sel = 5
		if sel = 5 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_fire_right];if key = -1 and sel = 5 and looper % 30 < 15: flash = ""
		DrawString("Fire Right: "+flash$,SCREENW/2-280,SCREENH/2+lsp*1,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*2,SCREENW,5*4): sel = 6
		if sel = 6 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_fire_up];if key = -1 and sel = 6 and looper % 30 < 15: flash = ""
		DrawString("Fire Up   : "+flash$,SCREENW/2-280,SCREENH/2+lsp*2,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*3,SCREENW,5*4): sel = 7
		if sel = 7 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_fire_down];if key = -1 and sel = 7 and looper % 30 < 15: flash = ""
		DrawString("Fire Down : "+flash$,SCREENW/2-280,SCREENH/2+lsp*3,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*4,SCREENW,5*4): sel = 8
		if sel = 8 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		flash$ = keystring[k_bomb];if key = -1 and sel = 8 and looper % 30 < 15: flash = ""
		DrawString("Bomb : "+flash$,SCREENW/2-280,SCREENH/2+lsp*4,4)

		if key = -10: if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*5,SCREENW,5*4): sel = 9
		if sel = 9 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*5,4)

		cnt += 1
		DrawTarget(SCREENW/2-280-20,yy,cnt,4)
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		if key = -10
			jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
			if abs(jdmy) < 0.6: jdmy = 0
			if jdmy = 0: ignorejoy = False
			if ignorejoy = True
				jdmy = 0

			if KeyHit(KEY_UP) or jdmy < 0
				sel -= 1
				if sel < 0: sel = 9
				MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-4)+20)

			if KeyHit(KEY_DOWN) or jdmy > 0
				sel += 1
				if sel > 9: sel = 0
				MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-4)+20)


			if jdmy != 0: ignorejoy = True
			if KeyHit(KEY_ENTER) or KeyHit(KEY_RIGHT) or KeyHit(KEY_LEFT) or MouseHit(1)
				if sel < 9
					key = -1
					FlushKeys()
				else:
					done = True



		if key = -1 # waiting for key press
			for Local kk:Int = 8 To 255
				if KeyDown(kk): FlushKeys();key=kk;Exit


		# key was entered
		if key > -1
			Select sel
				Case 0
					k_move_left = key
				Case 1
					k_move_right = key
				Case 2
					k_move_up = key
				Case 3
					k_move_down = key
				Case 4
					k_fire_left = key
				Case 5
					k_fire_right = key
				Case 6
					k_fire_up = key
				Case 7
					k_fire_down = key
				Case 8
					k_bomb = key

			key = -10

		looper  += 8
		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 7
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True







def JoypadControllerSettings(showgame:Int)
	Local xx:Int,yy:Int,cnt:Int
	Local done:Int = False
	Local jb:Int,i:Int
	Local looper:Int = 0
	Local sel:Int = 7
	Local s#,x:Int
	Local ignorejoy:Int, ignorexjoy:Int
	Local m$,f$
	Local tim:Int
	Local lsp:Int = 40

	if j_config = 0
		m$ = "D Pad"
		f$ = "4-Buttons"
	else:
		f$ = "D Pad"
		m$ = "4-Buttons"

	bombtime = 20
	FlushKeys()
	FlushMouse()
	MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*4+20)
	while not done
		Cls
		xx= MouseX()
		yy = MouseY()

		tim = time()
		if showgame: DrawAllStatic(.6)
		SetColor 255,0,0
		DrawString("Joypad Control",SCREENW/2-280,SCREENH/2-lsp*4,6)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp*2,SCREENW,5*4): sel = 0
		if sel = 0 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Move: "+m$+"  Fire: "+f$,SCREENW/2-280,SCREENH/2-lsp*2,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2-lsp,SCREENW,5*4): sel = 1
		if sel = 1 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Bomb: Button  ["+(j_pad_bomb+1)+"]",SCREENW/2-280,SCREENH/2-lsp,4)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2,SCREENW,5*4): sel = 2
		if sel = 2 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Option: Button  ["+(j_pad_option+1)+"]",SCREENW/2-280,SCREENH/2,4)

		if RectsOverlap(xx-8,yy-8,16,16,SCREENW/2+64,SCREENH/2+lsp*1,40,30): sel = 3
		if sel = 3 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2+64,SCREENH/2+lsp*1,40,30,0
		DrawString((j_pad_4+1),SCREENW/2+64+8,SCREENH/2+lsp*1+8,3)

		if RectsOverlap(xx-8,yy-8,16,16,SCREENW/2,SCREENH/2+lsp*2,40,30): sel = 4
		if sel = 4 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2,SCREENH/2+lsp*2,40,30,0
		DrawString((j_pad_1+1),SCREENW/2+8,SCREENH/2+lsp*2+8,3)

		if RectsOverlap(xx-8,yy-8,16,16,SCREENW/2+128,SCREENH/2+lsp*2,40,30): sel = 5
		if sel = 5 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2+128,SCREENH/2+lsp*2,40,30,0
		DrawString((j_pad_3+1),SCREENW/2+128+8,SCREENH/2+lsp*2+8,3)

		if RectsOverlap(xx-8,yy-8,16,16,SCREENW/2+64,SCREENH/2+lsp*3,40,30): sel = 6
		if sel = 6 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		rect SCREENW/2+64,SCREENH/2+lsp*3,40,30,0
		DrawString((j_pad_2+1),SCREENW/2+64+8,SCREENH/2+lsp*3+8,3)

		if RectsOverlap(xx-8,yy-8,16,16,0,SCREENH/2+lsp*4,SCREENW,5*4): sel = 7
		if sel = 7 SetColor 255,255,(cnt*8) % 255 else: SetColor 0,200,0
		DrawString("Done",SCREENW/2-280,SCREENH/2+lsp*4,4)
		DrawTarget(xx,yy,cnt,4)
		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim

		jdmy = GetJoyByAxis(joyport, axis_move_y, axis_move_y_inv, axis_move_y_sc, axis_move_y_center )
		if abs(jdmy) < 0.6: jdmy = 0
		if jdmy = 0: ignorejoy = False
		if ignorejoy = True
			jdmy = 0

		jdmx = GetJoyByAxis(joyport, axis_move_x, axis_move_x_inv, axis_move_x_sc, axis_move_x_center )
		if abs(jdmx) < 0.6: jdmx = 0
		if jdmx = 0: ignorexjoy = False
		if ignorexjoy = True
			jdmx = 0

		if jdmy != 0: ignorejoy = True
		if jdmx != 0: ignorexjoy = True
		if KeyHit(KEY_UP) or jdmy < 0
			sel -= 1
			if sel < 0: sel = 7
			Select sel
				Case 3
					MoveMouse(SCREENW/2+64-20,SCREENH/2+lsp*1+20)
				Case 4
					MoveMouse(SCREENW/2-20,SCREENH/2+lsp*2+20)
				Case 5
					MoveMouse(SCREENW/2+128-20,SCREENH/2+lsp*2+20)
				Case 6
					MoveMouse(SCREENW/2+64-20,SCREENH/2+lsp*3+20)
				Case 7
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-3)+20)
				Default
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-2)+20)


		if KeyHit(KEY_DOWN) or jdmy > 0
			sel += 1
			if sel > 7: sel = 0
			Select sel
				Case 3
					MoveMouse(SCREENW/2+64-20,SCREENH/2+lsp*1+20)
				Case 4
					MoveMouse(SCREENW/2-20,SCREENH/2+lsp*2+20)
				Case 5
					MoveMouse(SCREENW/2+128-20,SCREENH/2+lsp*2+20)
				Case 6
					MoveMouse(SCREENW/2+64-20,SCREENH/2+lsp*3+20)
				Case 7
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-3)+20)
				Default
					MoveMouse(SCREENW/2-280-20,SCREENH/2+lsp*(sel-2)+20)



		jb = 0
		bombtime = bombtime - 1
		if bombtime < 0: bombtime = 0
		for i = 0 To 15
			jb = jb + JoyDown(i,joyport)

		if jb > 0 and bombtime = 0 and looper > 15*8: done = True;bombtime = 20
		if KeyHit(KEY_ESCAPE): done = True;sel=7;bombtime = 20
		if KeyHit(KEY_LEFT) or MouseHit(1): jdmx = -1
		if KeyHit(KEY_RIGHT) or MouseHit(2): jdmx = 1
		if KeyHit(KEY_ENTER): jdmx = 1
		Select sel
			Case 0
				if jdmx != 0 j_config = 1-j_config
				done = False
				if j_config = 0
					m$ = "D Pad"
					f$ = "4-Buttons"
				else:
					f$ = "D Pad"
					m$ = "4-Buttons"

			Case 1
				if jdmx < 0
					j_pad_bomb -= 1
					if j_pad_bomb < 0: j_pad_bomb = 0
				elif jdmx > 0
					j_pad_bomb += 1
					if j_pad_bomb > 15: j_pad_bomb = 15

				for i = 0 To 15
					if JoyDown(i,joyport): j_pad_bomb = i

				done = False
			Case 2
				if jdmx < 0
					j_pad_option -= 1
					if j_pad_option < 0: j_pad_option = 0
				elif jdmx > 0
					j_pad_option += 1
					if j_pad_option > 15: j_pad_option = 15

				for i = 0 To 15
					if JoyDown(i,joyport): j_pad_option = i

				done = False
			Case 3
				if jdmx < 0:
					j_pad_4 -= 1
					if j_pad_4 < 0: j_pad_4 = 0
				elif jdmx > 0:
					j_pad_4 += 1
					if j_pad_4 > 15:
						j_pad_4 = 15

				for i = 0 To 15:
					if JoyDown(i,joyport):
						j_pad_4 = i

				done = False
			Case 4
				if jdmx < 0:
					j_pad_1 -= 1
					if j_pad_1 < 0: j_pad_1 = 0
				elif jdmx > 0:
					j_pad_1 += 1
					if j_pad_1 > 15:
						j_pad_1 = 15

				for i = 0 To 15:
					if JoyDown(i,joyport):
						j_pad_1 = i

				done = False
			Case 5
				if jdmx < 0
					j_pad_3 -= 1
					if j_pad_3 < 0: j_pad_3 = 0
				elif jdmx > 0
					j_pad_3 += 1
					if j_pad_3 > 15: j_pad_3 = 15

				for i = 0 To 15
					if JoyDown(i,joyport): j_pad_3 = i

				done = False
			Case 6
				if jdmx < 0:
					j_pad_2 -= 1
					if j_pad_2 < 0:
						j_pad_2 = 0
				elif jdmx > 0:
					j_pad_2 += 1
					if j_pad_2 > 15:
						j_pad_2 = 15

				for i = 0 To 15:
					if JoyDown(i,joyport):
						j_pad_2 = i

				done = False
			Case 7
				if jdmx != 0:
					done = True
				#exit

		looper += 8




def DualAnalogControllerSettings():

	Local done:Int = False
	Local tim:Int
	Local cnt:Int

	Setorigin (SCREENW-640)/2,(SCREENH-480)/2

	while not done:
		Cls
		tim = time()
		drawconfigstuff()

		mx = MouseX()
		my = MouseY()
		if mx>640:
			mx = 640
		if my>550:
			my = 550
		if assigning is False:
			done = CheckInput(joyport)
		else:
			AssignAllJoyAxis(joyport)
			if ax % 1 = 1:
				if GetJoyAxis(joyport,1) = -1:
					ax = ax + 1
			if ax = 8:
				assigning = False


		# map the Input values so the red dots can be drawn in position
		Local x1j# = GetJoyByAxis(joyport,j[joyport].x1id-1,j[joyport].x1invert,j[joyport].x1scale,j[joyport].x1center)
		Local y1j# = GetJoyByAxis(joyport,j[joyport].y1id-1,j[joyport].y1invert,j[joyport].y1scale,j[joyport].y1center)
		Local x2j# = GetJoyByAxis(joyport,j[joyport].x2id-1,j[joyport].x2invert,j[joyport].x2scale,j[joyport].x2center)
		Local y2j# = GetJoyByAxis(joyport,j[joyport].y2id-1,j[joyport].y2invert,j[joyport].y2scale,j[joyport].y2center)

		# dead band
		if abs(x1j) < j[joyport].x1dz: x1j = 0
		if abs(y1j) < j[joyport].y1dz: y1j = 0
		if abs(x2j) < j[joyport].x2dz: x2j = 0
		if abs(y2j) < j[joyport].y2dz: y2j = 0

		#scale to box size
		Local x1:Int = FitValueToRange#( x1j, -1, 1,  10, 110 )
		Local y1:Int = FitValueToRange#( y1j, -1, 1, 275, 375 )
		Local x2:Int = FitValueToRange#( x2j, -1, 1, 250, 350 )
		Local y2:Int = FitValueToRange#( y2j, -1, 1, 275, 375 )

		#draw the control dots
		SetColor 185,0,0
		DrawOval x1-5-j[joyport].x1center*50,y1-5-j[joyport].y1center*50,10,10
		DrawOval x2-5-j[joyport].x2center*50,y2-5-j[joyport].y2center*50,10,10

		#draw cursor
		DrawTarget(mx,my,cnt,4)

		if infotimer > 0
			DrawText info$,320,180
			infotimer -= 1

		cnt += 1
		Flip 1
		tim = time() - tim
		if tim < 20 and tim > 0
			Delay 20-tim



	Setorigin 0,0







def DrawConfigStuff():

	SetBlend MASKBLEND
	SetAlpha 1

	SetColor 255,255,255
	DrawText "Dual Stick Configuration",170,10

	SetColor 128,128,128
	Rect 10,32,600,130,0 # large text info box outline
	DrawText "Select controller port (0 for  single joypad)",15,35
	DrawText "others are only needed for multiple joypads.",15,35+1*12
	DrawText "Assign controls by clicking AXIS WIZARD or individually",15,35+2*12
	DrawText "cycle through available controls by left clicking on the axis box.",15,35+3*12
	DrawText "Right click on a box to toggle invert On or Off.",15,35+4*12
	DrawText "Blue box is normal, orange box indicates an inverted axis.",15,35+5*12
	DrawText "Click on Stick 1/2 boxes and use cursor keys to adjust centering and",15,35+6*12
	DrawText "Dead Zone.  Make sure the red dot is in the green square when at rest.",15,35+7*12
	DrawText "if it drifts, press SHIFT+Cursor Keys to adjust Dead Zone.",15,35+8*12


	SetColor 35,65,115
	Select joyport # draw current port selected
		Case 0
			Rect 100+10,130+45,45,25,1
		Case 1
			Rect 100+60,130+45,45,25,1
		Case 2
			Rect 100+110,130+45,45,25,1
		Case 3
			Rect 100+160,130+45,45,25,1


	SetColor 0,0,100
	Rect 100+10,130+45,45,25,0 # draw ports (outlines)
	Rect 100+60,130+45,45,25,0
	Rect 100+110,130+45,45,25,0
	Rect 100+160,130+45,45,25,0

	SetColor 255,255,255
	DrawText "Controller:",10,130+50
	DrawText "0",100+27,130+53
	DrawText "1",100+77,130+53
	DrawText "2",100+127,130+53
	DrawText "3",100+177,130+53

	if assigning is True:
		SetColor 100,100,100
		Rect 10,225,135,25,1

	SetColor 255,255,255
	Rect 10,225,135,25,0
	DrawText "AXIS WIZARD",25,230

	if assigningoption = True
		SetColor 100,100,100
		Rect 180,225,100,25,1

	SetColor 255,255,255
	Rect 180,225,100,25,0
	DrawText "OPTION = "+(j[joyport].optionbutton+1),190,230

	if assigningbomb = True
		SetColor 100,100,100
		Rect 320,225,100,25,1

	SetColor 255,255,255
	Rect 320,225,100,25,0
	DrawText "BOMB = "+(j[joyport].bombbutton+1),330,230

	#draw boxes for axis controls
	SetColor 50,65,220
	if j[joyport].x1invert =-1: SetColor 255,128,0
	Rect 10,395,175,14,1

	SetColor 50,65,220
	if j[joyport].y1invert =-1: SetColor 255,128,0
	Rect 10,415,175,14,1

	SetColor 50,65,220
	if j[joyport].x2invert =-1: SetColor 255,128,0
	Rect 250,395,175,14,1

	SetColor 50,65,220
	if j[joyport].y2invert =-1: SetColor 255,128,0
	Rect 250,415,175,14,1

	SetColor 255,255,255
	DrawText "Stick 1",10,380
	DrawText "Stick 2",250,380
	DrawText "X axis: " + joy_label$[j[joyport].x1id],20,396
	DrawText "X axis: " + joy_label$[j[joyport].x2id],260,396
	DrawText "Y axis: " + joy_label$[j[joyport].y1id],20,416
	DrawText "Y axis: " + joy_label$[j[joyport].y2id],260,416

	if deadbandadjust = 1
		SetColor 100,100,100
		Rect 10+1,275+1, 100-2,100-2,1
	elif deadbandadjust = 2
		SetColor 100,100,100
		Rect 250+1,275+1, 100-2,100-2,1


	SetColor 0,255,0
	rect 10+50-8,275+50-8,16,16
	rect 250+50-8,275+50-8,16,16

	SetColor 255,255,255
	Rect 10,275, 100,100,0 #draw outline boxes for controllers
	Rect 250,275, 100,100,0

	DrawText "X Scaling Factor",10,440
	DrawText "X Scaling Factor",250,440
	DrawText "Y Scaling Factor",10,480
	DrawText "Y Scaling Factor",250,480

	SetColor 35,65,115
	Select j[joyport].x1scale
		Case 1
			Rect 10,455,45,20,1
		Case 128
			Rect 60,455,45,20,1
		Case 255
			Rect 110,455,45,20,1

	Select j[joyport].y1scale
		Case 1
			Rect 10,495,45,20,1
		Case 128
			Rect 60,495,45,20,1
		Case 255
			Rect 110,495,45,20,1

	Select j[joyport].x2scale
		Case 1
			Rect 240+10,455,45,20,1
		Case 128
			Rect 240+60,455,45,20,1
		Case 255
			Rect 240+110,455,45,20,1

	Select j[joyport].y2scale
		Case 1
			Rect 240+10,495,45,20,1
		Case 128
			Rect 240+60,495,45,20,1
		Case 255
			Rect 240+110,495,45,20,1


	SetColor 255,255,255
	DrawText "1",27,460
	DrawText "180",70,460
	DrawText "255",120,460

	DrawText "1",240+27,460
	DrawText "180",240+70,460
	DrawText "255",240+120,460

	DrawText "1",27,500
	DrawText "180",70,500
	DrawText "255",120,500

	DrawText "1",240+27,500
	DrawText "180",240+70,500
	DrawText "255",240+120,500

	SetColor 0,0,100
	Rect 10,455,45,20,0
	Rect 60,455,45,20,0
	Rect 110,455,45,20,0

	Rect 240+10,455,45,20,0
	Rect 240+60,455,45,20,0
	Rect 240+110,455,45,20,0

	Rect 10,495,45,20,0
	Rect 60,495,45,20,0
	Rect 110,495,45,20,0

	Rect 240+10,495,45,20,0
	Rect 240+60,495,45,20,0
	Rect 240+110,495,45,20,0

	SetColor 255,32,32
	DrawText "DZ 1",120,270
	DrawText "DZ 2",360,270
	DrawText "C 1",120,330
	DrawText "C 2",360,330
	SetColor 32,32,240
	DrawText "X: "+j[joyport].x1dz,120,290
	DrawText "Y: "+j[joyport].y1dz,120,305
	DrawText "X: "+j[joyport].x2dz,360,290
	DrawText "Y: "+j[joyport].y2dz,360,305
	DrawText "X: "+j[joyport].x1center,120,350
	DrawText "Y: "+j[joyport].y1center,120,365
	DrawText "X: "+j[joyport].x2center,360,350
	DrawText "Y: "+j[joyport].y2center,360,365

	SetColor 64,64,64
	Rect 490,275+40,110,20
	Rect 490,300+40,110,20
	Rect 490,325+40,110,20
	Rect 490,350+40,110,20
	SetColor 255,255,255
	DrawText "(D)ebug",493,277+40
	DrawText "(S)ave Config",493,302+40
	DrawText "(L)oad Config",493,327+40
	DrawText "(E)xit",493,352+40

	if debug is True:
		SetColor 16,16,16
		Rect 0,25,640,217+80,1
		SetColor 48,48,48
		Rect 40,30,300,200+80,1
		SetColor 64,64,64 # draw grey boxes
		for Local loop:Int = 50 To 190+80 Step 20
			Rect 180,loop,150,15

		Rect 40,30,300,200+60,0
		Rect 39,29,302,202+60,0

		SetColor 128,128,128 # draw boxes showing movement of axis
		Rect 180,50,FitValueToRange#( JoyX(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,70,FitValueToRange#( JoyY(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,90,FitValueToRange#( JoyZ(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,110,FitValueToRange#( JoyR(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,130,FitValueToRange#( JoyU(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,150,FitValueToRange#( JoyV(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,170,FitValueToRange#( JoyPitch(joyport), -180, 180, 0, 150 ),15,1
		Rect 180,190,FitValueToRange#( JoyRoll(joyport), -180, 180, 0, 150 ),15,1
		Rect 180,210,FitValueToRange#( JoyYaw(joyport), -180, 180, 0, 150 ),15,1
		Rect 180,230,FitValueToRange#( JoyHat(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,250,FitValueToRange#( JoyWheel(joyport), -1, 1, 0, 150 ),15,1
		Rect 180,270,FitValueToRange#( JoyWhat(joyport,12), -1, 1, 0, 150 ),15,1
		Rect 180,290,FitValueToRange#( JoyWhat(joyport,13), -1, 1, 0, 150 ),15,1

		SetColor 160,160,160 # show values of axis
		DrawText "1.  JoyX()      : " + JoyX(joyport) ,50,50
		DrawText "2.  JoyY()      : " + JoyY(joyport),50,70
		DrawText "3.  JoyZ()      : " + JoyZ(joyport),50,90
		DrawText "4.  JoyR()      : " + JoyR(joyport),50,110
		DrawText "5.  JoyU()      : " + JoyU(joyport),50,130
		DrawText "6.  JoyV()      : " + JoyV(joyport),50,150
		DrawText "7.  JoyPitch()  : " + JoyPitch(joyport),50,170
		DrawText "8.  JoyRoll()   : " + JoyRoll(joyport),50,190
		DrawText "9.  JoyYaw()    : " + JoyYaw(joyport),50,210
		DrawText "10. JoyHat()    : " + JoyHat(joyport),50,230
		DrawText "11. JoyWheel()  : " + JoyWheel(joyport),50,250
		DrawText "12. JoyAxis12()  : " + JoyWhat(joyport,12),50,270
		DrawText "13. JoyAxis13()  : " + JoyWhat(joyport,13),50,290





def CheckInput(port: int) -> int:
	SetColor 255,0,0
	if RectsOverlap  (mx-2,my-2,4,4,10,395,175,14) # joy x 1
		Rect 9,394,177,16,0 # draw a highlight rectangle
		if MouseHit(1): j[port].x1id += 1
		if MouseHit(2): j[port].x1invert = - j[port].x1invert
		if j[port].x1id > 15: j[port].x1id = 0
		if j[port].x1id < 0: j[port].x1id = 15


	if RectsOverlap  (mx-2,my-2,4,4,10,415,175,14) # joy y 1
		Rect 9,414,177,16,0	# draw a highlight rectangle
		if MouseHit(1): j[port].y1id += 1
		if MouseHit(2): j[port].y1invert = - j[port].y1invert
		if j[port].y1id > 15: j[port].y1id = 0
		if j[port].y1id < 0: j[port].y1id = 15


	if RectsOverlap  (mx-2,my-2,4,4,250,395,175,14) # joy x 2
		Rect 249,394,177,16,0	# draw a highlight rectangle
		if MouseHit(1): j[port].x2id += 1
		if MouseHit(2): j[port].x2invert = - j[port].x2invert
		if j[port].x2id > 15: j[port].x2id = 0
		if j[port].x2id < 0: j[port].x2id = 15


	if RectsOverlap  (mx-2,my-2,4,4,250,415,175,14) # joy y 2
		Rect 249,414,177,16,0	# draw a highlight rectangle
		if MouseHit(1): j[port].y2id += 1
		if MouseHit(2): j[port].y2invert = - j[port].y2invert
		if j[port].y2id > 15: j[port].y2id = 0
		if j[port].y2id < 0: j[port].y2id = 15


	if RectsOverlap  (mx-2,my-2,4,4,10,275,100,100)
		Rect 10,275,100,100,0
		if MouseHit(1)
			if deadbandadjust = 1
				deadbandadjust = 0
			else:
				deadbandadjust = 1




	if RectsOverlap  (mx-2,my-2,4,4,250,275,100,100)
		Rect 250,275,100,100,0
		if MouseHit(1)
			if deadbandadjust = 2
				deadbandadjust = 0
			else:
				deadbandadjust = 2




	#joy port selection
	if RectsOverlap  (mx-2,my-2,4,4,100+10,130+45,45,25)
		Rect 100+10,130+45,45,25,0
		if MouseHit(1): joyport = 0


	if RectsOverlap  (mx-2,my-2,4,4,100+60,130+45,45,25)
		Rect 100+60,130+45,45,25,0
		if MouseHit(1): joyport = 1


	if RectsOverlap  (mx-2,my-2,4,4,100+110,130+45,45,25)
		Rect 100+110,130+45,45,25,0
		if MouseHit(1): joyport = 2


	if RectsOverlap  (mx-2,my-2,4,4,100+160,130+45,45,25)
		Rect 100+160,130+45,45,25,0
		if MouseHit(1): joyport = 3


	#scaling
	if RectsOverlap  (mx-2,my-2,4,4,10,455,45,20)
		Rect 10,455,45,20,0
		if MouseHit(1): j[joyport].x1scale = 1

	if RectsOverlap  (mx-2,my-2,4,4,60,455,45,20)
		Rect 60,455,45,20,0
		if MouseHit(1): j[joyport].x1scale = 180

	if RectsOverlap  (mx-2,my-2,4,4,110,455,45,20)
		Rect 110,455,45,20,0
		if MouseHit(1): j[joyport].x1scale = 255

	if RectsOverlap  (mx-2,my-2,4,4,10,495,45,20)
		Rect 10,495,45,20,0
		if MouseHit(1): j[joyport].y1scale = 1

	if RectsOverlap  (mx-2,my-2,4,4,60,495,45,20)
		Rect 60,495,45,20,0
		if MouseHit(1): j[joyport].y1scale = 180

	if RectsOverlap  (mx-2,my-2,4,4,110,495,45,20)
		Rect 110,495,45,20,0
		if MouseHit(1): j[joyport].y1scale = 255


	if RectsOverlap  (mx-2,my-2,4,4,240+10,455,45,20)
		Rect 240+10,455,45,20,0
		if MouseHit(1): j[joyport].x2scale = 1

	if RectsOverlap  (mx-2,my-2,4,4,240+60,455,45,20)
		Rect 240+60,455,45,20,0
		if MouseHit(1): j[joyport].x2scale = 180

	if RectsOverlap  (mx-2,my-2,4,4,240+110,455,45,20)
		Rect 240+110,455,45,20,0
		if MouseHit(1): j[joyport].x2scale = 255

	if RectsOverlap  (mx-2,my-2,4,4,240+10,495,45,20)
		Rect 240+10,495,45,20,0
		if MouseHit(1): j[joyport].y2scale = 1

	if RectsOverlap  (mx-2,my-2,4,4,240+60,495,45,20)
		Rect 240+60,495,45,20,0
		if MouseHit(1): j[joyport].y2scale = 180

	if RectsOverlap  (mx-2,my-2,4,4,240+110,495,45,20)
		Rect 240+110,495,45,20,0
		if MouseHit(1): j[joyport].y2scale = 255


	if RectsOverlap  (mx-2,my-2,4,4,10,225,135,25) # assign all axis button
		Rect 10,225,135,25,0
		if MouseHit(1): assigning = True;ax = 0;assigningoption = False;assigningbomb = False


	if RectsOverlap  (mx-2,my-2,4,4,180,225,100,25) # option button
		Rect 180,225,100,25,0
		if MouseHit(1): assigningoption = True;assigningbomb = False


	if RectsOverlap  (mx-2,my-2,4,4,320,225,100,25) # bomb button
		Rect 320,225,100,25,0
		if MouseHit(1): assigningbomb = True;assigningoption = False


	if assigningoption
		for Local i: int = 0 To 15
			if JoyDown(i,joyport): j[joyport].optionbutton = i

		if KeyHit(KEY_ENTER)
			j[joyport].optionbutton +=  1
			if j[joyport].optionbutton > 15: j[joyport].optionbutton = 0



	if assigningbomb
		for Local i: int = 0 To 15
			if JoyDown(i,joyport): j[joyport].bombbutton = i

		if KeyHit(KEY_ENTER)
			j[joyport].bombbutton +=  1
			if j[joyport].bombbutton> 15: j[joyport].bombbutton = 0



	if KeyHit(KEY_1):
		joyport = 0 #1 key
	if KeyHit(KEY_2):
		joyport = 1 #2 key
	if KeyHit(KEY_3):
		joyport = 2 #3 key
	if KeyHit(KEY_4):
		joyport = 3 #4 key

	if RectsOverlap  (mx-2,my-2,4,4,490,275+40,110,20) # debug toggle
		Rect 490,275+40,110,20,0
		if MouseHit(1):
			# debug = 1 - Debug
			debug = not debug


	if RectsOverlap  (mx-2,my-2,4,4,490,300+40,110,20) # save button
		Rect 490,300+40,110,20,0
		if MouseHit(1):
			SaveConfig()


	if RectsOverlap  (mx-2,my-2,4,4,490,325+40,110,20) #load button
		Rect 490,325+40,110,20,0
		if MouseHit(1):
			LoadConfig()


	if KeyHit(KEY_D):
		# debug = 1 - Debug # tab key,... turns on debug
		debug = not debug

	if KeyHit(KEY_S): # S key
		SaveConfig()


	if KeyHit(KEY_L): # L key
		LoadConfig()


	if KeyHit(KEY_E): # E for Exit
		return True


	if KeyDown(KEY_LSHIFT) or KeyDown(KEY_RSHIFT):
		if deadbandadjust > 0:
			if deadbandadjust = 1:
				if KeyDown(KEY_UP):
					j[joyport].y1dz -= .01
					if j[joyport].y1dz < 0:
						j[joyport].y1dz = 0

				if KeyDown(KEY_DOWN):
					j[joyport].y1dz += .01
					if j[joyport].y1dz > .5:
						j[joyport].y1dz = .5

				if KeyDown(KEY_LEFT):
					j[joyport].x1dz -= .01
					if j[joyport].x1dz < 0:
						j[joyport].x1dz = 0

				if KeyDown(KEY_RIGHT):
					j[joyport].x1dz += .01
					if j[joyport].x1dz > .5:
						j[joyport].x1dz = .5

			else:
				if KeyDown(KEY_UP):
					j[joyport].y2dz -= .01
					if j[joyport].y2dz < -.9:
						j[joyport].y2dz= -.9

				if KeyDown(KEY_DOWN):
					j[joyport].y2dz += .01
					if j[joyport].y2dz > .9:
						j[joyport].y2dz= .9

				if KeyDown(KEY_LEFT):
					j[joyport].x2dz -= .01
					if j[joyport].x2dz < -.9:
						j[joyport].x2dz= -.9

				if KeyDown(KEY_RIGHT):
					j[joyport].x2dz += .01
					if j[joyport].x2dz > .9:
						j[joyport].x2dz= .9

	else:
		if deadbandadjust > 0:
			if deadbandadjust == 1:
				if KeyDown(KEY_UP):
					j[joyport].y1center -= .01
					if j[joyport].y1center < -.9:
						j[joyport].y1center = -.9

				if KeyDown(KEY_DOWN):
					j[joyport].y1center += .01
					if j[joyport].y1center > .9:
						j[joyport].y1center = .9

				if KeyDown(KEY_LEFT):
					j[joyport].x1center -= .01
					if j[joyport].x1center < -.9:
						j[joyport].x1center = -.9

				if KeyDown(KEY_RIGHT):
					j[joyport].x1center += .01
					if j[joyport].x1center > .9:
						j[joyport].x1center = .9

			else:
				if KeyDown(KEY_UP):
					j[joyport].y2center -= .01
					if j[joyport].y2center < -.9:
						j[joyport].y2center= -.9

				if KeyDown(KEY_DOWN):
					j[joyport].y2center += .01
					if j[joyport].y2center > .9:
						j[joyport].y2center= .9

				if KeyDown(KEY_LEFT):
					j[joyport].x2center -= .01
					if j[joyport].x2center < -.9:
						j[joyport].x2center= -.9

				if KeyDown(KEY_RIGHT):
					j[joyport].x2center += .01
					if j[joyport].x2center > .9:
						j[joyport].x2center= .9

	if RectsOverlap(mx-2,my-2,4,4,490,350+40,110,20): # quit button
		Rect 490,350+40,110,20,0
		if MouseHit(1):
			return True

	return False




def GetJoyAxis(port: int, sc: float) -> int:
	# on some joysticks, when an axis is not present the value is the Max
	# so we needed to get around that with the double check
	Local count: int = 0
	while count < 30:
		if abs(JoyX(port)) > .5*sc and abs(JoyX(port)) < .9*sc:
			return 1
		if abs(JoyY(port)) > .5*sc and abs(JoyY(port)) < .9*sc:
			return 2
		if abs(JoyZ(port)) > .5*sc and abs(JoyZ(port)) < .9*sc:
			return 3
		if abs(JoyR(port)) > .5*sc and abs(JoyR(port)) < .9*sc:
			return 4
		if abs(JoyU(port)) > .5*sc and abs(JoyU(port)) < .9*sc:
			return 5
		if abs(JoyV(port)) > .5*sc and abs(JoyV(port)) < .9*sc:
			return 6
		if abs(JoyYaw(port)) > .5*sc and abs(JoyYaw(port)) < .9*sc:
			return 7
		if abs(JoyPitch(port)) > .5*sc and abs(JoyPitch(port)) < .9*sc:
			return 8
		if abs(JoyRoll(port)) > .5*sc and abs(JoyRoll(port)) < .9*sc:
			return 9
		if abs(JoyHat(port)) > .5*sc and abs(JoyHat(port)) < .9*sc:
			return 10
		if abs(JoyWheel(port)) > .5*sc and abs(JoyWheel(port)) < .9*sc:
			return 11
		if abs(JoyWhat(port,12)) > .5*sc and abs(JoyWhat(port,12)) < .9*sc:
			return 12
		if abs(JoyWhat(port,13)) > .5*sc and abs(JoyWhat(port,13)) < .9*sc:
			return 13
		if abs(JoyWhat(port,14)) > .5*sc and abs(JoyWhat(port,14)) < .9*sc:
			return 14
		if abs(JoyWhat(port,15)) > .5*sc and abs(JoyWhat(port,15)) < .9*sc:
			return 15

		if KeyHit(KEY_ESCAPE):
			return 0

		count += 1
		Delay 2

	return -1




def AssignAllJoyAxis(port: int)

	Local jax: int

	SetColor 0,255,0
	Select ax/2
		Case 0
			DrawText "move stick 1 left or right (Escape to Cancel)",180,210
			jax = getjoyaxis(port,j[port].x1scale)
			if jax >= 0:
			 	if jax > 0:
					j[port].x1id = jax
				ax += 1
				infotimer = 30*4
				info$ = "Stick 1 X axis assigned to " + joy_label[j[port].x1id]

		Case 1
			DrawText "move stick 1 up or down (Escape to Cancel)",180,210
			jax = getjoyaxis(port,j[port].y1scale)
			if jax >= 0:
			 	if jax > 0:
					j[port].y1id = jax
				ax += 1
				infotimer = 30*4
				info$ = "Stick 1 Y axis assigned to " + joy_label[j[port].y1id]

		Case 2
			DrawText "move stick 2 left or right (Escape to Cancel)",180,210
			jax = getjoyaxis(port,j[port].x2scale)
			if jax >= 0:
			 	if jax > 0:
					j[port].x2id = jax
				ax += 1
				infotimer = 30*4
				info$ = "Stick 2 X axis assigned to " + joy_label[j[port].x2id]

		Case 3
			DrawText "move stick 2 up or down (Escape to Cancel)",180,210
			jax = getjoyaxis(port,j[port].y2scale)
			if jax >= 0:
			 	if jax > 0:
					j[port].y2id = jax
				ax += 1
				infotimer = 60*4
				info$ = "Stick 2 Y axis assigned to " + joy_label[j[port].y2id]




def JoyWhat( port: int=0, axis: int ) -> float:
	SampleJoy port
	return joy_axis[port*16+axis]


def GetJoyByAxis( port: int, axis: int, invert: int=1, sc#, db# ) -> float:
	Local joy#

	Select axis
		Case 0
			joy=JoyX(port)/sc*invert - db
		Case 1
			joy=JoyY(port)/sc*invert - db
		Case 2
			joy=JoyZ(port)/sc*invert - db
		Case 3
			joy=JoyR(port)/sc*invert - db
		Case 4
			joy=JoyU(port)/sc*invert - db
		Case 5
			joy=JoyV(port)/sc*invert - db
		Case 6
			joy=JoyYaw(port)/sc*invert - db
		Case 7
			joy=JoyPitch(port)/sc*invert - db
		Case 8
			joy=JoyRoll(port)/sc*invert - db
		Case 9
			joy=JoyHat(port)/sc*invert - db
		Case 10
			joy=JoyWheel(port)/sc*invert - db
		Case 11
			joy=JoyWhat(port,12)/sc*invert - db
		Case 12
			joy=JoyWhat(port,13)/sc*invert - db
		Case 13
			joy=JoyWhat(port,14)/sc*invert - db
		Case 14
			joy=JoyWhat(port,15)/sc*invert - db

	return joy  #/sc * invert)



def SetController():
	axis_move_x = j[joyport].x1id-1
	axis_move_y = j[joyport].y1id-1
	axis_fire_x = j[joyport].x2id-1
	axis_fire_y = j[joyport].y2id-1
	axis_move_x_inv = j[joyport].x1invert
	axis_move_y_inv = j[joyport].y1invert
	axis_fire_x_inv = j[joyport].x2invert
	axis_fire_y_inv = j[joyport].y2invert
	axis_move_x_sc = j[joyport].x1scale
	axis_move_y_sc = j[joyport].y1scale
	axis_fire_x_sc = j[joyport].x2scale
	axis_fire_y_sc = j[joyport].y2scale
	axis_move_x_center = j[joyport].x1center
	axis_move_y_center = j[joyport].y1center
	axis_fire_x_center = j[joyport].x2center
	axis_fire_y_center = j[joyport].y2center
	axis_move_x_dz = j[joyport].x1dz
	axis_move_y_dz = j[joyport].y1dz
	axis_fire_x_dz = j[joyport].x2dz
	axis_fire_y_dz = j[joyport].y2dz
	j_d_bomb = j[joyport].bombbutton
	j_d_option = j[joyport].optionbutton
