# yt-playlist
A YouTube playlist downloader. Requires [Python 3.11+](https://www.python.org/downloads/), [pytube](https://github.com/nficano/pytube), and [ffmpeg](https://www.ffmpeg.org/) to work.

This script will download the audio of every song in a YouTube playlist, then convert the audio to mp3. To use, place it in the folder in which you want to download the playlist.

Please let me know if there are any bugs.

## Packages and versions
- pytube==12.1.0

## Installation
1. git clone ``https://github.com/Charlzk05/yt-playlist.git`` or download the source code
2. navigate to the folder
3. download ffmpeg
    https://github.com/BtbN/FFmpeg-Builds/releases
4. do ``pip install -r requirements.txt`` to install the package from requirements.txt

6. enjoy!

## Usage
- Please enter
        py yt-playlist-download.py [url of the playlist you wish to download]

        (playlist from youtube only)
    - e.g. 
    py yt-playlist-download.py https://www.youtube.com/playlist?list=OLAK5uy_lbX9HmX4ZrMSrS5wpDonp-EFy4IrhQeCc

