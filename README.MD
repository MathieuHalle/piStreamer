# Raspberry Pi code Automatic Twitch Streaming

This [project](https://www.cacouletu.com) is a camera placed on a three in our Sugar Shack that displays sap dripping in a collection bucket. We keep the feed running 24/7 for as long as the sugar season continues(2 to 4 weeks).

It will start streaming to the defined twitch channel when you power it. It will also check every 2 minutes the twitch API to see if you are still online. If the stream is offline, the Pi will reboot and restart the stream automatically.

This project is built with a Raspberry Pi 4 Model B and a USB webcam. It could also work with the Raspberry Pi Camera Module.

Pull Requests are always very welcome.

---

## Setup

You need to have the basic piOS image installed on your Raspberry Pi to get this to work. Make sure it's connected to the internet.

- SSH into your Raspberry Pi.
- install FFMPEG ` sudo apt-get -y install ffmpeg`
- install Python `sudo apt-get -y install python3-pip`

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

## The setup

2022 is the 5th year we have installed the project, and over the years, we have used multiple streaming services. First 2 years, we used Facebook Live, Then YouTube, And since last year, we have used [Twitch](https://www.twitch.tv).

Since we now have upload bandwidth to spare (fiber optic internet installed over winter), we might broadcast other nice things in the forest - lost of deers walking around.

![The box](https://www.cacouletu.com/assets/img/box/IMG_0765.jpg)

![Raspberry Pi](https://www.cacouletu.com/assets/img/box/IMG_0768.jpg)

![Webcam and Lights](https://www.cacouletu.com/assets/img/box/IMG_0766.jpg)
