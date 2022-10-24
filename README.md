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
  
  ## GIT clone BTC-Info-LEDMatrix
    git clone https://github.com/max21h/BTC-Info-LEDMatrix.git
    
   ## Parameters
    1. Brightness of LED Matrix
    2. URL for example: https://solo.ckpool.org/users/bc1...
    3. mode (look at "Run Modes")
    
     Run Modes
      no set: Complete JSON line by line
      0: first line of JSON in a loop
      1: second line of JSON in a loop
      2: third line of JSON in a loop
      3: ...and so on
      
   ## Start Script (e.g. solo.ckpool info)
    Option 1 (Direct):
      python3 btcInfo.py [brightness as integer][https://solo.ckpool.org/users/bc1...] [mode as integer]
    Option 2 (Background):
      nohup python3 btcInfo.py [brightness as integer] [https://solo.ckpool.org/users/bc1...] [mode as integer] &
  
   ## Start Script (BTC/USDT Price from Binance API)
    Option 1 (Direct):
      python3 btcInfo.py [brightness as integer]
    Option 2 (Background):
      nohup python3 btcInfo.py [brightness as integer] &

  
![BTC/USDT Price Ticker](https://media.giphy.com/media/VOoDxEf03tR6rYt28b/giphy.gif)
  
## Donate
<img width="573" alt="image" src="https://user-images.githubusercontent.com/116381805/197489090-9f5e78f4-6c32-43b0-b544-67ccea1c12f3.png">
