from tkinter import *
import threading
from quotesApiApp import quotesApiApp
import time

#thread flag 
f=False

class thread(threading.Thread):
    def __init__(self,h, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.h=h
 
        # helper function to execute the threads
    def run(self):

        obj=quotesApiApp()
        while True:
            obj.task()
            global f
            if f:
                del obj
                f=False
                break
            time.sleep(self.h)

        print("killed "+str(self.thread_name) +" "+ str(self.thread_ID));
 


class tkvalue(Exception):
    def __init__(self) -> None:
        super().__init__("exception in value tk")
        messageVar = Message(master,text = "The fields should not contain any letter",width=1000)
        messageVar.config(fg="red")
        messageVar.grid(row=4,column=1)



def convertTime(hours,mins,secs):
    total_secs=0
    try:
        if hours.isdigit():
            total_secs+=int(hours)*60*60
        elif hours!="":
            raise tkvalue()

        if mins.isdigit():
            total_secs+=int(mins)*60
        elif mins!="":
            raise tkvalue()

        if secs.isdigit():
            total_secs+=int(secs)
        elif secs!="":
            raise tkvalue()
    except tkvalue:
        print("heelo")
    else:
        try:
            thread1 = thread(total_secs,"qod app thread", 1000)
            thread1.start()
        except:
            print ("Error: unable to start thread")
        


master = Tk()
master.geometry("270x250")

secs=StringVar()
mins=StringVar()
hours=StringVar()

messageVar = Message(master,text = "\nEnter the time delay\n",width=1000)
messageVar.config(bg='lightgreen')
messageVar.grid(row=0,column=1)

Label(master, text='Hours').grid(row=1)
Label(master, text='Mins').grid(row=2)
Label(master, text='Secs').grid(row=3)

e1 = Entry(master,textvariable=hours)
e2 = Entry(master,textvariable=mins)
e3 = Entry(master,textvariable=secs)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)


def kill():
    global f
    f=True
    

button1 = Button(master, text='Start notifications', fg='black', bg='green',
                    command=lambda: convertTime(hours.get(),mins.get(),secs.get()), height=1, width=20)
button1.grid(row=5, column=1)

button2 = Button(master, text='Stop notifications', fg='black', bg='red',
                    command= lambda:kill(), height=1, width=20)
button2.grid(row=6, column=1)
mainloop()