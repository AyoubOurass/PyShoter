#! python3
import os 
from tkinter import *
from PIL import Image,ImageTk,ImageGrab
import datetime
import subprocess
from playsound import playsound
import getpass 


line = ("C:\\Users\ "+str(getpass.getuser())+"\Pictures\Screenshots")
line = line.replace(" ","")
if os.path.exists(line) == True:
	pass
else : 
	os.mkdir(line)



window = Tk()
window.title("PyShoter v1.0")
window.geometry("300x300")
window.configure(bg="#555e6f")
window.iconbitmap(r'Extensions/icon.ico')

image = Image.open("Extensions/image.png")
image = image.resize((100,100),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
picture = Label(image=photo,bg="#555e6f")
picture.pack()

image1 = Image.open("Extensions/facebook.png")
image1 = image1.resize((22,22),Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image1)
picture2 = Label(image=photo2, bg="#555e6f")


text = Label(text="PyShoter v1.0", bg='#555e6f', fg='black', font=('Bauhaus 93',20))
text.pack()

def shot():

	pic =  str(datetime.datetime.now())
	new = pic.replace(':','')
	new1 = new.replace('-','')
	new2 = new1.replace('.','')
	new3 = new2.replace(' ','-')+str(".png")
	new4 = ("PyShoter_"+new3)

	#line = ("C:\\Users\ "+str(getpass.getuser())+"\Pictures\Screenshots\\")
	#line = line.replace(" ","")

	screenshot = ImageGrab.grab()
	file = str("C:/Users/"+getpass.getuser()+"/Pictures/Screenshots/"+new4)
	outputfile = (file)
	screenshot.save(outputfile)


	playsound("Extensions/sound.mp3")



def exitt():
	window.destroy()

def facebook():

	subprocess.check_output("start chrome.exe https://www.facebook.com/Ay0ub.90", shell=True)
	

button1 = Button(window, text="Shot",font=('Lucida Console',20,),width=5, bg="#2a292a", fg="white",relief=FLAT,activebackground='#2a292a',activeforeground="white",command=shot)
button1.place(x=105,y=150)
button2 = Button(window, text="Exit",font=('Lucida Console',20,),width=5, bg="#2a292a", fg="white",relief=FLAT,activebackground='#2a292a',activeforeground="white",command=exitt)
button2.place(x=105,y=215)
button3 = Button(window, bg="#555e6f",image=photo2,relief=FLAT,activebackground='#555e6f', command=facebook)
button3.place(x=272,y=273)
window.resizable(False, False)
window.mainloop()



