import ffmpeg

# video_stream = ffmpeg.input("Hackowanie vs Sztuczna Inteligencja.mp4")
# audio_stream = ffmpeg.input("Hackowanie vs Sztuczna Inteligencja.webm")

# ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()

# video = ffmpeg.input("Hackowanie vs Sztuczna Inteligencja.mp4")
# audio = ffmpeg.input('Hackowanie vs Sztuczna Inteligencja.webm')

video = ffmpeg.input("video_1.webm")
audio = ffmpeg.input("audio_1.ogg")


stream = ffmpeg.output(video, audio, "Jak stracić wszystko klikając w reklamę.mp4", vcodec="copy", acodec="copy")

stream.run()