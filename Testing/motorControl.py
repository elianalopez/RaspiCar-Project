#motorControl.Py
#By Eliana Lopez

import RPi.GPIO as GPIO
import time
from tkinter import *
from tkinter import ttk

class motorController(object):   
    def int():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(7, True)
        GPIO.output(11, True)


    def right():
        int()
        print("Right")
        GPIO.output(13, True)
        GPIO.output(15, False)


    def left():
        int()
        print("Left")
        GPIO.output(13, False)
        GPIO.output(15, True)

        
    def forward():
        int()
        print("Forward")
        GPIO.output(16, True)
        GPIO.output(18, False)


    def backward():
        int()
        print("Backwards")
        GPIO.output(16, False)
        GPIO.output(18, True)

        
    def backStop():
        int()
        print("Back Stop")
        GPIO.output(16, False)
        GPIO.output(18, False)

        
    def frontStop():
        int()
        print("Front Stop")
        GPIO.output(13, False)
        GPIO.output(15, False)
        
    def endProgram():
        GPIO.cleanup()
        print("done")
        
    #root window    
    rw = Tk()

    #buttons
    btn1=ttk.Button(rw,text="right")
    btn1.pack()
    btn1.config(command=right)

    btn2=ttk.Button(rw,text="left")
    btn2.pack()
    btn2.config(command=left)

    btn3=ttk.Button(rw,text="forward")
    btn3.pack()
    btn3.config(command=forward)

    btn4=ttk.Button(rw,text="backward")
    btn4.pack()
    btn4.config(command=backward)

    btn5=ttk.Button(rw,text="front stop")
    btn5.pack()
    btn5.config(command=frontStop)

    btn6=ttk.Button(rw,text="back stop")
    btn6.pack()
    btn6.config(command=backStop)

    btn7=ttk.Button(rw,text="end")
    btn7.pack()
    btn7.config(command=endProgram)
