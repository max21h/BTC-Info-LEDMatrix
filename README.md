# BTC-Info-LEDMatrix
Show CKPool Infos or BTC Price on LED Matrix Modul

## Requirements
  - Raspberry PI
  - LED Matrix Modul
  
 ## Software Requirements
  ### Update Raspbian
    sudo apt-get update 
    sudo apt-get upgrade
   ### Install Python
    https://raspberrytips.com/install-latest-python-raspberry-pi/
   ### Install Requests
    sudo pip3 install requests
   ### Install Luma for LED Matrix
    https://luma-led-matrix.readthedocs.io/en/latest/install.html
    
 ## Activate SPI:
  1. Run sudo raspi-config
  2. Use the down arrow to select 5 Interfacing Options 
  3. Arrow down to P4 SPI 
  4. Select yes when it asks you to enable SPI 
  5. Also select yes when it asks about automatically loading the kernel module
  6. Use the right arrow to select the <Finish> button 
  7. Reboot
  
  ## Download BTC-Info-LEDMatrix
    mkdir -p btcinfoLedMatrix; cd btcinfoLedMatrix 
    git clone https://github.com/BTC-Info-LEDMatrix/btcInfo.git
    cd btcinfoLedMatrix
    
   ## Parameters
    1. URL for example: https://solo.ckpool.org/users/bc1...
    2. mode (look at "Run Modes")
    3. Brightness of LED Matriy
    
     Run Modes
      -1 or empty: Complete JSON line by line
      0: first line of JSON
      1: second line of JSON
      2: third line of JSON
      3: ...and so on
      
   ## Start Script
    Option 1 (Direct):
      python3 btcInfo.py [https://solo.ckpool.org/users/bc1...] [mode as integer] [brightness as integer]
    Option 2 (Background):
      nohup python3 jsonToLEDMatrix.py [https://solo.ckpool.org/users/bc1...] [brightness as integer] [brightness as integer] &
      
      
