from pytubefix import YouTube
from pytubefix.cli import on_progress

class YouTubeAudioDownloader:
    def __init__(self, url, save_path):
        """
        Initializes the downloader with the video URL and save path.

        Args:
            url (str): The URL of the YouTube video.
            save_path (str): The directory where the audio file will be saved.
        """
        self.url = url
        self.save_path = save_path

    def display_video_title(self):
        """
        Fetches and displays the title of the YouTube video.

        Returns:
            str: The title of the YouTube video.
        """
        self.yt = YouTube(self.url, on_progress_callback=on_progress)
        print(f"Video Title: {self.yt.title}")
        return self.yt.title

    def download_audio(self):
        """
        Downloads the audio stream of the YouTube video.
        """
        # Filter streams to only audio
        audio_stream = self.yt.streams.filter(only_audio=True).first()

        # Download the audio stream as an MP3 file
        audio_stream.download(self.save_path, mp3=True)
        print(f"Audio downloaded successfully to {self.save_path}")

if __name__ == "__main__":
    # Define the video URL and save path
    VIDEO_URL = "URL"  # Replace with the YouTube video URL
    SAVE_PATH = "audio/"  # Directory to save the audio

    # Initialize the downloader
    downloader = YouTubeAudioDownloader(VIDEO_URL, SAVE_PATH)

    # Display the video title
    downloader.display_video_title()

    # Download the audio
    downloader.download_audio()
