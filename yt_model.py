from youtube_transcript_api import YouTubeTranscriptApi

class YTModel():
    ''' The model of the youtube transcription program. '''
    
    def get_transcript(self, video_id):
        ''' Gets the transcript of a youtube video.
        Args:
            video_id: a string representing the id of a youtube video
            
        Returns:
            An array of dictionaries each containing duration, start, and text 
                key pairs that cover the transcription for the youtube video
                identified through video_id. Uses manually created transcript
                if available, otherwise it will use the auto generated one.
        '''
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    
    def get_manually_created_transcript(self, video_id):
        ''' Gets the transcript of a youtube video.
        Args:
            video_id: a string representing the id of a youtube video
            
        Returns:
            An array of dictionaries each containing duration, start, and text 
                key pairs that cover the manually generated transcription for 
                the youtube video identified through video_id. If none exists,
                it will throw an error.
        '''
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        generated = transcript_list.find_manually_created_transcript(['en'])
        return generated.fetch()