# video-cut.py

from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import math

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
    # Set input and output paths
    input_video_path = "baby.mp4"
    output_video_folder = "saved_video"

    # Cut the video into 1-second segments
    cut_video(input_video_path, output_video_folder)
