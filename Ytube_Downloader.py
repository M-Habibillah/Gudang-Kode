# importing modules
from pytube import YouTube
from tkinter import *
import tkinter as tk


# Create an instance of tkinter frame or window
window = Tk()
# Set the size of the tkinter window
window.geometry("700x350")
window.title("HBeey")  # give title to the window

text = tk.StringVar()
Label(window, text="DOWNLOAD VIDEO dari YOUTUBE ",bg='grey', font=('Calibri 15')).pack()  # a label
Label(window, text="Copas Link Di Sini", font=('Calibri 12')).pack()  # a label
Entry(window,textvariable=text,width=50).pack()  # entry field

res1 = IntVar()
res2 = IntVar()
res3 = IntVar()
Checkbutton(text='360p',onvalue=18, offvalue=0,variable=res1).pack()#creating checkbox
Checkbutton(text='720p',onvalue=22, offvalue=0,variable=res2).pack()#creating checkbox
Checkbutton(text='1080p',onvalue=37, offvalue=0,variable=res3).pack()#creating checkbox


def downloader():  # defining a function
    global res  # global variable
    t = text.get()  # getting the value
    video = YouTube(t)

    if res1 == 18:
        res = 18
    elif res2 == 22:
        res = 22
    elif res3 == 37:
        res = 37

    video_streams = video.streams.filter(file_extension='mp4').get_by_itag(res)
    video_streams.download(filename="Untitled", output_path="video_path")
    Label(window, text="Downloaded Successfully").pack()


#creating a button
Button(window,text="Download",bg='green',command=downloader).pack()


window.mainloop()


# Source = https://pythongeeks.org/python-youtube-video-downloader-code/