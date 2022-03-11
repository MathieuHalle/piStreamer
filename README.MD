# Raspberry Pi code Automatic Twitch Streaming

This project is a camera placed on a three in our Sugar Shack that displays sap dripping in a collection bucket. We keep the feed running 24/7 for as long as the sugar season continues(2 to 4 weeks).

It will start streaming to the defined twitch channel when you power it. It will also check every 2 minutes the twitch API to see if you are still online. If the stream is offline, the Pi will reboot and restart the stream automatically.

This project is built with a Raspberry Pi 4 Model B and a USB webcam. It could also work with the Raspberry Pi Camera Module.

---

## Setup

You need to have the basic piOS image installed on your Raspberry Pi to get this to work. Make sure it's connected to the internet.

*SSH into your Raspberry Pi.
*install FFMPEG ` sudo apt-get -y install ffmpeg`
\*install Python `sudo apt-get -y install python3-pip`

- Edit `startStream.sh` to add your Twitch stream key.
- Copy `startStream.sh` to `/home/pi/piTube/`
- Add `startStream.sh` to the cron job
- In terminal type `sudo crontab -e`
- Add this entry and the end of the file
- `@reboot /home/pi/piTube/startStream.sh`
- Exit and save.
- Now, you can reboot and see if it works.

If you want to monitor if you are still online:

- Edit `checkLive.py` to add your Twitch API key and secret.
- Copy `checkLive.py` to `/home/pi/piTube/`
- Add `checkLive.py` to the cron job
- In terminal type `sudo crontab -e`
- Add this entry and the end of the file
- `*/3 * * * * /home/pi/piTube/checkLive.py`
- Exit and save.

Voila!

_PS: This is not the best code I have written, but it works for me :)_
