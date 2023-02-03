# Pytube1080p
Get videos in 1080p resolution with this python script
# YouTube Video and Audio Downloader
This script allows you to download the video and audio streams of a YouTube video and merge them into a single mp4 file.

## Requirements
- python (pip install python)
- ffmpeg (installation instructions depend on your operating system)
- pytube (pip install pytube)

## Usage
1. Clone or download the repository to your local machine.
2. Install the required packages by running:

```
pip install -r requirements.txt
```
Run the script using:
```
python pytubw1080p.py
```


3. Enter the YouTube video URL when prompted.
4. The script will print information about the video, including the title, views, size, and available itags.
5. Enter the itags of the video and audio streams you want to download in that order, separated by a comma (e.g. 137, 140)
6. The script will download the selected streams and merge them into a single mp4 file in the same directory as the script.

**Note: The default download directory is set to '/Users/Desktop/pytube1080' but you can change it to any directory of your choice by modifying the download() method in the script.**

# Customization
You can customize the script by changing the default download directory, the file names of the downloaded streams, or the parameters passed to ffmpeg when merging the streams.
