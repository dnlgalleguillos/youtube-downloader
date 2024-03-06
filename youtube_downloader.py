from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Set the output path for the downloaded video
        output_file = video_stream.download(output_path)

        print(f"Video downloaded successfully: {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_VIDEO_URL' with the actual YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Replace 'YOUR_OUTPUT_PATH' with the desired output path
    output_path = input("Enter the output path (press Enter for the current directory): ")

    if not output_path:
        output_path = '.'

    download_video(video_url, output_path)

