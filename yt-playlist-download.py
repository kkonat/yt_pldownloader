import sys, os, shutil, subprocess
from pytube import Playlist, YouTube


def run(pl):
    # insert the downloads destination (optional)
    # e.g. C:\Users\Username\Folder
    # filepath = input("Downloads destination (optional): ")
    filepath = "./Downloads"
    # get linked list of links in the playlist
    links = pl.video_urls
    # download each item in the list
    pllen = len(links)
    current = 0
    for l in links:
        # os.system("cls")
        print("Processing " + str(current) + " of " + str(pllen) + "... ")
        current += 1
        # converts the link to a YouTube object
        yt = YouTube(l)

        # takes first stream; since ffmpeg will convert to mp3 anyway
        # changes: added filter with file extension of mp4
        music = yt.streams.filter(file_extension="mp4").first()

        # gets the filename of the first video stream
        default_filename = music.default_filename

        new_filename = default_filename.replace("mp4", "mp3")
        new_filename = new_filename.replace("  ", " ")
        new_filename = new_filename.replace(" - ", "-")
        new_filename = new_filename.replace(" ", "_")
        # & messess up ffmpeg call in windows
        new_filename = new_filename.replace("&", "and")

        # remove illegal characters from new_filename_compacted
        new_filename = "".join(
            c
            for c in new_filename
            if c not in ("/", "\\", ":", "*", "?", '"', "<", ">", "|")
        )
        downloaded_path = os.path.abspath("./Downloads")

        # skip if new_filename already exists in downloaded_path
        if os.path.exists(os.path.join(downloaded_path, new_filename)):
            print("Already processed, skipping " + default_filename + "...")
            continue

        print("Downloading " + default_filename + " -> " + new_filename + "...")

        # downloads first video stream and rename the first video stream
        try:
            music.download()
        except:
            continue

        print("Converting to mp3....")

        # converts mp4 video to mp3 audio and moving the audio to folder input
        # NOTE: MUST HAVE "ffmpeg.exe" DOWNLOADED AND PLACED INSIDE THE DIRECTORY
        try:
            subprocess.call(
                f'ffmpeg -i "{default_filename}" {new_filename}',
                shell=True,
            )
        except:
            os.remove(default_filename)
            continue

        # if exception then create download folder if not exists and store the downloaded audios
        try:
            # if filepath is empty then create download if not exists and store the downloaded audios
            if filepath == "":
                shutil.move(new_filename, downloaded_path, new_filename)
            else:
                shutil.move(new_filename, downloaded_path, new_filename)
        except:
            if os.path.exists("./Downloads"):
                shutil.move(new_filename, downloaded_path, new_filename)
            else:
                os.makedirs("./Downloads")
                shutil.move(new_filename, downloaded_path, new_filename)
        os.remove(default_filename)

    print("Download finished.")


if __name__ == "__main__":
    # check if command has onee argument annnd if it is a valid url

    if len(sys.argv) != 2:
        print("Please provide an url")
        exit(1)
    url = sys.argv[1]
    if not url.startswith("https://youtube.com/playlist?list="):
        print("Please enter a valid youtube playlist url")
        exit(1)
    pl = Playlist(url)
    run(pl)
