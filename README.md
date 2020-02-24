# youtube-video-audio-conversor
Tool to download youtube videos from a channel


## Prequisites:
- Install [python](https://www.python.org/downloads/)
- Install [ffmpeg](https://www.ffmpeg.org/download.html)
- Run the following command `pip install -r requirements.txt` after previous installations are finished
- Modify Config file with proper parameters
**Example**
```properties
[DEFAULT]
youtube_channel_url = https://www.youtube.com/channel/{CHANNEL_ID}/video
number_days = 1
quality = 128
```

## Run
- `python liveconverter.py`

