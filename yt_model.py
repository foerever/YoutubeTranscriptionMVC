from youtube_transcript_api import YouTubeTranscriptApi

class YTModel():
    
    def get_transcript(self, video_id):
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    
    def get_manually_created_transcript(self, video_id):
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        generated = transcript_list.find_manually_created_transcript(['en'])
        return generated.fetch()