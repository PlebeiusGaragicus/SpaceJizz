import pygame

def setup():
	pygame.init()
	screen: pygame.display = pygame.display.set_mode((640, 480))

	# JoyCount()
	# LoadConfig() # see control.bmx for more global settings
	# LoadColours()
	GetGfxModes()
	FindSetting()
	SetController()
	SetupKeyTable()
	SetUp()
	LoadSounds()

	# SeedRnd(time())
	seed( time() )

	score.LoadScores()
	HideMouse()
	Main()
	ShowMouse()
	SaveConfig()
	SaveColours() # only needed once
	score.SaveScores()





def main():
	setup()

	tim: int
	tim2: int
	tim3: int
	tim4: int

	looper: int
	f: int
	done: bool = False

	part.CreateAll()

	FlushKeys()

	while not done:
		while playgame is False and done is False:
			StartMusic(0)
			if playgame is False and done is False:
				done = ShowTitle()
			if playgame is False and done is False:
				done = ShowScores()
			if playgame is False and done is False:
				done = ShowFriends()
			if playgame is False and done is False:
				done = ShowEnemies()

		if playgame and not done:
			if not cheat:
				valid = True
				nokillme = False

			StopMusic()
			remove_all(True)
			ResetGame()
			dying = True
			done = GetReady()
			dying = False
			Cls

			while gameover is not True or playgame is True:
				tim = time()
				Spawn(gcount)
				UpdatePlayer()
				UpdateAll()
				tim2: int = time()-tim
				DrawAll()
				tim3: int = time()-tim

				if gameover:
					StopMusic()
					done = DoGameOver()
					playgame = False

				if cheat:
					DrawString("Update ms: "+tim2, 10,30,3)
					DrawString("Draw ms: " + (tim3 - tim2) , 10 , 50 , 3)
					DrawString("Last Frame ms: " + (tim4) , 10 , 70 , 3)
					Flip 1
					if KeyDown(KEY_P):
						pause: bool = True
						while pause:
							sleep(100)
							if KeyHit(KEY_O):
								pause = False
				else:
					Flip 1

				gcount += 1

				if KeyHit(KEY_ESCAPE) or (JoyDown(j_pad_option,joyport) and CONTROLTYPE == 3 and bombtime == 0) or (JoyDown(j_d_option,joyport) and CONTROLTYPE == 0 and bombtime == 0)
					ret: int = Options(True)
					if ret > 0:
						done = True
						gameover = True
						if ret = 2:
							StopMusic()
							playgame = False
							done = False

					bombtime = 20

				tim4: int = time() - tim
				if tim4 < 20 and tim4 > 0:
					sleep(20-tim4)

				Cls


			remove_all(True) # in case some sounds still playing and we quit
			if done == False:
				gxoff = 0
				gyoff = 0
				if pscore > lowesthiscore:
					StartMusic(2)
					f = score.GetHighScore()
					done = ShowScores(f)
					pscore = 0
					StopMusic()
				else:
					if pscore > 0:
						StartMusic(0);
						done = ShowScores(-20)





if __name__ == '__main__':
    main()
