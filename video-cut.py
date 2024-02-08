import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# 원본동영상 : 엑셀 2~48까지 다운로드
# 코드 설명 : "원본동영상" 폴더에 있는 동영상들을 1초 간격의 클립으로 "클립동영상" 폴더에 저장함.

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
    for i in range(int(video_duration)):
        start_time = i
        end_time = i + 1

        # Create subclip
        subclip = clip.subclip(start_time, end_time)

        # Generate subclip name with index
        subclip_name = f'{video_name}-{i+1}.mp4'

        # Save subclip to the output folder
        subclip_path = os.path.join(output_folder, subclip_name)
        subclip.write_videofile(subclip_path, codec='libx264', audio_codec='aac')

    print(f"{video_name}: Video successfully cut into 1-second segments.")

if __name__ == "__main__":
    # Set input and output paths
    original_videos_folder = "원본동영상"
    output_clips_folder = "클립동영상"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_clips_folder):
        os.makedirs(output_clips_folder)

    # Iterate through each video in the original folder
    for video_file in os.listdir(original_videos_folder):
        if video_file.endswith(".mp4"):
            # Set input path for each video
            video_path = os.path.join(original_videos_folder, video_file)

            # Cut the video into 1-second segments and save to the output folder
            cut_video(video_path, output_clips_folder)
