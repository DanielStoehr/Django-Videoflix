import subprocess


def convert_480p(source):
    target = source.split('.')[0] + '_480.mp4'
    cmd = f'ffmpeg -i "{source}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target}"'
    subprocess.run(cmd)
