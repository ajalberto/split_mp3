import os
import csv
import subprocess
import sys
from pathlib import Path


def main(f, tl):
    target_path = ''
    p = Path(f)
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        target_path = str(p.parent)+'/splitted/'
    elif sys.platform.startswith('win32'):
        target_path = str(p.parent) + '\\splitted\\'

    try:
        os.mkdir(target_path)
    except OSError:
        print('Couldn\'t create directory (%s) for storing splitted files.' % target_path)
    else:
        csv.register_dialect('szr', delimiter=';', quoting=csv.QUOTE_NONE)
        with open(tl, newline='') as csvfile:
            reader = csv.reader(csvfile, 'szr')
            next(reader)
            for row in reader:
                split_command = [
                    'ffmpeg', '-i', f,
                    '-acodec', 'copy', '-ss', row[1], '-to', row[2], target_path+row[0].strip(' ')+'.mp3'
                ]
                print(*split_command)
                subprocess.run(split_command, stdout=subprocess.PIPE, stdin=subprocess.PIPE)


if __name__ == '__main__':
    ffmpeg_is_installed = True
    try:
        print(subprocess.check_output(['which', 'ffmpeg']))
    except Exception as e:
        print(e, e.output)
        ffmpeg_is_installed = False
    if not ffmpeg_is_installed:
        print('ffmpeg is needed to run this script. Please install it first, then re-run.')
    else:
        if len(sys.argv) == 3:
            main(sys.argv[1], sys.argv[2])
        else:
            print('Usage: %s file_to_split tracklist' % os.path.relpath(__file__))
