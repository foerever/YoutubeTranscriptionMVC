from pprint import pprint
from urllib.parse import urlparse
from urllib.parse import parse_qs

class YTView():
    ''' The view of the youtube transcription program. '''
    
    def introduction(self):
        ''' Prints the introduction to the youtube transcription service. ''' 
        print("Welcome to Youtube Translation Service!")

    def get_youtube_id(self):
        ''' Gets the youtube id from the user. ''' 
        video_url = input("Please enter the Youtube URL you wish to transcribe:\n")
        video_id = self.parse_id(video_url)
        # This is what a ternary operator looks like in Python!
        # Ternator operators reduce simple if else statements that normally
        # would take up 4 lines down to 1 line. You can think of it like this:
        # return <THIS> if <THIS> exists else <REPEAT THIS FUNCTION>
        # Ternary operators are very useful for functional programming but in 
        # general can be a stylistically cleaner way of writing code.
        return video_id if video_id else self.get_youtube_id()
    
    def parse_id(self, url):
        ''' Parses the id of a video given a valid youtube url.
        Args:
            url: a string representing a valid youtube url.
            
        Returns:
            A string representing the video id of a valid youtube
                video from the input url.
        '''
        url_data = urlparse(url)
        query = parse_qs(url_data.query)
        return query['v'][0]
    
    def print_transcript(self, transcript):
        ''' Pretty prints the transcript
        Args:
            transcript: an array of dictionaries representing the transcript
                of a youtube video.
        '''
        pprint(transcript)