from pytube import YouTube

class VideoHandler():
    video_url: str = ""
    video_obj: YouTube = None
    
    def __init__(self, url = None):
        self.video_url = url
        
        # TODO: check if inserted text is OK
        if self.video_url != None:
            self.video_obj = YouTube(self.video_url)
    
    def setUrl(self, url):
        self.video_url = url
        self.video_obj = YouTube(url)
    
    def getTitle(self):
        return self.video_obj.title
    
    def getThumbnailPicUrl(self):
        return self.video_obj.thumbnail_url