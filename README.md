# sw-funduino-2048
Implementation of game 2048 on BeagleBone communicating with LED RGB matrix (Funduino v1.A board) by UART and with keyboard connected to arduino also by UART. Console version of the game is also available.

# Python 3.4
On our BeagleBone we does not have python 3.11 and numpy so we had to rewrite code for python 3.4 without numpy. We wanted to do it as simple as possible so we removed docs, inheritance etc. The code is in *python3.4* directory.

If you want to run console version of the game with python 3.4 and docker you can use *console34.sh* script. Docker compose was not used for simplicity.