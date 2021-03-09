#!/bin/bash
# bash -v <(curl -sL https://raw.githubusercontent.com/nrobinson2000/vr-sentry/master/app/install.sh)

# Install git and pip3
sudo apt update
sudo apt install -y git python3-pip vim motion python3-pantilthat
sudo apt install python3-flask python3-picamera

# Clone the git repository
git clone https://github.com/nrobinson2000/vr-sentry
cd vr-sentry/cli/

# Install python dependencies
sudo pip3 install -r requirements.txt

# OLD COMMANDS:

# Install udev file to allow non-root access to the USB device
sudo cp 99-sentry.rules /etc/udev/rules.d/

# sudo vim /etc/default/motion
# Change the line to:

# start_motion_daemon=yes


# sudo vim /etc/motion/motion.conf 
# Change the following settings:

# daemon on
# flip_axis h
# width 640
# height 480
# framerate 30
# threshold 1000
# ffmpeg_output_movies off
# stream_quality 90
# stream_motion on
# stream_maxrate 30
# stream_localhost off
