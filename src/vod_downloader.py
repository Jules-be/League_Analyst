from pytube import YouTube

# Where to save
save_path = "../data/game_vod"

# Link of the video to be downloaded
link = "https://www.youtube.com/watch?v=UuEtiwyGSag"

try:
    yt = YouTube(link)
except Exception as e:
    print(f"Connection Error: {e}")

# Select the highest resolution video-only stream
video_stream = yt.streams.filter(progressive=False, file_extension='mp4').order_by('resolution').desc().first()

if video_stream:
    try:
        video_stream.download(save_path)
        print(f'{yt.title} successfully downloaded in highest video quality!')
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No suitable video-only stream found.")
