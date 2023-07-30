from pytube import YouTube
import getpass

username = getpass.getuser() 
yt_videos_download_path = 'C:\\Users\\' + username + '\\Videos\\yt videos' 

link = input("Insert video link: ")

yt = YouTube(link)

print("Video ", yt.title, " is downloading.")

yt_vid_download = yt.streams.get_highest_resolution()
yt_vid_download.download(yt_videos_download_path)


print("Video has been downloaded to the " + yt_videos_download_path + " folder. Enjoy! :)")

