# Songs-for-dad
Python-based tool to batch-download Bollywood songs as MP3s from YouTube using yt-dlp and ffmpeg. Built for offline car listening.
# Information
This project is a Python-based automation tool designed to download Bollywood songs in MP3 format directly from YouTube using yt-dlp and ffmpeg.

Originally created to help my father enjoy his favorite old Hindi songs in the car without needing internet or streaming apps, this script takes a list of song titles, searches for the best YouTube matches, downloads them in bulk, and converts them into high-quality MP3s — all automatically.

It’s a simple but meaningful solution for anyone who wants offline access to classic music without the manual hassle.
# 🎵 Songs-for-dad

A Python-based automation tool that searches YouTube for Bollywood songs, downloads them in high-quality MP3 format using `yt-dlp` and `ffmpeg`, and saves them locally — perfect for offline listening in cars or music players.

📌 Why I Built This

My dad wanted a collection of old Bollywood classics on a pen drive for his car — no Spotify, no YouTube, just pure MP3s. Manually searching, downloading, and converting each track was too slow and painful, so I built a tool to automate it all.

🚀 Features

- ✅ Accepts a list of songs from a `.txt` file
- 🔎 Automatically searches YouTube for the best match
- 🎧 Downloads and converts videos to MP3 using `yt-dlp` and `ffmpeg`
- 📁 Saves songs to a specified folder with clean filenames
- ⏳ Shows real-time download progress
- 🔄 Handles multiple songs in a batch process

🧰 Tech Stack

- Language: Python 3
- Libraries:
  - `yt-dlp` – for downloading and YouTube search
  - `ffmpeg` – for audio extraction
  - `tqdm` – for progress bar
  - `os`, `re`, `subprocess` – for handling files and processes

📂 Input Format

Put all the song titles in a simple text file like:
Tujhe Dekha To
Pehla Nasha
Tum Hi Ho
Lag Ja Gale


Name it something like `songs.txt`.

#⚙️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Shivam109677/Songs-for-dad.git
   cd songs-for-dad
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Make sure ffmpeg is installed and added to PATH:
   FFmpeg Download
   
5. Run the script:
   ```bash
   python download_songs.py
   
💡 Use Cases

Offline music for cars or grandparents

Quick creation of MP3 playlists from YouTube

Personal backups of rare songs

🤝 Contributions

Feel free to fork, improve, or raise issues. Pull requests are welcome!

📜 License

This project is licensed under the MIT License.


