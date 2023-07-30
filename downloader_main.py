from pytube import YouTube
import getpass

#download location
username = getpass.getuser() 
yt_videos_download_path = 'C:\\Users\\' + username + '\\Videos\\yt videos' 

#link insertion
link = input("Insert video link: ")
yt = YouTube(link)

#download
print("Video ", yt.title, " is being downloaded...")
yt_vid_download = yt.streams.get_highest_resolution()
yt_vid_download.download(yt_videos_download_path)


