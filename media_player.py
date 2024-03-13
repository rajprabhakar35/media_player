import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# mixer.init

root=Tk()
root.title("M-Player")
root.geometry("560x700+290+10")
root.configure(background="skyblue")
root.resizable(False,False)
mixer.init()


def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END,song)

def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    Label(root,text=Music_Name).place(x=0,y=10)
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()


def PauseMusic():
    mixer.music.pause()  

def UnpauseMusic():
    mixer.music.unpause()

def Stop():
    mixer.music.stop()

def VolumeUp():
    volup=mixer.music.get_volume()
    mixer.music.set_volume(volup+0.1)

def VolumeDown():
    
    voldown=mixer.music.get_volume()
    mixer.music.set_volume(voldown-0.1)

image_icon=PhotoImage(file="player_icon.png")
root.iconphoto(False,image_icon)


upperimage=PhotoImage(file="COVER-Music.png")
upper_frame=Frame(root,width=565,height=380)
upper_frame.place(x=0,y=0)
Label(upper_frame,image=upperimage,width=565,height=375).pack()

lower_frame = Frame(root,bg="#FFFFFF",width=1000,height=180)
lower_frame.place(x=0,y=400)

# menu=PhotoImage(file="menu.png")
# Label(root,image=menu).place(x=0,y=580,width=485,height=100)

# Button(menu,image="back.png")

Button(root,text="browse music", width=69,height=1,font=("calibri",12,"bold"),fg="Black",bg="#ffffff",activebackground="green",command=AddMusic).place(x=0,y=550)

Frame_Music=Frame(root,bd=2,relief=RIDGE)
Frame_Music.place(x=0,y=585,width=561,height=100)

pause=PhotoImage(file="pause.png")
Button(lower_frame,image=pause,bg="#FFFFFF",bd=0,height=50,width=50,activebackground="grey",command=PauseMusic).place(x=100,y=20)



play=PhotoImage(file="play-button.png")
Button(lower_frame,text="play",image=play,bg="#FFFFFF",bd=0,height=50,width=50,activebackground="grey",command=PlayMusic).place(x=250,y=20)

stop=PhotoImage(file="stop-button.png",height=50,width=50)
Button(lower_frame,image=stop,bg="#FFFFFF",bd=0,height=50,width=50,activebackground="grey",command=Stop).place(x=400,y=20)


volumeup=PhotoImage(file="high-volume.png")
Button(lower_frame,image=volumeup,bg="#FFFFFF",bd=0,height=50,width=50,activebackground="grey",compound=RIGHT,command=VolumeUp).place(x=100,y=90)

volumedown=PhotoImage(file="volume-down.png")
Button(lower_frame,image=volumedown,bg="#FFFFFF",bd=0,height=50,width=50,activebackground="grey",command=VolumeDown).place(x=400,y=90)

scroll=Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music,width=90,font=("Times new roman", 10),bg="#333555",fg="grey",selectbackground="green",cursor="hand2",bd=0,yscrollcommand=scroll.set)
Playlist.pack(side=LEFT,fill=Y)

scroll.config(command=Playlist.yview)
scroll.pack(side=RIGHT,fill=BOTH)










root.mainloop()




