from pytube import YouTube
from pytube.cli import on_progress
import subprocess
import os
import re

url = input("Enter video url:")
yt = YouTube(url, on_progress_callback=on_progress)

print("Title: ", yt.title)
print("views: ", yt.views)
print("size:", yt.streams.get_highest_resolution().filesize/1024/1024, "MB")

for stream in yt.streams:
    print(stream.itag, stream.mime_type)

itags = [int(x) for x in input("Enter itags, separated by comma:").split(',')]
video_stream = yt.streams.get_by_itag(itags[0])
audio_stream = yt.streams.get_by_itag(itags[1])

if video_stream and audio_stream:
    video_file_name = f"{yt.title} ({itags[0]}).{video_stream.subtype}"
    audio_file_name = f"{yt.title} ({itags[1]}).{audio_stream.subtype}"
    video_file_name = re.sub(r'[^\w\-_\. ]', '_', video_file_name)
    audio_file_name = re.sub(r'[^\w\-_\. ]', '_', audio_file_name)
    video_stream.download('/Users/Desktop/pytube1080', filename=video_file_name)
    audio_stream.download('/Users/Desktop/pytube1080', filename=audio_file_name)
    
    print("video_file_name: ", video_file_name)
    print("audio_file_name: ", audio_file_name)
    print("current working directory: ", os.getcwd())
   
    output_file_name = f"{yt.title}.mp4"
    output_file_name = re.sub(r'[^\w\-_\. ]', '_', output_file_name)
    subprocess.run(['ffmpeg', '-i', os.path.join('/Users/Desktop/pytube1080', video_file_name), '-i', os.path.join('/Users/Desktop/pytube1080', audio_file_name), '-c', 'copy', output_file_name], cwd='/Users/Desktop/pytube1080')
    
else:
    if not video_stream:
        print(f"The itag {itags[0]} is not available for this video.")
    if not audio_stream:
        print(f"The itag {itags[1]} is not available for this video.")
    
