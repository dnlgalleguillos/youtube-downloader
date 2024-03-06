# Youtube Downloader
To create a Python application for downloading YouTube videos on Linux, you can use the pytube library, which is a lightweight and easy-to-use library for accessing YouTube videos.

- OS Fedora and Debian with GNOME Desktop

Here are the steps to create a simple YouTube video downloader app:
Before you go any further, make sure you have Python and that the expected version is available from your command line. You can check this by running:

```bash
  python3 --version
```

Additionally, you’ll need to make sure you have pip available. You can check this by running:

```bash
  python3 -m pip --version
```

If pip isn’t already installed, then first try to bootstrap it from the standard library:

```bash
  python3 -m ensurepip --default-pip
```

While pip alone is sufficient to install from pre-built binary archives, up to date copies of the setuptools and wheel projects are useful to ensure you can also install from source archives:

```bash
  python3 -m pip install --upgrade pip setuptools wheel
```

Install the pytube library:

```bash
  pip install pytube
```

Create a Python script (youtube_downloader.py) with the following code:

```bash
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
```
Run the script:

```bash
  python youtube_downloader.py
```
Enter the YouTube video URL when prompted, and press Enter.

Optionally, enter the output path where you want to save the downloaded video. Press Enter to use the current directory as the output path.

```bash
  Enter the YouTube video URL: https://www.youtube.com/watch?v=5NgNicANyqM&t=25459s
```
Enter the output path

```bash
  Enter the output path (press Enter for the current directory):
```
This is great for downloading a video of more than 11 hours of study.

```bash
  Video downloaded successfully: /home/daniel/Videos/./Harvard CS50’s Artificial Intelligence with Python – Full University Course.mp4
```
This is a basic example, and you may want to add more features, such as downloading specific video resolutions or creating a simple GUI for a better user experience. Keep in mind that downloading YouTube videos may violate YouTube's terms of service, so make sure to use this script responsibly and in compliance with YouTube's policies.
