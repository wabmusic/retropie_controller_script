from evdev import uinput, InputDevice, categorize, ecodes
#from pynput.keyboard import Key, Controller
import psutil, sys, os, subprocess, shutil

#keyboard = Controller()
activeEmu = sys.argv[1]
activeROM = sys.argv[2]
print("activeROM is currently:(" + activeROM + ")")
from subprocess import Popen

isGamepad = bool(False)
eventNum = 1
tryLoops = 0
controllerPath = '/dev/input/event'
isAllowed = bool(False)
isQjoypad = bool(False)
procQjoypad = '/usr/bin/qjoypad'

#controller names whitelist
gpPS3 = 'MY-POWER CO.,LTD. 2In1 USB Joystick'
gpGC = 'NGC USB Gamepad     NGC USB Gamepad    '
gpSwitchPro = 'PDP CO.,LTD. Faceoff Deluxe Wired Pro Controller for Nintendo Switch'
gpSwitchPro2 = 'PDP CO.,LTD. Faceoff Deluxe Wired Pro Contro漀爀 一椀渀琀攀渀搀漀 匀眀椀琀挀栀Ḁ䠃伀刀䤀 '
gpSega = 'SWITCH CO.,LTD. USB Gamepad'
gpXBOX1 = 'Generic X-Box pad'
gpLogitech = 'Logitech Gamepad F310'

#assigning gamepad as first viable controller detected
while isGamepad == False:
	tryLoops += 1
	print("Proceeding with attempt #" + str(tryLoops))		
	try:
		gamepad = InputDevice(controllerPath + str(eventNum))
		isGamepad = bool(True)
	except:
		print("Tried to assign gamepad as an invalid device")
		eventNum += 1
	
	if isGamepad == True:
		if (gamepad.name == gpPS3 or gamepad.name == gpGC or gamepad.name == gpSwitchPro or gamepad.name == gpSwitchPro2 or gamepad.name == gpSega or gamepad.name == gpLogitech or gamepad.name == gpXBOX1):
			print("gamepad is = "+ gamepad.name)
		else :
			print("Input device not recognized within the whitelist")
			eventNum += 1
			isGamepad = bool(False)

#assigning buttons based on controller being used
if gamepad.name == gpPS3:
	buttonHotkey = 296
	buttonStart = 297
	buttonRThmb = 299
elif gamepad.name == gpGC:
	buttonHotkey = 295
	buttonStart = 297
elif gamepad.name == gpSwitchPro or gamepad.name == gpSwitchPro2:
	buttonHotkey = 312
	buttonStart = 313
	buttonRThmb = 315
elif gamepad.name == gpSega:
	buttonHotkey = 296
	buttonStart = 297
elif gamepad.name == gpXBOX1:
	buttonHotkey = 314
	buttonStart = 315
	buttonRThmb = 318
elif gamepad.name == gpLogitech:
	buttonHotkey = 314
	buttonStart = 315
	buttonRThmb = 318
	
#settings configs for appropriate conditions
if activeEmu == 'gc':
	#assinging appropriate controller config file
	oldConfigGP = '/opt/retropie/configs/gc/Config'
	os.remove(oldConfigGP + '/GCPadNew.ini')
	if gamepad.name == gpSwitchPro:
		newConfigGP = '/opt/retropie/configs/gc/Config/Controllers/switchPro/GCPadNew.ini'
	elif gamepad.name == gpSwitchPro2:
		newConfigGP = '/opt/retropie/configs/gc/Config/Controllers/switchPro2/GCPadNew.ini'
	elif gamepad.name == gpPS3:
		newConfigGP = '/opt/retropie/configs/gc/Config/Controllers/ps3/GCPadNew.ini'
	else:
		newConfigGP = '/opt/retropie/configs/gc/Config/Controllers/default/GCPadNew.ini'

	shutil.copy(newConfigGP, oldConfigGP)

elif activeEmu == 'ps2':
	oldConfig = '/home/toomu/.config/PCSX2/inis'	
	#Delete existing ps2 configurations
	shutil.rmtree(oldConfig)
	
	#Assign appropriate config to replace with according to activeROM
	if activeROM == '/home/toomu/RetroPie/roms/ps2/Champions':
		newConfig = '/opt/retropie/configs/all/ps2 configs/Champions/inis'
	elif activeROM == '/home/toomu/RetroPie/roms/ps2/X-Men':
		newConfig = '/opt/retropie/configs/all/ps2 configs/XMen/inis'
	elif activeROM == '/home/toomu/RetroPie/roms/ps2/Lord':
		newConfig = '/opt/retropie/configs/all/ps2 configs/LOTR/inis'
	elif activeROM == '/home/toomu/RetroPie/roms/ps2/Gran':
		newConfig = '/opt/retropie/configs/all/ps2 configs/GranTurismo/inis'
	elif activeROM == '/home/toomu/RetroPie/roms/ps2/Soulcalibur':
		newConfig = '/opt/retropie/configs/all/ps2 configs/SoulCalibur/inis'
	else:
		newConfig = '/opt/retropie/configs/all/ps2 configs/default/inis'
		
	#Copy the assigned config settings into emulator configs
	shutil.copytree(newConfig, oldConfig)

# Process to look for to kill when BOTH keys are pressed
if activeEmu == 'gc':
	procName = '/opt/retropie/emulators/dolphin/bin/dolphin-emu-nogui'
elif activeEmu == 'ps2':
	procName = '/usr/games/PCSX2'
			
#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
	if event.type == ecodes.EV_KEY:
		if event.value == 1:
			# Hotkey Button pressed
			if event.code == buttonHotkey:
				for event2 in gamepad.read_loop():
                    
					# Hotkey Button released
					if event2.code == buttonHotkey:
						break               

					# Start Button pressed
					elif event2.code == buttonStart:
						print("Hotkey and Start Buttons Pressed")
						for process in psutil.process_iter():
							if procQjoypad in process.cmdline():
								process.terminate()
							if procName in process.cmdline():
								print('Ending the declared process')
								process.terminate()
								exit()
								break
		     
					# Right stick pressed
					elif event2.code == buttonRThmb:
						print("Hotkey and Right Stick Pressed")
						#keyboard.tap(Key.f9)
						#toggle qjoypad activity
						if activeEmu == 'ps2':
							if isQjoypad == False:
								isQjoypad = bool(True)
								subprocess.Popen([procQjoypad])
							else:
								isQjoypad = bool(False)
								for process in psutil.process_iter():
									if procQjoypad in process.cmdline():
										process.terminate()
						break
						
		
		     	
