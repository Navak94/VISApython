from tkinter import *
import pyvisa 
import time
from pynput.keyboard import Key, Controller
import os
from subprocess import Popen
from subprocess import call
import RPi.GPIO as gpio
root=Tk()
keyboard = Controller()
info =""
h=1
w=2
p=-130 #shift buttons over left or right
s =30  #shift buttons up or down
gpio.setmode(gpio.BCM)
gpio.setup(16,gpio.OUT)
gpio.setup(6,gpio.OUT)
def retrieve_input():
    Start=textBox1.get("1.0","end-1c")
    End=textBox3.get("1.0","end-1c")
    Volty =textBox4.get("1.0","end-1c")
    CycleLoop=textBox2.get("1.0","end-1c")
    measuredVolts = 1
    rm = pyvisa.ResourceManager()
    print(rm.list_resources())
    #inst = rm.open_resource('USB0::5784::2103::005000000081::0::INSTR')
    #inst.write('*CLS') # clear error state in event of error
    #inst.write('CONFigure:OUTPut ON ')
    #inst.write('FETCh:VOLTage?')
    var13 = StringVar()
    var12 = StringVar()
    for cycle in range(1,int(CycleLoop)+2):
        
        for starting in range(1,int(Start)+1):
          gpio.output(16, gpio.HIGH)
          gpio.output(6, gpio.LOW)
          #if starting ==1:
              #inst.write('CONFigure:OUTPut ON')
              #inst.write('SOURce:VOLTage:SLEW 10;:VOLT '+str(Volty)+';:CURR 3 ')
          time.sleep(1)
          root.update()
          
          
          
        for ending in range(1,int(End)+2):
          gpio.output(16, gpio.LOW)
          gpio.output(6, gpio.HIGH)
          #if ending ==1:
              #inst.write('CONFigure:OUTPut OFF') 
          time.sleep(1)
          root.update()
        var14 = StringVar()
        var13.set("OFF:   ")
        var14.set("Cycle:  "+ str(cycle))
        label =Label( root, textvariable=var14, relief=FLAT, font =("Helvetica","40") )
        label.place(x=50,y=280)
        root.update()
    var14.set("Done          ")
    label =Label( root, textvariable=var14, relief=FLAT, font =("Helvetica","40") )
    label.place(x=50,y=280)
    #inst.write('CONFigure:OUTPut OFF') #turn off after last cycle is complete
    root.update()
                
def key0():
    keyboard.press('0')
def key1():
    keyboard.press('1')
def key2():
    keyboard.press('2')
def key3():
    keyboard.press('3')
def key4():
    keyboard.press('4')
def key5():
    keyboard.press('5')
def key6():
    keyboard.press('6')
def key7():
    keyboard.press('7')
def key8():
    keyboard.press('8')
def key9():
    keyboard.press('9')
def rebootpython():
    call('reboot')
    call("pkill -f /home/pi/Desktop/tkintermessing1.py",shell=True)
def shutOFF():
    call('sudo nohup shutdown -h now',shell=True)
def CLEAR1():
    print("went into clear")
    textBox1.delete('1.0',END)
    textBox2.delete('1.0',END)
    textBox3.delete('1.0',END)
    textBox4.delete('1.0',END)

root.title("Switch Application")    
root.attributes("-fullscreen",True) #fullscreen
#root.geometry("1280x720")
var = StringVar()
var.set("ON")
label =Label( root, textvariable=var, relief=FLAT ,font =("Helvetica","30"))
label.place(x=50,y=25)

textBox1=Text(root, height=2, width=4,font =("Helvetica","30"))
textBox1.place(x=50,y=100)

var1 = StringVar()
label1 = Label( root, textvariable=var1, relief=FLAT ,font =("Helvetica","30"))
var1.set("Cycles")
label1.place(x=40,y=150)

textBox2=Text(root, height=1, width=4,font =("Helvetica","30"))
textBox2.place(x=50,y=210)

varcyc = StringVar()
label1 = Label( root, textvariable=varcyc, relief=FLAT,font =("Helvetica","30") )
varcyc.set("OFF")
label1.place(x=180,y=25)

textBox3=Text(root, height=1, width=4,font =("Helvetica","30"))
textBox3.place(x=200,y=100)

varVOLT = StringVar()
label1 = Label( root, textvariable=varVOLT, relief=FLAT,font =("Helvetica","30") )
varVOLT.set("Volts")
label1.place(x=180,y=150)

textBox4=Text(root, height=1, width=4,font =("Helvetica","30"))
textBox4.place(x=200,y=210)


root.grid_propagate(False)

buttonCommit2=Button(root, height=h, width=w+4, font =("Helvetica","40"),text="Enter", command=lambda: retrieve_input())
buttonCommit2.place(x=50,y=350)

buttonPAD0=Button(root, height=h, width=w,font =("Helvetica","40"), text="0", command=lambda: key0())
buttonPAD0.place(x=432+p,y=20+s)

buttonPAD1=Button(root, height=h, width=w,font =("Helvetica","40"), text="1", command=lambda: key1())
buttonPAD1.place(x=552+p,y=220+s)

buttonPAD2=Button(root, height=h, width=w, font =("Helvetica","40"),text="2", command=lambda: key2())
buttonPAD2.place(x=672+p,y=220+s)

buttonPAD3=Button(root, height=h, width=w, font =("Helvetica","40"),text="3", command=lambda: key3())
buttonPAD3.place(x=792+p,y=220+s)

buttonPAD4=Button(root, height=h, width=w, font =("Helvetica","40"),text="4", command=lambda: key4())
buttonPAD4.place(x=552+p,y=120+s)

buttonPAD5=Button(root, height=h, width=w,font =("Helvetica","40"), text="5", command=lambda: key5())
buttonPAD5.place(x=672+p,y=120+s)

buttonPAD6=Button(root, height=h, width=w,font =("Helvetica","40"), text="6", command=lambda: key6())
buttonPAD6.place(x=792+p,y=120+s)

buttonPAD7=Button(root, height=h, width=w, font =("Helvetica","40"),text="7", command=lambda: key7())
buttonPAD7.place(x=552+p,y=20+s)

buttonPAD8=Button(root, height=h, width=w, font =("Helvetica","40"),text="8", command=lambda: key8())
buttonPAD8.place(x=672+p,y=20+s)

buttonPAD9=Button(root, height=h, width=w, font =("Helvetica","40"),text="9", command=lambda: key9())
buttonPAD9.place(x=792+p,y=20+s)

CLEAR=Button(root,height=h, width=w+4, font =("Helvetica","40"),text="Clear", command=lambda: CLEAR1())
CLEAR.place(x=300,y=350)

QUIT=Button(root, height=h, width=w+4, font =("Helvetica","40"),text="Restart", command=lambda: rebootpython())
QUIT.place(x=672+p,y=300+s)

Power=Button(root, height=h, width=w+4,font =("Helvetica","40"), text="Power", command=lambda:shutOFF())
Power.place(x=672+p,y=380+s)

root.mainloop()
