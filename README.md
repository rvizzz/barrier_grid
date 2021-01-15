Create barrier grid animations

Demo: https://twitter.com/r_vizzz/status/1314232479604256771

    usage: barrier_grid.py [-h] [-w W] [-f F] [-s S] [-t T] video_file

    positional arguments:
      video_file  video file to make an animation of

    optional arguments:
      -h, --help  show this help message and exit
      -w W        width in pixels of the vertical slices from the video frame
      -f F        number of frames from the input video (should be small (~4))
      -s S        number of frames to skip after writing a frame from the video
                  file
      -t T        width in pixels that will be transparent in the transparency
                  print out
