# BTC-Info-LEDMatrix
Show CKPool Infos or BTC Price on LED Matrix Modul

Requierments:
	- Raspberry Pi
	- Matrix LED Module

Software Requierments:
	Update Raspbian
		sudo apt-get update 
		sudo apt-get upgrade
	Install Python
		https://raspberrytips.com/install-latest-python-raspberry-pi/
	Python Requests
		sudo pip3 install requests
	LED Matrix
		https://luma-led-matrix.readthedocs.io/en/latest/install.html

	
Activate SPI:
	1. Run sudo raspi-config 
	2. Use the down arrow to select 5 Interfacing Options 
	3. Arrow down to P4 SPI 
	4. Select yes when it asks you to enable SPI 
	5. Also select yes when it asks about automatically loading the kernel module 
	6. Use the right arrow to select the <Finish> button 
	7. Reboot.

Run Modes:
	-1: complete JSON line by line
	0: first line of JSON
	1: second line of JSON
	2: third line of JSON
	3: fourth line…
	4: fifth…
	5: ….
	.
	.
	.
	∞

Run (you can use any url that returns a json file):
	cd yourDirectory where btcInfo.py is located
	Run direct:
		python3 jsonToLEDMatrix.py [https://solo.ckpool.org/users/bc1...] [brightness as integer] [mode as integer]
	Run background:
		nohup python3 jsonToLEDMatrix.py [https://solo.ckpool.org/users/bc1...] [brightness as integer] [mode as integer] &
