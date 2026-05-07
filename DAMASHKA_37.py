class AudioFileMixin:
    """Mixin to provide audio playback functionality."""
    def play_audio(self):
        """
                Returns a formatted string of audio tracks.

                Raises:
                    AttributeError: If the object does not have an 'audio_tracks' field.
                """
        if not hasattr(self, 'audio_tracks'):
            raise AttributeError(f"error {self.__class__.__name__} not 'audio_tracks'")
        result = f"Воспроизведение аудио для {self.__class__.__name__}:"
        for track in self.audio_tracks:
            result += f"\n{track}"
        return result


class VideoFileMixin:
    """Mixin to provide video playback functionality."""
    def play_video(self):
        """
                Returns a formatted string of video files.

                Raises:
                    AttributeError: If the object does not have a 'video_files' field.
                """
        if not hasattr(self, 'video_files'):
            raise AttributeError(f"error {self.__class__.__name__} not 'video_files'")

        result = f"Воспроизведение видео для {self.__class__.__name__}:"
        for video in self.video_files:
            result += f"\n{video}"
        return result

class MediaPlayer(AudioFileMixin):
    """Device that supports only audio playback."""
    def __init__(self, tracks):
        """Initialize with a list of audio tracks."""
        self.audio_tracks = tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    """Device that supports both audio and video playback."""
    def __init__(self, tracks, videos):
        """Initialize with lists of tracks and video files."""
        self.audio_tracks = tracks
        self.video_files = videos


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

player = MediaPlayer(tracks)
print(player.play_audio())

laptop = Laptop(tracks, movies)
print(laptop.play_audio())
print(laptop.play_video())
print(Laptop.__mro__)
