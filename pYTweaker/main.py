from pytube import YouTube
import pytube

import requests
import json

# video_obj = YouTube("https://www.youtube.com/watch?v=sc32v7HCnvU")
# video_obj = YouTube("https://www.youtube.com/watch?v=ZvI9IRCEIJ4")
# video_obj = YouTube("https://www.youtube.com/watch?v=WnEw4f_nwPw")

# # DOWNLOADING

# stream_list = video_obj.streams

# for el in stream_list:
#     print(el)

# video_obj.streams.get_by_itag(244).download(filename="video_1.webm")
# video_obj.streams.get_by_itag(251).download(filename="audio_1.ogg")

# print(video_obj.thumbnail_url)

# lista = pytube.Search("klawiter").results

# for el in lista:
#     print(el.title)
    
# url = "https://www.youtube.com/watch?v=psUK-vctrU"
# response = requests.get(url)

# response_text = response.text

# it = response_text.find("playabilityStatus")

# INFO: regex
# "playabilityStatus":\{"status":"ERROR",


#############################
# DOWNLOADing YT video
#############################

url = "https://www.youtube.com/watch?v=FfTrRwxRP08"
video_obj = YouTube(url)

stream_list = video_obj.streams

for el in stream_list:
    print("TYPE:", type(el), "| DATA:", str(el))
    
# video_obj.streams.get_by_itag(248).download(filename="video_1.webm")
# video_obj.streams.get_by_itag(251).download(filename="audio_1.ogg")