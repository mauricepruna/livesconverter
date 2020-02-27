import sys
import configparser
from youtube_dl import YoutubeDL, DateRange
from datetime import date, timedelta


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('conf.ini')
    youtube_channel_url = config['DEFAULT']['youtube_channel_url']
    number_days = config['DEFAULT']['number_days']
    quality = config['DEFAULT']['quality']



    if youtube_channel_url and number_days and quality:
        today = date.today()
        before = today - timedelta(days=int(number_days))
        datebefore = today.strftime("%Y%m%d")
        dateafter = before.strftime("%Y%m%d")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality
            }],
            'ignoreerrors':"True",
            'outtmpl': './download/%(title)s-%(upload_date)s.%(ext)s',
            'download_archive' : 'downloadedVideos.txt',
            'daterange': DateRange(dateafter, datebefore),
            'playlistend': 10
        }
        ydl = YoutubeDL(ydl_opts)
        ydl.download([youtube_channel_url])
    else:
        print("Missing one of the configurations needed:\n url:{url} days:{days} quality:{qual} ".format(url=youtube_channel_url, days=number_days, qual=quality))
        exit(0)