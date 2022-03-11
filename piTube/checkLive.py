#!/usr/bin/python3

import requests
import os
from datetime import datetime

client_id = '013o46uyxraolj1_xxxxxxxxxxxxxxxx'
client_secret = '0jwdv3j1au6z9kvq_xxxxxxxxxxxxxxxx'
streamer_name = 'the_user_name_you_want_to_monitor'
nowDate = datetime.now()
nowStr = nowDate.strftime("%Y/%m/%d %H:%M:%S")

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

# data output
keys = r.json()

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

stream = requests.get(
    'https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

stream_data = stream.json()

if len(stream_data['data']) == 1:
    with open("/home/pi/piTube/log/piTubeChecklive.log", "a") as piTubeCheckliveLog:
        piTubeCheckliveLog.write(nowStr + ": Stream is live\n")

else:
    with open("/home/pi/piTube/log/piTubeChecklive.log", "a") as piTubeCheckliveLog:
        piTubeCheckliveLog.write(nowStr + ": Stream is offline\n")
    os.system("reboot now")
