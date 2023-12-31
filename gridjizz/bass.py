BASSTRUE = 1
BASSFALSE = 0
BASS_OK = 0
BASS_ERROR_MEM = 1
BASS_ERROR_FILEOPEN = 2
BASS_ERROR_DRIVER = 3
BASS_ERROR_BUFLOST = 4
BASS_ERROR_HANDLE = 5
BASS_ERROR_FORMAT = 6
BASS_ERROR_POSITION = 7
BASS_ERROR_INIT = 8
BASS_ERROR_START = 9
BASS_ERROR_INITCD = 10
BASS_ERROR_CDINIT = 11
BASS_ERROR_NOCD = 12
BASS_ERROR_CDTRACK = 13
BASS_ERROR_ALREADY = 14
BASS_ERROR_CDVOL = 15
BASS_ERROR_NOPAUSE = 16
BASS_ERROR_NOTAUDIO = 17
BASS_ERROR_NOCHAN = 18
BASS_ERROR_ILLTYPE = 19
BASS_ERROR_ILLPARAM = 20
BASS_ERROR_NO3D = 21
BASS_ERROR_NOEAX = 22
BASS_ERROR_DEVICE = 23
BASS_ERROR_NOPLAY = 24
BASS_ERROR_FREQ = 25
BASS_ERROR_NOTFILE = 27
BASS_ERROR_NOHW = 29
BASS_ERROR_EMPTY = 31
BASS_ERROR_NONET = 32
BASS_ERROR_CREATE = 33
BASS_ERROR_NOFX = 34
BASS_ERROR_PLAYING = 35
BASS_ERROR_NOTAVAIL = 37
BASS_ERROR_DECODE = 38
BASS_ERROR_DX = 39
BASS_ERROR_TIMEOUT = 40
BASS_ERROR_FILEFORM = 41
BASS_ERROR_SPEAKER = 42
BASS_ERROR_UNKNOWN = -1
BASS_DEVICE_8BITS = 1
BASS_DEVICE_MONO = 2
BASS_DEVICE_3D = 4
BASS_DEVICE_LEAVEVOL = 32
BASS_DEVICE_NOTHREAD = 128
BASS_DEVICE_LATENCY = 256
BASS_DEVICE_VOL1000 = 512
BASS_DEVICE_FLOATDSP = 1024
BASS_DEVICE_SPEAKERS = 2048
DSCAPS_CONTINUOUSRATE = 16
DSCAPS_EMULDRIVER = 32
DSCAPS_CERTIFIED = 64
DSCAPS_SECONDARYMONO = 256
DSCAPS_SECONDARYSTEREO = 512
DSCAPS_SECONDARY8BIT = 1024
DSCAPS_SECONDARY16BIT = 2048
DSCCAPS_EMULDRIVER = DSCAPS_EMULDRIVER
DSCCAPS_CERTIFIED = DSCAPS_CERTIFIED
WAVE_FORMAT_1M08 = $1
WAVE_FORMAT_1S08 = $2
WAVE_FORMAT_1M16 = $4
WAVE_FORMAT_1S16 = $8
WAVE_FORMAT_2M08 = $10
WAVE_FORMAT_2S08 = $20
WAVE_FORMAT_2M16 = $40
WAVE_FORMAT_2S16 = $80
WAVE_FORMAT_4M08 = $100
WAVE_FORMAT_4S08 = $200
WAVE_FORMAT_4M16 = $400
WAVE_FORMAT_4S16 = $800
BASS_MUSIC_RAMP = 1
BASS_MUSIC_RAMPS = 2
BASS_MUSIC_LOOP = 4
BASS_MUSIC_FT2MOD = 16
BASS_MUSIC_PT1MOD = 32
BASS_MUSIC_MONO = 64
BASS_MUSIC_3D = 128
BASS_MUSIC_POSRESET = 256
BASS_MUSIC_SURROUND = 512
BASS_MUSIC_SURROUND2 = 1024
BASS_MUSIC_STOPBACK = 2048
BASS_MUSIC_FX = 4096
BASS_MUSIC_CALCLEN = 8192
BASS_MUSIC_NONINTER = 16384
BASS_MUSIC_FLOAT = $10000
BASS_MUSIC_DECODE = $200000
BASS_MUSIC_NOSAMPLE = $400000
BASS_SAMPLE_8BITS = 1
BASS_SAMPLE_FLOAT = 256
BASS_SAMPLE_MONO = 2
BASS_SAMPLE_LOOP = 4
BASS_SAMPLE_3D = 8
BASS_SAMPLE_SOFTWARE = 16
BASS_SAMPLE_MUTEMAX = 32
BASS_SAMPLE_VAM = 64
BASS_SAMPLE_FX = 128
BASS_SAMPLE_OVER_VOL = 65536
BASS_SAMPLE_OVER_POS = 131072
BASS_SAMPLE_OVER_DIST = 196608
BASS_MP3_SETPOS = 131072
BASS_STREAM_AUTOFREE = 262144
BASS_STREAM_RESTRATE = 524288
BASS_STREAM_BLOCK = 1048576
BASS_STREAM_DECODE = $200000
BASS_STREAM_META = $400000
BASS_STREAM_FILEPROC = $800000
BASS_SPEAKER_FRONT = $1000000
BASS_SPEAKER_REAR = $2000000
BASS_SPEAKER_CENLFE = $3000000
BASS_SPEAKER_REAR2 = $4000000
BASS_SPEAKER_LEFT = $10000000
BASS_SPEAKER_RIGHT = $20000000
BASS_SPEAKER_FRONTLEFT = BASS_SPEAKER_FRONT | BASS_SPEAKER_LEFT
BASS_SPEAKER_FRONTRIGHT = BASS_SPEAKER_FRONT | BASS_SPEAKER_RIGHT
BASS_SPEAKER_REARLEFT = BASS_SPEAKER_REAR | BASS_SPEAKER_LEFT
BASS_SPEAKER_REARRIGHT = BASS_SPEAKER_REAR | BASS_SPEAKER_RIGHT
BASS_SPEAKER_CENTER = BASS_SPEAKER_CENLFE | BASS_SPEAKER_LEFT
BASS_SPEAKER_LFE = BASS_SPEAKER_CENLFE | BASS_SPEAKER_RIGHT
BASS_SPEAKER_REAR2LEFT = BASS_SPEAKER_REAR2 | BASS_SPEAKER_LEFT
BASS_SPEAKER_REAR2RIGHT = BASS_SPEAKER_REAR2 | BASS_SPEAKER_RIGHT
BASS_TAG_ID3 = 0
BASS_TAG_ID3V2 = 1
BASS_TAG_OGG = 2
BASS_TAG_HTTP = 3
BASS_TAG_ICY = 4
BASS_TAG_META = 5
BASS_3DMODE_NORMAL = 0
BASS_3DMODE_RELATIVE = 1
BASS_3DMODE_OFF = 2
EAX_ENVIRONMENT_GENERIC = 0
EAX_ENVIRONMENT_PADDEDCELL = 1
EAX_ENVIRONMENT_ROOM = 2
EAX_ENVIRONMENT_BATHROOM = 3
EAX_ENVIRONMENT_LIVINGROOM = 4
EAX_ENVIRONMENT_STONEROOM = 5
EAX_ENVIRONMENT_AUDITORIUM = 6
EAX_ENVIRONMENT_CONCERTHALL = 7
EAX_ENVIRONMENT_CAVE = 8
EAX_ENVIRONMENT_ARENA = 9
EAX_ENVIRONMENT_HANGAR = 10
EAX_ENVIRONMENT_CARPETEDHALLWAY = 11
EAX_ENVIRONMENT_HALLWAY = 12
EAX_ENVIRONMENT_STONECORRIDOR = 13
EAX_ENVIRONMENT_ALLEY = 14
EAX_ENVIRONMENT_FOREST = 15
EAX_ENVIRONMENT_CITY = 16
EAX_ENVIRONMENT_MOUNTAINS = 17
EAX_ENVIRONMENT_QUARRY = 18
EAX_ENVIRONMENT_PLAIN = 19
EAX_ENVIRONMENT_PARKINGLOT = 20
EAX_ENVIRONMENT_SEWERPIPE = 21
EAX_ENVIRONMENT_UNDERWATER = 22
EAX_ENVIRONMENT_DRUGGED = 23
EAX_ENVIRONMENT_DIZZY = 24
EAX_ENVIRONMENT_PSYCHOTIC = 25
EAX_ENVIRONMENT_COUNT = 26
EAX_PRESET_GENERIC = 1
EAX_PRESET_PADDEDCELL = 2
EAX_PRESET_ROOM = 3
EAX_PRESET_BATHROOM = 4
EAX_PRESET_LIVINGROOM = 5
EAX_PRESET_STONEROOM = 6
EAX_PRESET_AUDITORIUM = 7
EAX_PRESET_CONCERTHALL = 8
EAX_PRESET_CAVE = 9
EAX_PRESET_ARENA = 10
EAX_PRESET_HANGAR = 11
EAX_PRESET_CARPETEDHALLWAY = 12
EAX_PRESET_HALLWAY = 13
EAX_PRESET_STONECORRIDOR = 14
EAX_PRESET_ALLEY = 15
EAX_PRESET_FOREST = 16
EAX_PRESET_CITY = 17
EAX_PRESET_MOUNTAINS = 18
EAX_PRESET_QUARRY = 19
EAX_PRESET_PLAIN = 20
EAX_PRESET_PARKINGLOT = 21
EAX_PRESET_SEWERPIPE = 22
EAX_PRESET_UNDERWATER = 23
EAX_PRESET_DRUGGED = 24
EAX_PRESET_DIZZY = 25
EAX_PRESET_PSYCHOTIC = 26
BASS_SYNC_POS = 0
BASS_SYNC_MUSICPOS = 0
BASS_SYNC_MUSICINST = 1
BASS_SYNC_END = 2
BASS_SYNC_MUSICFX = 3
BASS_SYNC_META = 4
BASS_SYNC_SLIDE = 5
BASS_SYNC_MESSAGE = $20000000
BASS_SYNC_MIXTIME = $40000000
BASS_SYNC_ONETIME = $80000000
CDCHANNEL = 0
RECORDCHAN = 1
BASS_ACTIVE_STOPPED = 0
BASS_ACTIVE_PLAYING = 1
BASS_ACTIVE_STALLED = 2
BASS_ACTIVE_PAUSED = 3
BASS_SLIDE_FREQ = 1
BASS_SLIDE_VOL = 2
BASS_SLIDE_PAN = 4
BASS_CDID_IDENTITY = 0
BASS_CDID_UPC = 1
BASS_CDID_CDDB = 2
BASS_CDID_CDDB2 = 3
BASS_DATA_AVAILABLE= 0
BASS_DATA_FFT512 = $80000000
BASS_DATA_FFT1024 = $80000001
BASS_DATA_FFT2048 = $80000002
BASS_DATA_FFT512S = $80000010
BASS_DATA_FFT1024S = $80000011
BASS_DATA_FFT2048S = $80000012
BASS_DATA_FFT_NOWINDOW = $20
BASS_INPUT_OFF = $10000
BASS_INPUT_ON = $20000
BASS_INPUT_LEVEL = $40000
BASS_INPUT_TYPE_MASK = $ff000000
BASS_INPUT_TYPE_UNDEF = $00000000
BASS_INPUT_TYPE_DIGITAL = $01000000
BASS_INPUT_TYPE_LINE = $02000000
BASS_INPUT_TYPE_MIC = $03000000
BASS_INPUT_TYPE_SYNTH = $04000000
BASS_INPUT_TYPE_CD = $05000000
BASS_INPUT_TYPE_PHONE = $06000000
BASS_INPUT_TYPE_SPEAKER = $07000000
BASS_INPUT_TYPE_WAVE = $08000000
BASS_INPUT_TYPE_AUX = $09000000
BASS_INPUT_TYPE_ANALOG = $0a000000
BASS_NET_TIMEOUT = 0
BASS_NET_BUFFER = 1
BASS_FILEPOS_DECODE = 0
BASS_FILEPOS_DOWNLOAD = 1
BASS_FILEPOS_END = 2
BASS_FILE_CLOSE = 0
BASS_FILE_READ = 1
BASS_FILE_QUERY = 2
BASS_FILE_LEN = 3
BASS_OBJECT_DS = 1
BASS_OBJECT_DS3DL = 2
BASS_VAM_HARDWARE = 1
BASS_VAM_SOFTWARE = 2
BASS_VAM_TERM_TIME = 4
BASS_VAM_TERM_DIST = 8
BASS_VAM_TERM_PRIO = 16
BASS_3DALG_DEFAULT = 0
BASS_3DALG_OFF = 1
BASS_3DALG_FULL = 2
BASS_3DALG_LIGHT = 3
BASS_FX_CHORUS = 0
BASS_FX_COMPRESSOR = 1
BASS_FX_DISTORTION = 2
BASS_FX_ECHO = 3
BASS_FX_FLANGER = 4
BASS_FX_GARGLE = 5
BASS_FX_I3DL2REVERB = 6
BASS_FX_PARAMEQ = 7
BASS_FX_REVERB = 8
BASS_FX_PHASE_NEG_180 = 0
BASS_FX_PHASE_NEG_90 = 1
BASS_FX_PHASE_ZERO = 2
BASS_FX_PHASE_90 = 3
BASS_FX_PHASE_180 = 4

