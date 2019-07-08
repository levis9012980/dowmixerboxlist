import requests
import youtube_dl
import json
import re

class mixerbox:
	def dowload(self, item):
		options = {
            'format': 'bestaudio/best',
			'outtmpl': 'G:\\GitHub\\Downloads\\music\\%(title)s.%(ext)s',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
                'preferredquality': '192'
			}]
		}
		for x in item:
			try:
				url = "http://www.youtube.com/watch?v=" + x["f"]
				with youtube_dl.YoutubeDL(options) as ydl:
					ydl.download([url])
				pass
			except:
				pass
			

	def getHTML(self,vectorId):
		cto = requests.get('http://www.mixerbox.com/service?&callback=jQuery172009174624213601712_1453105380546&appVer=205&funcs=getVector&skip=0&limit=0&locale=zh-tw&mobile=1&type=playlist&vectorId='+vectorId+'&random=8398&_=1453105381259')
		return cto.text

mixerbox = mixerbox()
vectorId = "40361693" # 歌單的編碼 https://www.mixerbox.com/user/40361693
HTML = mixerbox.getHTML(vectorId)
result = re.search(r'\((.+?)\)\;',HTML).group(1)
res = json.loads(result)
item = res["getVector"]["items"]
mixerbox.dowload(item)