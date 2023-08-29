from pytube import YouTube

# video_obj = YouTube("https://www.youtube.com/watch?v=sc32v7HCnvU")
video_obj = YouTube("https://www.youtube.com/watch?v=ZvI9IRCEIJ4")

# DOWNLOADING

# stream_list = video_obj.streams.filter(only_audio=True)

# for el in stream_list:
#     print(el)

# video_obj.streams.get_by_itag(251).download()

print(video_obj.thumbnail_url)