BASS_CD_RWFLAG_READCDR = 1
BASS_CD_RWFLAG_READCDRW = 2
BASS_CD_RWFLAG_READCDRW2 = 4
BASS_CD_RWFLAG_READDVD = 8
BASS_CD_RWFLAG_READDVDR = 16
BASS_CD_RWFLAG_READDVDRAM = 32
BASS_CD_RWFLAG_READM2F1 = $100000
BASS_CD_RWFLAG_READM2F2 = $200000
BASS_CD_RWFLAG_READMULTI = $400000
BASS_CD_RWFLAG_READCDDA = $1000000
BASS_CD_RWFLAG_READCDDASIA = $2000000
BASS_CD_RWFLAG_READUPC = $40000000
BASS_CD_FREEOLD = $10000
BASS_SYNC_CD_ERROR = 1000
BASS_CD_DOOR_CLOSE = 0
BASS_CD_DOOR_OPEN = 1
BASS_CD_DOOR_LOCK = 2
BASS_CD_DOOR_UNLOCK = 3

# Additional error codes returned by BASS_ErrorGetCode
BASS_ERROR_WMA_LICENSE = 1000    # # the file is protected
BASS_ERROR_WMA_WM9 = 1001        # # WM9 is required
BASS_ERROR_WMA_DENIED = 1002     # # access denied (user/pass is invalid)
BASS_ERROR_WMA_CODEC = 1003      # # no appropriate codec is installed

