# Youtube to MP3/MP4 Downloader:
*Roux Institute at Northeastern; CS5001: Intensive Foundations of CS; Fall 2023 Final Project.*<br>

Download some of your favorite YouTube videos as mp3 or mp4 files! You can even download multiple URLs at the same time. <br>

UPDATE 12/15: The mp4 downloading option became available.

## Features
* Safe, secure, and fast downloads. *NOTE: This does not work on live videos*
* Options to paste URL directly, extract multiple URLs at the same time from an external file, or run a test URL.
* Can handle downloads even for videos over 3 hours long.
    * It can actually handle videos of any length, but longer videos take much longer to download.
* Audio quality/bitrate set to 128kbps, but can be manually changed within the code using the optional parameters.
    * NOTE: Increasing audio quality may also increase download time.
* Default mp3 file name set to `ytmp3_file.mp3`, but can be manually changed within the code using the optional parameters. Default mp4 file name is `ytmp4_file.mp4`
* All mp4 downloads set to highest resolution.

## Necessary Installations
The following packages are all required for this program's implementation. Documentation and instructions for installing each package can be found below:<br>

### `Python3`
1. Please ensure that python 3.6+ is installed in your system. Documentation and instructions for installation can be found [here](https://www.python.org/downloads/)

### `pytube3`
1. This is a Python library used for downloading videos from the web.
2. To check if you already have this installed, try entering `pip show pytube3` (you may need to use `pip3` if you are a Mac or Homebrew user) in your terminal.
3. Documentation for `pytube3` can be found [here](https://pypi.org/project/pytube3/). Installation instructions are also included.
4. NOTE: Some people have been known to come across a confusing error `HTTP Error 410: Gone`. A way to debug it has been found [here](https://github.com/pytube/pytube/issues/1076). You can also try upgrading your Pytube3 if you haven't already. You can try `python -m pip install --upgrade pytube`.

### `MoviePy`
1. This is a Python library used for video editing
2. To check if you already have this installed, try entering `pip show moviePy` (you may need to use `pip3` if you are a Mac or Homebrew user) in your terminal.
3. Documentation for `moviePy` can be found [here](https://pypi.org/project/moviepy/). Installation instructions are included.

### `FFmpeg`
1. This is a free and open-source software that consists of libraries and tools designed to handle multimedia files such as videos, audio files, and images. Many applications depend on it.
2. To check if you already have this installed, try entering `ffmpeg -version` in your terminal.
3. Documentation for `ffmpeg` can be found [here](https://ffmpeg.org/ffmpeg.html).
4. Installation instructions for `ffmpeg` can be found [here](https://www.bannerbear.com/blog/how-to-install-ffmpeg-on-mac-windows-and-ubuntu-linux-step-by-step/).
    * NOTE: If you have a Mac, it is considerably easier to use the homebrew method.

### `Homebrew` *(for those downloading FFmpeg via the homebrew method)*
1. This is a package managing software that makes it easier for MacOS users to access open source community resources (such as `ffmpeg`).
2. To check if you already have this installed, try entering `brew --version` into your terminal.
3. Documentation and installation instructions can be found [here](https://brew.sh). If more help is needed, here is an additional [instructional video](https://www.youtube.com/watch?v=IWJKRmFLn-g).

## Instructions for Use
1. Run program `main.py`.
2. Decide if you wish to paste a youtube URL manually (option 1), upload a file of URLs by (option 2), running the provided test URL by (option 3), or exiting the program (option 4)
    * If option 1 is chosen (entering 1 into the terminal), paste your URL into the terminal when prompted. Option 1 is also the default option should anything other than 1, 2, 3, or 4 be chosen. From there, you will choose whether you want mp4 or mp3 files (4 for mp4, or any other key for mp3).
    * If option 2 is chosen, then user will be prompted to enter the proper filepath. Alternatively, you can also paste your URLs into `url_list.txt` and use that as your file. Three URLs have already been added to `url_list.txt` as an example. From there, you will choose whether you want mp4 or mp3 files.
        * For every URL in your file, mp3/mp4 files with the names `ytmp3_file.mp3/4`, `ytmp3_file.mp3/4#`, `ytmp3_file.mp3/4##`...etc. will show up in your directory.
        * NOTE: Please make sure your url files consist of *only* URLs. Extra line returns will be accounted for, but any invalid URLs will raise an error message.
    * If option 3 is chosen, program will run the program with the test URL. Choose whether you want an mp3 or an mp4 file. A `test_url` file will appear in the same directory upon completion.
    * If option 4 is chosen, the program will end there.
3. Program will run as intended, and upon completion, the new mp3 or mp4 file(s) will appear in the same directory.
4. Enjoy your downloads!
#### <u>Optional: Changing the audio bitrate and filenames</u>
To change the audio bitrate or the names of your mp3 files, go into the `main()` of the `yt2mp3.py` file. Every time you see the `download_and_convert()` function being called, you may add the optional parameters. Both additional parameters must be `strings`. For example, if you wanted to change your audio bitrate to 256kbps, you would use `bitrate="256k"` as an argument.

## Fair Use Policy
Please keep in mind that downloading certain YouTube videos might violate YouTube's terms of service, so make sure you comply with their policies. Additionally, the legality of converting YouTube videos to MP3 may vary depending on your location, so be sure to consider local laws and regulations. YouTube's terms of service can be found at the link [here](https://www.youtube.com/static?template=terms).