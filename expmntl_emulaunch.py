from evdev import uinput, InputDevice, categorize, ecodes
#from pynput.keyboard import Key, Controller
import psutil, sys, os, subprocess, shutil

#keyboard = Controller()
activeEmu = sys.argv[1]
activeROM = sys.argv[2]
print("activeROM is currently:(" + activeROM + ")")
from subprocess import Popen

isGamepad1 = bool(False)
isGamepad2 = bool(False)
isGamepad3 = bool(False)
isGamepad4 = bool(False)
isGamepad1Done = bool(False)
isGamepad2Done = bool(False)
isGamepad3Done = bool(False)
isGamepad4Done = bool(False)

eventNum = 1
controllerPath = '/dev/input/event'
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

#assigning gamepads as valid controller devices
while isGamepad1Done == False:
	print("Checking: (" + controllerPath + str(eventNum) + ") for gamepad1")		
	try:
		gamepad1 = InputDevice(controllerPath + str(eventNum))
		isGamepad1 = bool(True)
	except:
		print("Tried to assign gamepad as an invalid device")
		eventNum += 1
	
	#found a valid device, checking if controller is recognized
	if isGamepad1 == True:
		if (gamepad1.name == gpPS3 or gamepad1.name == gpGC or gamepad1.name == gpSwitchPro or gamepad1.name == gpSwitchPro2 or gamepad1.name == gpSega or gamepad1.name == gpLogitech or gamepad1.name == gpXBOX1):
			print("gamepad1 is = "+ gamepad1.name)
			isGamepad1Done = bool(True)
			eventNum += 1
		else :
			print("Input device not recognized within the whitelist")
			eventNum += 1
			isGamepad1 = bool(False)
	
	#stop looking for controllers beyond event30
	if eventNum >= 30:
		print("Could not find a valid controller to assign to gamepad1")
		isGamepad1Done = bool(True)
		isGamepad2Done = bool(True)
		isGamepad3Done = bool(True)
		isGamepad4Done = bool(True)
		exit()

while isGamepad2Done == False:
	print("Checking: (" + controllerPath + str(eventNum) + ") for gamepad2")
	try:
		gamepad2 = InputDevice(controllerPath + str(eventNum))
		isGamepad2 = bool(True)
	except:
		print("Tried to assign gamepad as an invalid device")
		eventNum += 1
	
	#found a valid device, checking if controller is recognized
	if isGamepad2 == True:
		if (gamepad2.name == gpPS3 or gamepad2.name == gpGC or gamepad2.name == gpSwitchPro or gamepad2.name == gpSwitchPro2 or gamepad2.name == gpSega or gamepad2.name == gpLogitech or gamepad2.name == gpXBOX1):
			print("gamepad2 is = "+ gamepad2.name)
			isGamepad2Done = bool(True)
			eventNum += 1
		else :
			print("Input device not recognized within the whitelist")
			eventNum += 1
			isGamepad2 = bool(False)
	
	#stop looking for controllers beyond event30
	if eventNum >= 30:
		print("Could not find a valid controller to assign to gamepad2")
		isGamepad2Done = bool(True)
		isGamepad3Done = bool(True)
		isGamepad4Done = bool(True)

while isGamepad3Done == False:
	print("Checking: (" + controllerPath + str(eventNum) + ") for gamepad3")
	try:
		gamepad3 = InputDevice(controllerPath + str(eventNum))
		isGamepad3 = bool(True)
	except:
		print("Tried to assign gamepad as an invalid device")
		eventNum += 1
	
	#found a valid device, checking if controller is recognized
	if isGamepad3 == True:
		if (gamepad3.name == gpPS3 or gamepad3.name == gpGC or gamepad3.name == gpSwitchPro or gamepad3.name == gpSwitchPro2 or gamepad3.name == gpSega or gamepad3.name == gpLogitech or gamepad3.name == gpXBOX1):
			print("gamepad3 is = "+ gamepad3.name)
			isGamepad3Done = bool(True)
			eventNum += 1
		else :
			print("Input device not recognized within the whitelist")
			eventNum += 1
			isGamepad3 = bool(False)
	
	#stop looking for controllers beyond event30
	if eventNum >= 30:
		print("Could not find a valid controller to assign to gamepad3")
		isGamepad3Done = bool(True)
		isGamepad4Done = bool(True)

while isGamepad4Done == False:
	print("Checking: (" + controllerPath + str(eventNum) + ") for gamepad4")
	try:
		gamepad4 = InputDevice(controllerPath + str(eventNum))
		isGamepad4 = bool(True)
	except:
		print("Tried to assign gamepad as an invalid device")
		eventNum += 1
	
	#found a valid device, checking if controller is recognized
	if isGamepad4 == True:
		if (gamepad4.name == gpPS3 or gamepad4.name == gpGC or gamepad4.name == gpSwitchPro or gamepad4.name == gpSwitchPro2 or gamepad4.name == gpSega or gamepad4.name == gpLogitech or gamepad4.name == gpXBOX1):
			print("gamepad4 is = "+ gamepad4.name)
			isGamepad4Done = bool(True)
		else :
			print("Input device not recognized within the whitelist")
			eventNum += 1
			isGamepad4 = bool(False)
	
	#stop looking for controllers beyond event30
	if eventNum >= 30:
		print("could not find a valid controller to assign to gamepad4")
		isGamepad4Done = bool(True)

