import os
import shutil
import subprocess
import tempfile

from pytubefix import YouTube


def download_video(url, output_path='.'):
    try:
        if shutil.which('ffmpeg') is None:
            raise RuntimeError("ffmpeg is not installed (sudo apt install ffmpeg)")

        # Create a YouTube object
        yt = YouTube(url)
        print(f"Title: {yt.title}")

        # YouTube now serves video and audio as separate streams,
        # so take the best of each and merge them with ffmpeg.
        video_stream = (
            yt.streams.filter(adaptive=True, only_video=True, file_extension='mp4')
            .order_by('resolution')
            .desc()
            .first()
        )
        audio_stream = yt.streams.get_audio_only()  # best m4a audio

        if video_stream is None or audio_stream is None:
            raise RuntimeError("No downloadable video/audio streams found")

        print(f"Video: {video_stream.resolution} | Audio: {audio_stream.abr}")

        os.makedirs(output_path, exist_ok=True)
        output_file = os.path.join(os.path.abspath(output_path), video_stream.default_filename)

        with tempfile.TemporaryDirectory(dir=output_path) as tmp:
            print("Downloading video...")
            video_file = video_stream.download(output_path=tmp, filename='video.mp4')
            print("Downloading audio...")
            audio_file = audio_stream.download(output_path=tmp, filename='audio.m4a')

            print("Merging video and audio...")
            subprocess.run(
                ['ffmpeg', '-y', '-loglevel', 'error',
                 '-i', video_file, '-i', audio_file,
                 '-c', 'copy', output_file],
                check=True,
            )

        print(f"Video downloaded successfully: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")

    output_path = input("Enter the output path (press Enter for the current directory): ")

    if not output_path:
        output_path = '.'

    download_video(video_url, os.path.expanduser(output_path))
