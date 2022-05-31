from tkinter import*
# MEMBERS:
# KRYSTYLL MAE M. LEMANA
# JOHANNE RALPH TRANSMONTE
# ALEXIS NATIVIDAD
#start
watch = Tk()
watch.geometry ("1000x600")
watch.title("STOPWATCH")
watch.config(bg = "darkslategray")

seconds = 00
minutes = 00
hours = 00
h = 00
j = 00

#FUNCTIONS
def create_label(text,_x,_y):
	label=Label(watch,text=text,fg="ivory3",bg="lightsteelblue4",font=("gothic",10,"bold"))
	label.place(x=_x,y=_y,width = 100,height=45)

def Start():
	global time, timer, seconds, minutes, hours
	seconds=seconds+1	
	if seconds == 10:
		minutes = minutes+1
		seconds=00
	
	elif minutes == 60:
		hours = hours+1
		minutes=00
		
	timer.config(text = f"{hours}:{minutes}:{seconds}")
	time = timer.after(60,Start)
	
def Stop():
	global time
	timer.after_cancel(time)

def Reset():
	global seconds, minutes,  hours
	seconds=00
	minutes=00
	hours=00
	
	timer.config(text = f'{hours}:{minutes}:{seconds}')
	timer.after_cancel(time)
	
def Split():
	global seconds,minutes,hours,time,self_job,timer,h,j
	if h<9:
		create_label((str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)),20+(110*h),400+(j*50))	
	else:
		j+=1
		h=0
		create_label((str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)),20+(110*h),400+(j*50))
	h+=1
		 		 
def Close():
	watch.destroy()
	
Top = Frame(watch, width = 300, height = 300, bg = "deepskyblue3")
Top.pack(side = TOP)
Bottom = Frame(watch, width = 300, height = 300, bg = "deepskyblue3")
Bottom.pack(side = BOTTOM)
Title = Label(Top, text = "StopWatch", font = ("gothic 80 bold"),
    fg = "midnightblue", bg = "powderblue")
Title.pack(fill = X)
timer = Label(Top, font = ("times new roman", 50), fg = "midnightblue",
    bg = "powderblue")
timer.pack(fill = X, expand = NO, pady = 10)
timer.config(text = f' {hours}:{minutes}:{seconds}')
Startt = Button(Bottom, text = 'START', font = ("gothic 18 bold"),
    fg = "lightblue2", bg = "royalblue4", width = 6, command = Start)
Startt.pack(side = LEFT,padx = 2, pady = 5)
Stopp = Button(Bottom, text = 'STOP', font = ("gothic 18 bold"),
    fg = "lightblue2", bg = "royalblue4", width = 6, command = Stop)
Stopp.pack(side = LEFT,padx = 2, pady = 5)
Resett = Button(Bottom, text = 'RESET', font = ("gothic 18 bold"),
    fg = "lightblue2", bg = "royalblue4", width = 6, command = Reset)
Resett.pack(side = LEFT,padx = 2, pady = 5)
Split_button=Button(Bottom,text="SPLIT",fg="lightblue2", bg = "royalblue4", command=Split,font=("gothic",18,"bold"), width = 6)
Split_button.pack(side = LEFT,padx = 2, pady = 5)

Close = Button(Bottom, text = 'CLOSE', font = ("gothic 18 bold"),
    fg = "lightblue2", bg = "royalblue4", width = 6, command = Close)

Close.pack(side = LEFT,padx = 2, pady = 5)



watch.mainloop()
	
