
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

def CreateWidgets():
    linkLabel = Label(root, text="SELECT THE FILE TO COPY : ", bg="deepskyblue4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    source_browseButton = Button(root, text="BROWSE", command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3, pady=5, padx=5)

    destinationLabel = Label(root, text="SELECT THE DESTINATION : ", bg="deepskyblue4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=50, textvariable=destinationLocation)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5, columnspan = 2)

    dest_browseButton = Button(root, text="BROWSE", command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=2, column=3, pady=5, padx=5)

    copyButton = Button(root, text="COPY FILE", command=CopyFile, width=15)
    copyButton.grid(row=3, column=1, pady=5, padx=5)

    moveButton = Button(root, text="MOVE FILE", command=MoveFile, width=15)
    moveButton.grid(row=3, column=2, pady=5, padx=5)

def SourceBrowse():

    root.files_list = list(filedialog.askopenfilenames(initialdir="Users\dell\source\repos\SiguriaNeInternet"))

    root.sourceText.insert('1', root.files_list)

def DestinationBrowse():

    destinationdirectory = filedialog.askdirectory(initialdir="Users\dell\source\repos\SiguriaNeInternet")

    root.destinationText.insert('1', destinationdirectory)

def CopyFile():

    files_list = root.files_list

    destination_location = destinationLocation.get()

 
    for f in files_list:

        shutil.copy(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES COPIED SUCCESSFULLY")

def MoveFile():

    files_list = root.files_list


    destination_location = destinationLocation.get()

    for f in files_list:

        shutil.move(f, destination_location)

    messagebox.showinfo("SUCCESS", "FILES MOVED SUCCESSFULLY")


root = tk.Tk()

root.geometry("830x120")
root.title("FILES COPY-MOVE APP")
root.config(background = "deepskyblue4")

sourceLocation = StringVar()
destinationLocation = StringVar()

CreateWidgets()

root.mainloop()
