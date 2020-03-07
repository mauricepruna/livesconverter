# youtube-video-audio-conversor
Tool to download youtube videos from a channel


## Prequisites:
- Install [python](https://www.python.org/downloads/)
- Install [ffmpeg](https://www.ffmpeg.org/download.html)
- Run the following command `pip install -r requirements.txt` after previous installations are finished
- Modify Config file with proper parameters
- Run `git clone https://github.com/mauricepruna/youtube-video-audio-conversor.git`

**Example**
```properties
[channel_name]
youtube_channel_url = https://www.youtube.com/channel/{CHANNEL_ID}/video
number_days = 1
quality = 128
```

## Run
- `python liveconverter.py`


## Schedule

If you want to create a scheduled execution using a cron job performing `crontab -e` insert similar line to the following: 

Ex. 
```
0 12 * * * cd ~/workspace/youtube-video-audio-conversor && python liveconverter.py && ./bucket_upload.sh
```

previous example will run an execution every day at noon. check logs for completion with `grep CRON /var/log/syslog`   