# mp3c
Compress mp3 files to reduce their size. By default, the target frame rate will be 11025hz.

Usage:
- Compress all mp3 files in the current directory
```shell
$ mp3c.py *
```

- Compress sample.mp3 file
```shell
$ mp3c.py sample1.mp3 sample2.mp3
```

Requirements to run the script:

- Install [ffmpeg](https://ffmpeg.org/)
```shell
$ brew install ffmpeg --with-libvorbis --with-ffplay --with-theora
```
- Install [pydub](https://github.com/jiaaro/pydub)
```shell
$ pip install pydub
```

