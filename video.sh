#!/bin/bash
ffmpeg -f image2 -r 8 -i video/%d.png -vcodec mpeg4 -y movie.mp4
