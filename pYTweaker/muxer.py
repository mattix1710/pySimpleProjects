import ffmpeg

video_stream = ffmpeg.input("Hackowanie vs Sztuczna Inteligencja.mp4")
audio_stream = ffmpeg.input("Hackowanie vs Sztuczna Inteligencja.webm")

ffmpeg.output(audio_stream, video_stream, 'out.mp4').run()