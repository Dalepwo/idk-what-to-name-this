from moviepy import VideoFileClip

def play_video_with_audio(video_path):
    clip = VideoFileClip(video_path)
    clip.preview()  # Plays the video with audio
    clip.close()

# Paths to the video files
file1 = "goofyahh.mp4"
file2 = "goofballs.mp4"

# Play videos sequentially
play_video_with_audio(file1)
play_video_with_audio(file2)
