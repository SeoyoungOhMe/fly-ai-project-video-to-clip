# video-cut.py

from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import math

def download_youtube_video(youtube_url, output_path):
    yt = YouTube(youtube_url)
    yt.streams.filter(file_extension='mp4').first().download(output_path)
    return os.path.join(output_path, f"{yt.title}.mp4")

def cut_video(input_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extract video name without extension
    video_name = os.path.splitext(os.path.basename(input_path))[0]

    # Load video clip
    clip = VideoFileClip(input_path)

    # Get video duration in seconds
    video_duration = clip.duration

    # Cut the video into 1-second segments
    for i in range(math.ceil(video_duration)):
        start_time = i
        end_time = i + 1

        # Ensure end_time does not exceed the video duration
        if end_time > video_duration:
            break

        # Create subclip
        subclip = clip.subclip(start_time, end_time)

        # Generate subclip name with index
        subclip_name = f'{video_name}-{i+1}.mp4'

        # Save subclip to the output folder
        subclip_path = os.path.join(output_folder, subclip_name)
        subclip.write_videofile(subclip_path, codec='libx264', audio_codec='aac')

    print("Video successfully cut into 1-second segments.")

if __name__ == "__main__":
    # Set YouTube video link and output paths
    youtube_url = "https://www.gettyimages.com/detail/video/month-little-white-newborn-boy-is-kicking-his-legs-stock-footage/1382573370?adppopup=true"
    output_video_folder = "saved_video_2"

    # Download YouTube video
    downloaded_video_path = download_youtube_video(youtube_url, "원본동영상")

    # Cut the video into 1-second segments
    cut_video(downloaded_video_path, output_video_folder)
