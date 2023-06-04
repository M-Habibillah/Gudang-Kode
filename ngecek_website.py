# Import the required libraries
import urllib.request
from tkinter import *
import tkinter as tk

window=Tk()

# Set the size of the tkinter window
window.geometry("700x350")
window.title("HBeey")#give title to the window
head=Label(window, text="Website Connectivity Checker \n ngecek website ada atau enggak", font=('Calibri 15'))# a label
head.pack(pady=20)


url=tk.StringVar()# url is of string type

#main command
def check():
    web= (url.get())
    status_code = urllib.request.urlopen(web).getcode()
    website_is_up = status_code == 200
    if website_is_up==TRUE:
        Label(window, text="Website Available \n website nya ada", font=('Calibri 15')).place(x=260,y=200)
    else:
        Label(window, text="Website Not Available \n website nya ga ada", font=('Calibri 15')).place(x=260,y=200)

Entry(window, textvariable=url).place(x=200,y=80,height=30,width=280)# enter a website url
#create a button
Button(window, text="Check",command=check).place(x=320,y=160)
window.mainloop()

# https://pythongeeks.org/python-website-connectivity-checker-project/