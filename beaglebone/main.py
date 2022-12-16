#!/usr/bin/python

import Adafruit_DHT
import Adafruit_BBIO.UART as UART
import serial
from game2048 import Game2048
from uart_tools import UARTTools
UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.flushInput()
ser.flushOutput()

tools = UARTTools(ser)

while True:
    game = Game2048(4)
    while True:
        tools.print_board(game)
        if not game.win:
            direction = tools.handle_buttons()
            if direction != None:
                game.move(direction)
        if(tools.handle_reset()):
            break
        
ser.close()