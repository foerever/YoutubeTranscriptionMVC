from yt_model import YTModel
from yt_view import YTView

class YTController():
    
    def __init__(self):
        self.model = YTModel()
        self.view = YTView()
    
    def start_program(self):
        self.view.introduction()
        video_id = self.view.get_youtube_id()
        transcript = self.model.get_manually_created_transcript(video_id)
        self.view.print_transcript(transcript)
            
if __name__ == "__main__":
    controller = YTController()
    controller.start_program()