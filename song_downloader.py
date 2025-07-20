import os
from yt_dlp import YoutubeDL
from tqdm import tqdm

# Path to your songs list
SONG_LIST_FILE = r"C:\\Users\\raina\\OneDrive\\Desktop\\New folder\\songs.txt"

OUTPUT_DIR = "C:/Users/raina/OneDrive/movies"  # Your desired folder

# Ensure output folder exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read songs from text file
with open(SONG_LIST_FILE, "r", encoding="utf-8") as f:
    songs = [line.strip() for line in f if line.strip()]

# YT-DLP settings
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True,
    'noplaylist': True
}

# Download loop
with YoutubeDL(ydl_opts) as ydl:
    for song in tqdm(songs, desc="Downloading songs"):
        try:
            tqdm.write(f"🔍 Searching: {song}")
            ydl.download([f"ytsearch1:{song}"])
        except Exception as e:
            tqdm.write(f"❌ Error downloading '{song}': {e}")

print("✅ All downloads finished.")
