# split_mp3

Simple python script for splitting mix mp3 files to separate tracks based on a tracklist csv.

Sample csv can be found in repo.

It requires ffmpeg to run.

python3 main.py file_to_split.mp3 tracklist.csv

The script will create a folder called 'splitted' in the directory where the original mp3 can be find, and puts the tracks in it.