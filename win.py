# Arch : sudo pacman -S tk python-pyserial


from tkinter import *
import serial

ser = serial.Serial('/dev/ttyUSB0')  	# open serial port
print(ser.name)         		# check which port was really used
ser.write(b'hello')     		# write a string
ser.close()

root = Tk()

def goForward():
	print("forward")

def goBack():
	print("back")

def goLeft():
	print("left")

def goRight():
	print("right")

frame = Frame(root)
frame.pack()
bF = Button(frame, text="FORWARD",fg="red", command=goForward)
bB = Button(frame, text="BACK",fg="red", command=goBack)
bR = Button(frame, text="RIGHT",fg="red", command=goRight)
bL = Button(frame, text="LEFT",fg="red", command=goLeft)
bF.pack(side=TOP)
bB.pack(side=BOTTOM)
bR.pack(side=RIGHT)
bL.pack(side=LEFT)

root.mainloop()
root.destroy()
