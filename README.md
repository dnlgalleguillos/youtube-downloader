# Youtube Downloader

![Downloader_Banner](https://github.com/dnlgalleguillos/youtube-downloader/assets/23320192/c161a2b2-d00a-4599-bf8c-8cc772fda8a5)

To create a Python application for downloading YouTube videos on Linux, you can use the pytubefix library, which is a lightweight and easy-to-use library for accessing YouTube videos.

- Linux OS Fedora and Debian with [GNOME Desktop](https://www.gnome.org/)                

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

Install ffmpeg (used to merge the video and audio streams):

```bash
  sudo apt install ffmpeg      # Debian
  sudo dnf install ffmpeg      # Fedora
```

Create a virtual environment and install [pytubefix](https://github.com/JuanBindez/pytubefix) (the maintained fork of pytube, which no longer works with YouTube):

```bash
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
```

Run the script:

```bash
  .venv/bin/python youtube_downloader.py
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

Although [You-Get](https://github.com/soimort/you-get) is a viable option for those who prefer the command line and simplicity of use, those seeking faster downloads may opt for alternatives that can offer higher download speeds.  

```bash
  pip3 install you-get
```