# Additional flags for use with BASS_WMA_EncodeOpenFile/Network
BASS_WMA_ENCODE_TAGS = $10000    #  set tags in the WMA encoding
BASS_WMA_ENCODE_SCRIPT = $20000  #  set script (mid-stream tags) in the WMA encoding

# Additional flag for use with BASS_WMA_EncodeGetRates
BASS_WMA_ENCODE_RATES_VBR = $10000 #  get available VBR quality settings

# WMENCODEPROC "type" values
BASS_WMA_ENCODE_HEAD = 0
BASS_WMA_ENCODE_DATA = 1
BASS_WMA_ENCODE_DONE = 2

# BASS_CHANNELINFO type
BASS_CTYPE_STREAM_WMA = $10300

Local dll:Int = LoadLibraryA("bass.dll")
Local dll2:Int = LoadLibraryA("basswma.dll")
Local addr:Int
Local addl:Long

addr = Int(GetProcAddress(dll,"BASS_Init"))
Global BASS_Init%(device:Int, freq:Int, flags:Int, win:Int, clsid:Int) "win32"
(Int Ptr(Varptr(BASS_Init)))[0]=addr

# changed in 1.18 - no more $z, use :Byte Ptr instead
#addr:Int = Int(GetProcAddress(dll,"BASS_StreamCreateFile")) #"win32"
#Global BASS_StreamCreateFile%(mem:Int, file$z, offset:Int, length:Int, flags:Int) "win32"
#(Int Ptr(Varptr(BASS_StreamCreateFile)))[0]=addr

