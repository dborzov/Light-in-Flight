#!/bin/bash
ffmpeg -f image2 -r 5 -i slowlight/video_U/%d.png -vcodec mpeg4 -y slowlight/movie_U.avi -s 1920x1080
