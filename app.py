import eel
from pytube import *
import moviepy.editor as mp
from win10toast import ToastNotifier
import os
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

toast = ToastNotifier()
folder_path = ""

@eel.expose
def browse_button():
    open_file = filedialog.askdirectory() # Returns opened path as str
    return open_file  

@eel.expose
def DonwloadMp3(url, W):
    videotitle = YouTube(url).title
    toast.show_toast(
    videotitle,
    "Downloading Now",
    duration = 5,
    threaded = True,
    )

    download_folder = W
    format_list2 = YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)
    os.chdir(download_folder)
    print(os.getcwd())
    
    
    character = ",'"
    
    for x in range(len(character)):
        videotitle = videotitle.replace(character[x],"")
    
    mp4_file = videotitle + '.mp4'
    mp3_file = videotitle + '.mp3'
    clip = mp.AudioFileClip(mp4_file)
    clip.write_audiofile(mp3_file)
    clip.close()
    os.remove(mp4_file)
    

@eel.expose
def DownloadMp4(url, W):
    videotitle = YouTube(url).title
    toast.show_toast(
    videotitle,
    "Downloading Now",
    duration = 5,
    threaded = True,
    )

    download_folder = W
    format_list2 = YouTube(url).streams.filter(mime_type='video/mp4').first().download(download_folder)
    os.chdir(download_folder)
    print(os.getcwd())
    
    
    character = ",'"
    
    for x in range(len(character)):
        videotitle = videotitle.replace(character[x],"")
    
    mp4_file = videotitle + '.mp4'
    



@eel.expose
def callPyt(vid, folder, type):
    print(str(vid))
    print(str(folder))
    print(str(type))
    
    if "https://www.youtube.com/playlist?list=" in str(vid) and str(type).lower() == "mp3":
        playlist = Playlist(str(vid))
        print(f'Downloading: ' + playlist.title)

        for video in playlist.videos:
            videoLink = "https://www.youtube.com/watch?v=" + video.video_id
            DonwloadMp3(videoLink, str(folder))

        
    if "https://www.youtube.com/playlist?list=" in str(vid) and str(type).lower() == "mp4":
        playlist = Playlist(str(vid))
        print(f'Downloading: ' + playlist.title)

        for video in playlist.videos:
            videoLink = "https://www.youtube.com/watch?v=" + video.video_id
            DownloadMp4(videoLink, str(folder))
        
    if "https://www.youtube.com/watch?v=" in str(vid) and str(type).lower() == "mp3":
        DonwloadMp3(str(vid), str(folder))
        
    if "https://www.youtube.com/watch?v=" in str(vid) and str(type).lower() == "mp4":
        DownloadMp4(str(vid), str(folder))
    
eel.init('web')
eel.start('index.html', size=(300, 500))