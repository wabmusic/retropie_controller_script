# retropie_controller_script
## Operating-System:
### Ubuntu 20.04.1 LTS
## Application:
### RetroPie

## Script Description
The script checks for plugged in preset controllers, and assigns them as gamepads from 1 through 4.

Assigns specific gamepad1 buttons to be recognized as hotkey buttons for later use.

Checks which core is being run, and determines which configurations need to be adjusted.
Writes dolphin controller configuration .ini file according to plugged in controllers, and preset configuration files.
Overwrites pcsx2 configurations with preset rom-specific optimized settings.

Listens for specific controller buttons being pushed to close down the core.
For pcsx2, listens for an extra button combination to launch/close QJoyPad
