# bundletool-ui
v1.0.1

A user interface that makes working with Google's Bundletool easy. <br>
Allows you to create APKs or universal APK from app's Android App <br>
Bundle file (.aab) <br>

## Requirements
- Python 3.8 or newer, you can download it from https://www.python.org/downloads/
- Google's Bundletool 1.3.0 or newer, you can download it from https://developer.android.com/studio/command-line/bundletool

## How to run
- First open `api/settings.py` and change the `DEFAULT_SETTINGS`'s `bundletool_path` property to the path where
  you installed Bundletool
- Like this: `{'bundletool_path': r'path:\to\bundletool'}`
- Note: Don't forget to have the `r` in front of the path string because it is required for Python
- Then open your terminal and type: `python main.py` or `python3 main.py` (on Mac) in bundletool-ui folder

## Run from any directory
- For instructions on how to run `bundletool.py` from any directory
take a look at these StackOverflow answers:
- <a href="https://stackoverflow.com/a/48730548/13646430">Windows</a>
- <a href="https://stackoverflow.com/a/57205929/13646430">Linux & Mac</a>

This project was created by Andrej Vujić <br>
on November 30th, 2020

Copyright © 2020-2021 Andrej Vujić
