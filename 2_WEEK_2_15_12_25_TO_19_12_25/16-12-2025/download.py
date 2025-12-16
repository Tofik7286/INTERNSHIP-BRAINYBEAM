import yt_dlp
import os

def download_video(url):
    download_folder = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_folder, exist_ok=True)

    ydl_opts = {
        # Best video + best audio
        'format': 'bestvideo+bestaudio/best',
        # Save file as MP4
        'merge_output_format': 'mp4',
        # Output filename
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        # Do not download playlists
        'noplaylist': True,
        # Show progress
        'progress_hooks': [progress_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']}  Speed: {d['_speed_str']}  ETA: {d['_eta_str']}")
    elif d['status'] == 'finished':
        print("Download completed. Merging audio and video...")

if __name__ == "__main__":
    url = input("Paste YouTube URL here: ").strip()
    download_video(url)
    print("\nDone! Check the 'downloads' folder.")
