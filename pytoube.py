import os
from pytube import Playlist
from pytube.cli import on_progress


def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())


def truncate_filename(title, max_length):
    return title[:max_length-4]


def download_progress(stream, chunk, file_handle, remaining):
    percent = (float(file_size - remaining) / file_size) * 100
    print(f"Downloading... {percent:.2f}% complete", end='\r')


link = input("Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)

folder_name = make_alpha_numeric(yt_playlist.title)
os.makedirs(folder_name, exist_ok=True)

total_video_count = len(yt_playlist.videos)
print("Total videos in playlist:", total_video_count)

MAX_FILENAME_LENGTH = 100  # Adjust the limit as needed

for index, video in enumerate(yt_playlist.videos, start=1):
    truncated_title = truncate_filename(video.title, MAX_FILENAME_LENGTH)
    file_path = os.path.join(folder_name, truncated_title + ".mp4")

    if os.path.exists(file_path):
        print(f"Skipping {truncated_title} - already downloaded")
        continue

    try:
        print("Downloading:", truncated_title)
        video_size = video.streams.get_highest_resolution().filesize
        file_size = video_size // (1024 ** 2)
        video.register_on_progress_callback(on_progress)
        video.streams.get_highest_resolution().download(output_path=folder_name, filename=truncated_title)
        print(f"\nDownloaded: {truncated_title} successfully! ({file_size} MB)")
    except Exception as e:
        print(f"\nError downloading {truncated_title}: {str(e)}")
        continue

    print("Remaining Videos:", total_video_count - index)

print("All videos downloaded successfully!")
