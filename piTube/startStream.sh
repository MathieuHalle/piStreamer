#! /bin/sh

stream_to_twitch() {
    res_input=1920x1080 # input resolution 1280x720 | 920x640 | 
    fps="9" # target FPS
    audio_rate="44100"
    stream_server="live-prg" # see https://stream.twitch.tv/ingests for list
    stream_key="live_XXXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXX" # key will be passed as an argument from the command line

	
### Make sure our capturedive is available
	fuser -k /dev/video0	

### No Audio
	ffmpeg -input_format mjpeg -f v4l2 -s $res_input -r $fps -i /dev/video0 \
		-vf "drawtext=fontfile=/usr/share/fonts/truetype/freefont/FreeSerif.ttf:text='%{localtime}':fontsize=48:x=20:y=20:fontcolor=white: box=1: boxcolor=black@0.75: boxborderw=16" -an \
 		-c:v h264_omx -r $fps -f rtsp -preset veryfast -b:v 6000k -maxrate 6000k -bufsize 6000k  \
		-f flv "rtmp:${stream_server}.twitch.tv/app/${stream_key}" 

}

stream_to_twitch