#addr:Int = Int(GetProcAddress(dll2,"BASS_WMA_StreamCreateFile")) #"win32"
#Global BASS_WMA_StreamCreateFile%(mem:Int, file$z, offset:Int, length:Int, flags:Int) "win32"
#(Int Ptr(Varptr(BASS_WMA_StreamCreateFile)))[0]=addr

#addr:Int = Int(GetProcAddress(dll,"BASS_MusicLoad")) #"win32"
#Global BASS_MusicLoad%(mem:Int, file$z, offset:Int, length:Int, flags:Int, freq:Int) "win32"
#(Int Ptr(Varptr(BASS_MusicLoad)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_StreamCreateFile")) #"win32"
Global BASS_StreamCreateFile%(mem:Int, file:Byte Ptr, offset:Int, length:Int, flags:Int) "win32"
(Int Ptr(Varptr(BASS_StreamCreateFile)))[0]=addr

addr:Int = Int(GetProcAddress(dll2,"BASS_WMA_StreamCreateFile")) #"win32"
Global BASS_WMA_StreamCreateFile%(mem:Int, file:Byte Ptr, offset:Int, length:Int, flags:Int) "win32"
(Int Ptr(Varptr(BASS_WMA_StreamCreateFile)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_MusicLoad")) #"win32"
Global BASS_MusicLoad%(mem:Int, file:Byte Ptr, offset:Int, length:Int, flags:Int, freq:Int) "win32"
(Int Ptr(Varptr(BASS_MusicLoad)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelPlay")) #"win32"
Global BASS_ChannelPlay%(handle:Int, restart:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelPlay)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_Free")) #"win32"
Global BASS_Free%()"win32"
(Int Ptr(Varptr(BASS_Free)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ErrorGetCode")) #"win32"
Global BASS_ErrorGetCode%()"win32"
(Int Ptr(Varptr(BASS_ErrorGetCode)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_StreamGetLength")) #"win32"
Global BASS_StreamGetLength%(handle:Int) "win32"
(Int Ptr(Varptr(BASS_StreamGetLength)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelStop")) #"win32"
Global BASS_ChannelStop%(handle:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelStop)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelPause")) #"win32"
Global BASS_ChannelPause%(handle:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelPause)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelIsActive")) #"win32"
Global BASS_ChannelIsActive%(handle:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelIsActive)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelGetLevel")) #"win32"
Global BASS_ChannelGetLevel%(handle:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelGetLevel)))[0]=addr

addl:Long = Int(GetProcAddress(dll,"BASS_ChannelGetPosition")) #"win32"
Global BASS_ChannelGetPosition%(handle:Int) "win32"
(Long Ptr(Varptr(BASS_ChannelGetPosition)))[0]=addl

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelSetPosition")) #"win32"
Global BASS_ChannelSetPosition%(handle:Int, pos:Long) "win32"
(Int Ptr(Varptr(BASS_ChannelSetPosition)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelGetAttributes")) #"win32"
Global BASS_ChannelGetAttributes%(handle:Int, freq:Int Var, vol:Int Var, pos:Int Var) "win32"
(Int Ptr(Varptr(BASS_ChannelGetAttributes)))[0]=addr

addr:Int = Int(GetProcAddress(dll,"BASS_ChannelSetAttributes")) #"win32"
Global BASS_ChannelSetAttributes%(handle:Int, freq:Int, vol:Int, pan:Int) "win32"
(Int Ptr(Varptr(BASS_ChannelSetAttributes)))[0]=addr


Function MakeLong:Long(HiWord:Int, LoWord:Int)

	#2 ints 8 bytes
	Return (HiWord Shl 16) | (LoWord & $FFFF)

End Function



Rem
nt = BASS_Init(True,44100,0,0,0)
ch = BASS_StreamCreateFile(False,"song.mp3",0,0,0)
pl = BASS_ChannelPlay(ch, False)
bf = BASS_Free()
er = BASS_ErrorGetCode()

BASS_Init:int (device:int, freq:int, flags:int, win:int, clsid:int)
BASS_Free()
BASS_ErrorGetCode%()
BASS_StreamCreateFile%(mem:int, file$, offset:int, length:int, flags:int)
BASS_WMA_StreamCreateFile%(mem:int, file$, offset:int, length:int, flags:int)
BASS_MusicLoad%           (mem:int, file$, offset:int, length:int, flags:int, freq:int)
BASS_ChannelPlay%(handle:int, restart:int)
BASS_StreamGetLength%(handle:int)
BASS_ChannelStop%(handle:int)
BASS_ChannelPause%(handle:int)
BASS_ChannelIsActive%(handle:int)
BASS_ChannelGetLevel%(handle:int)
BASS_ChannelGetPosition%(handle:int)
BASS_ChannelSetPosition%(handle:int, pos:int)

BASS_ChannelGetAttributes%(handle:int, fbank:Int Var, vbank:Int Var, pbank:Int Var)


def BASS_GetStringVersion$():
	Local Version,HiWord,LoWord
	Version = CreateBank(4)
	#PokeInt Version,0,BASS_GetVersion()
	HiWord = PeekShort(Version,0)
	LoWOrd = PeekShort(Version,2)
	return HiWord + "." + LoWord



# // Win32 API //%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%//
Extern "win32"
	Function SetWindowTextA:Int(hWnd:Int, lpString:Byte Ptr)
	Function GetActiveWindow:Int()
End Extern

# // Create Window %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%//
GFX_WIDTH = 320
GFX_HEIGHT = 200
BIT_DEPTH = 0
HERTZ = -1

Graphics GFX_WIDTH, GFX_HEIGHT, BIT_DEPTH, HERTZ
Local hWnd% = GetActiveWindow()
SetWindowTextA hWnd, "My Window"

End Rem
