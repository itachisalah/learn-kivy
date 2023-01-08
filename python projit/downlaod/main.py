# rakwan salah :devloper
from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name =  filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="check fial",fg ="red")

#download video
def DownlaodVideo():
    choice = ytdchoices.get()
    url = ytdEntryVar.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="cope line now",fg="red")


    #dowanload functio
    select.download(Folder_Name)
    ytdError.config(text="finsh download !!")


root = Tk()
root.title("salaheddine :V 1.12 youtube download ")
root.geometry("650x410+340+10")#set window
root.resizable(False,False)
root.columnconfigure(0,weight=1)#set all content in center.

f1=Frame(root,width=580,height=100,bg ='whitesmoke',bd=3,relief=GROOVE)
f1.place(x=30,y=130)
f2=Frame(root,width=580,height=55,bg='whitesmoke',bd=3,relief=GROOVE)
f2.place(x=30,y=250)

#Ytd link Label
t = Label(root, text='appliction download video and music',bg='red',fg='white',font=("Tajawal",15,'bold'))
t.pack(fill=X)
ytdLabel = Label(root, text ="please enter url video ", font =("Tajawal",15,'bold'))
ytdLabel.pack()

#Entry Box
ytdEntryVar = StringVar()
ytdEntryVar = Entry(root,width=70,justify='center',font=("Tajawal",15),fg='blue',textvariable=ytdEntryVar)
ytdEntryVar.pack()

#Error Msg
ytdError = Label(root,text="see download",fg="red",font=("Tajawal",10))
ytdError.pack()

#Asking save fille label

saveLabel = Label(root,text=":where save video",bg='whitesmoke',font=("Tajawal",15,"bold"))
saveLabel.place(x=390,y=140)

#btn of save file
saveEntry = Button (root,width=20,font=("Tajawal",12),bg="red",fg="white",text="how sava", command=openLocation)
saveEntry.place(x=410,y=180)

#Error Msg location
locationError = Label(root, text="not how savw video and music",bg='whitesmoke',fg="red",font=("Tajawal",12))
locationError.place(x=100,y=190)

#Download quality
ytdQuality = Label(root,text="check size video",bg='whitesmoke',font=("Tajawal",15,'bold'))
ytdQuality.place(x=430,y=255)

#combobox
choices = ("720p","144p","only voice")
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.place(x=260,y=265)

#donwload btn
downloadbtn =Button(root,text="download now",width=20,font=("tajawal",12),bg="red",fg="white",command =DownlaodVideo)
downloadbtn.place(x=40,y=255)

#developer Label
developerlabell= Label(root,text="don disian befor",font=("Tajawal",10))
developerlabell.place(x=265,y=350)
developerlabel = Label(root,text="salah DEVLOPER",font=("Tajawal",12))
developerlabel.place(x=250,y=370)

root.mainloop()