import sys
from youtube_dl import YoutubeDL, DateRange
from datetime import date, timedelta

if __name__ == '__main__':

    today = date.today()
    before = today - timedelta(days=2)
    datebefore = today.strftime("%Y%m%d")
    dateafter = before.strftime("%Y%m%d")

    if len(sys.argv) > 1:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
            'download_archive' : 'downloadedVideos.txt',
            'daterange': DateRange(dateafter, datebefore),
            'playlistend': 10
        }
        ydl = YoutubeDL(ydl_opts)
        ydl.download(sys.argv[1:])
    else:
        print("Enter list of urls to download")
        exit(0)