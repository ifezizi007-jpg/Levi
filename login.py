#create an application using tkinter that downloads youtube vidos
# using tkinter  

import tkinter as tk
from tkinter import filedialog , messagebox
from pytube import  YouTube
import threading
# Downdoad function
def download_Video():
    Url =url_Entry.get() .strip()
    Folder =folder_path. get() .strip()
    
    if not Url :
        messagebox .showerror ("error ,please enter a youtube url")
        return
    if not Folder :
        messagebox .showerror ("error ,please select a download forlder",)
        return
    try:
        yt=YouTube (Url)
        stream=yt.stream. get_hihgest_resolution()
        status_label.config(text="downloading...",fg=("blue"))
        stream.download(Folder)
        status_label.config(text="download complete;",fg="green")
    except Exception as e:
        messagebox. showerror("error",f"download failed.in {e}")
        status_label.config(text="fg=red")
# run download in a spearte thread to keep UI responsive 
def start_download ():
    threading.Thread (target=download_Video,daemon=True).start()
#  folder selection 
def browse_folder():
    Folder_selected =filedialog.askdirectory()
    if Folder_selected:
        folder_path.set (Folder_selected)
# cuiI setup
root =tk.Tk()
root.title ("youtube video downloar")  
root.geometry("500x250")   
root.resizable (False,False)   

folder_path=tk.StringVar()
tk.Label(root,text="youtube video url", font=("airial",12)).pack(pady=5)


url_Entry =tk.Entry (root, width=50)
url_Entry.pack (pady=5)

tk.Button(root,text="sleect download folder",command= browse_folder).pack(pady=5)
tk.Button(root,text="download vidoe",command=start_download,bg="green",fg="white").pack(pady=5)

status_label =tk.Label (root,text="",font=("arial",10))
status_label.pack (pady=5)




root . mainloop ()






















    




