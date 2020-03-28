from Tkinter import *
import os
import pygame
import tkFileDialog
import numpy as num
import pandas as p

master = Tk()
master.minsize(300,100)
master.title('Alex Mercer')

trkno = 0
songs = []
def browse():
	global songs
	global dir
	songs = []
	os.chdir(dir)
	for j in os.listdir(dir):
		if j.endswith('.mp3' or '.wav'):
			songs.append(j)
	print(songs)


dir = tkFileDialog.askdirectory()
os.chdir(dir)
for i in os.listdir(dir):
    if i.endswith(".mp3" or '.wav'):
        songs.append(i)
print(songs)
pygame.mixer.init()
pygame.mixer.music.load(songs[0])


def play():
    global trkname
    global trkno
    global pi
    if pi==0:
        pygame.mixer.music.play()
        trkname.set((str(songs[trkno])).replace(".mp3",""))
    else:
        pygame.mixer.music.unpause()
    
def stop():
    global pi
    pygame.mixer.music.pause()
    pi=1


def nexttrk():
    global trkname
    global trkno
    global songs
    trkno += 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3",""))
    

def prevtrk():
    global trkname
    global trkno
    global songs
    trkno -= 1
    pygame.mixer.music.load(songs[trkno])
    pygame.mixer.music.play()
    trkname.set((str(songs[trkno])).replace(".mp3",""))


def voli():
    global vol
    vol=pygame.mixer.music.get_volume()
    vol += 0.1
    if vol>=0.9921875:
        vol = 0.9921875
    pygame.mixer.music.set_volume(vol)


def vold():
    global vol
    vol=pygame.mixer.music.get_volume()
    vol -= 0.1
    if vol<0:
        vol = 0.0
    pygame.mixer.music.set_volume(vol)

font1='Helvetica', 25, 'bold'
font2='Baskerville', 15, 'bold'


trkname=StringVar()
pi = 0
vol = 1
Button(master,text='Next',command=nexttrk).grid(row=1,column=3,sticky=W,pady=4)
Button(master,text='Previous',command=prevtrk).grid(row=1,column=0,sticky=W,pady=4)
Button(master,text='Pause',command=stop).grid(row=1,column=1,sticky=W,pady=4)
Button(master,text='Play',command=play).grid(row=1,column=2,sticky=W,pady=4)
Label(master,textvariable=trkname,font=font1).grid(row=1,column=4)
Button(master,text=' Volume + ',command=voli).grid(row=2,column=0,sticky=W,pady=4)
Button(master,text=' Volume - ',command=vold).grid(row=2,column=3,sticky=W,pady=4)
Button(master,text='Browse',command=browse).grid(row=2,column=4,sticky=W,pady=4)


master.mainloop()