from yt_model import YTModel
from yt_view import YTView

class YTController():
    ''' The controller for the youtube transcription program.
    
    Attributes:
        model: an instance of a YTModel object that represents the model of the 
            youtube transcription program.
        view: an instance of the YTView object which represents the view of the 
            youtube transcription program.
    '''
    
    def __init__(self):
        self.model = YTModel()
        self.view = YTView()
    
    def start_program(self):
        ''' Starts the youtube transcription program. '''
        self.view.introduction()
        video_id = self.view.get_youtube_id()
        transcript = self.model.get_manually_created_transcript(video_id)
        self.view.print_transcript(transcript)
            
if __name__ == "__main__":
    controller = YTController()
    controller.start_program()