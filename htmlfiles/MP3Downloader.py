from pytube import YouTube
import os

yt = YouTube(str(input("Enter The URL That You Want To Download >> ")))

video = yt.streams.filter(only_audio=True).first()

print("Enter The Destination You Want >> ")
destination = str(input(">> "))

out_file = video.download(output_path=destination)

base ,ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

print(yt.title + "Download ended Successfully")