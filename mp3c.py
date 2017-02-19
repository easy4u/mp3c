#!/usr/bin/env python
"""
Compress mp3 files to frame rate 11025 to reduce file size.

Usage:
- Compress all mp3 files in the current directory
$ mp3c.py *

- Compress sample.mp3 file
$ mp3c.py sample1.mp3 sample2.mp3

Requirements to run the script:
1. ffmpeg
$ brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
2. pydub
$ pip install pydub
"""

import os
import sys
from pydub import AudioSegment
from os import listdir
from os.path import basename
from os.path import isfile, join

def compress_mp3_file(mp3_file_path):
    if (not mp3_file_path.endswith(".mp3")): return

    output_file_path = "c_{}.mp3".format(os.path.splitext(basename(mp3_file_path))[0])
    print "\n Processing {} ==> {}".format(mp3_file_path, output_file_path)

    audio_file = AudioSegment.from_file(mp3_file_path, "mp3")
    frame_rate = audio_file.frame_rate
    bytes_per_sample = audio_file.sample_width

    if (frame_rate == 11025):
        print " frame rate is already 11025, ignore."
        return

    print " frame_rate {} ==> {}".format(frame_rate, "11025")
    audio_file.export(output_file_path, format="mp3", parameters=["-ar", "11025"])


## check arguments and print usage
if (len(sys.argv) < 2 or sys.argv[1] == '?'):
    print "\nUsage:  " + sys.argv[0] + " [mp3_file]\nFor example: mp3c.py song.mp3 \n"
    sys.exit(-1)

mp3_files = [x for x in sys.argv[1:] if x.endswith(".mp3")]
# mp3_files = filter(lambda x: x.endswith(".mp3"), sys.argv[1:])

print "\n Files to precess: {}".format(mp3_files)

for mp3_file in mp3_files:
    compress_mp3_file(mp3_file)

print "\n DONE."
