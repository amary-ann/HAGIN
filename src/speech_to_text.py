import subprocess
import io
from google.oauth2 import service_account
from google.cloud import speech

class SpeechToText:
    def __init__(self, video_file, audio_file, client_file):
        self.video_file = video_file
        self.audio_file = audio_file
        self.client_file = client_file
        self.credentials = service_account.Credentials.from_service_account_file(self.client_file)
        self.client = speech.SpeechClient(credentials=self.credentials)

    def extract_audio(self):
        """Extract audio from the video file using FFmpeg."""
        command = f'ffmpeg -i {self.video_file} -ab 160k -ar 44100 -vn {self.audio_file}'
        subprocess.call(command, shell=True)

    def perform_speech_to_text(self):
        """Perform speech-to-text operation on the extracted audio file."""
        with io.open(self.audio_file, 'rb') as f:
            content = f.read()
            audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='en-US',
            audio_channel_count=2,
        )

        # Perform speech-to-text
        response = self.client.recognize(config=config, audio=audio)
        
        # Collect transcriptions
        transcripts = []
        for result in response.results:
            transcripts.append(result.alternatives[0].transcript)

        return transcripts

if __name__ == "__main__":
    # Initialize the SpeechToText object
    video_file = "video_file.mp4"  # Replace with your video file path
    audio_file = "audio_file.wav"  # Replace with your desired audio file path
    client_file = "sa_speechdemo.json"  # Replace with your service account JSON file path

    stt = SpeechToText(video_file, audio_file, client_file)

    # Extract audio from video
    print("Extracting audio...")
    stt.extract_audio()
    print("Audio extraction complete.")

    # Perform speech-to-text
    print("Performing speech-to-text...")
    transcripts = stt.perform_speech_to_text()
    print("Transcription complete.")

    # Print the results
    print("Transcripts:")
    for transcript in transcripts:
        print(transcript)