#assigning buttons based on controller being used
if gamepad1.name == gpPS3:
	buttonHotkey = 296
	buttonStart = 297
	buttonRThmb = 299
elif gamepad1.name == gpGC:
	buttonHotkey = 295
	buttonStart = 297
elif gamepad1.name == gpSwitchPro or gamepad1.name == gpSwitchPro2:
	buttonHotkey = 312
	buttonStart = 313
	buttonRThmb = 315
elif gamepad1.name == gpSega:
	buttonHotkey = 296
	buttonStart = 297
elif gamepad1.name == gpXBOX1:
	buttonHotkey = 314
	buttonStart = 315
	buttonRThmb = 318
elif gamepad1.name == gpLogitech:
	buttonHotkey = 314
	buttonStart = 315
	buttonRThmb = 318
	
#settings configs for appropriate conditions
if activeEmu == 'gc':
	#assinging appropriate controller config file
	gcGPConfig = '/opt/retropie/configs/gc/Config/GCPadNew.ini'
	gcGPPS3 = '/opt/retropie/configs/gc/Config/Controllers/ps3/GCPadNew.ini'
	gcGPSP = '/opt/retropie/configs/gc/Config/Controllers/switchPro/GCPadNew.ini'
	gcGPSP2 = '/opt/retropie/configs/gc/Config/Controllers/switchPro2/GCPadNew.ini'
	gcGPDefault = '/opt/retropie/configs/gc/Config/Controllers/default/GCPadNew.ini'

	if gamepad1.name == gpPS3:
		with open(gcGPPS3, 'r') as file:
			gcGPString = "[GCPAD1]" + "\n" + file.read()
	elif gamepad1.name == gpSwitchPro:
		with open(gcGPSP, 'r') as file:
			gcGPString = "[GCPAD1]" + "\n" + file.read()
	elif gamepad1.name == gpSwitchPro2:
		with open(gcGPSP2, 'r') as file:
			gcGPString = "[GCPAD1]" + "\n" + file.read()
	else:
		with open(gcGPDefault, 'r') as file:
			gcGPString = "[GCPAD1]" + "\n" + file.read()

	if isGamepad2 == True:
		if gamepad2.name == gpPS3:
			with open(gcGPPS3, 'r') as file:
				gcGPString += "\n" + "[GCPAD2]" + "\n" + file.read()
		elif gamepad2.name == gpSwitchPro:
			with open(gcGPSP, 'r') as file:
				gcGPString += "\n" + "[GCPAD2]" + "\n" + file.read()
		elif gamepad2.name == gpSwitchPro2:
			with open(gcGPSP2, 'r') as file:
				gcGPString += "\n" + "[GCPAD2]" + "\n" + file.read()
		else:
			with open(gcGPDefault, 'r') as file:
				gcGPString += "\n" + "[GCPAD2]" + "\n" + file.read()
	
	if isGamepad3 == True:
		if gamepad3.name == gpPS3:
			with open(gcGPPS3, 'r') as file:
				gcGPString += "\n" + "[GCPAD3]" + "\n" + file.read()
		elif gamepad3.name == gpSwitchPro:
			with open(gcGPSP, 'r') as file:
				gcGPString += "\n" + "[GCPAD3]" + "\n" + file.read()
		elif gamepad3.name == gpSwitchPro2:
			with open(gcGPSP2, 'r') as file:
				gcGPString += "\n" + "[GCPAD3]" + "\n" + file.read()
		else:
			with open(gcGPDefault, 'r') as file:
				gcGPString += "\n" + "[GCPAD3]" + "\n" + file.read()
	
	if isGamepad4 == True:
		if gamepad4.name == gpPS3:
			with open(gcGPPS3, 'r') as file:
				gcGPString += "\n" + "[GCPAD4]" + "\n" + file.read()
		elif gamepad4.name == gpSwitchPro:
			with open(gcGPSP, 'r') as file:
				gcGPString += "\n" + "[GCPAD4]" + "\n" + file.read()
		elif gamepad4.name == gpSwitchPro2:
			with open(gcGPSP2, 'r') as file:
				gcGPString += "\n" + "[GCPAD4]" + "\n" + file.read()
		else:
			with open(gcGPDefault, 'r') as file:
				gcGPString += "\n" + "[GCPAD4]" + "\n" + file.read()
	
	file = open(gcGPConfig, 'w')
	n = file.write(gcGPString)
	file.close()
	print("Tried to write gcGPConfig as" + gcGPString)

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
for event in gamepad1.read_loop():
	if event.type == ecodes.EV_KEY:
		if event.value == 1:
			# Hotkey Button pressed
			if event.code == buttonHotkey:
				for event2 in gamepad1.read_loop():
                    
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