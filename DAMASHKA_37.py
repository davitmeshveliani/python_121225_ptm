class AudioFileMixin:
    """Mixin to provide audio playback functionality."""
    def play_audio(self):
        if not hasattr(self, 'audio_tracks'):
            raise AttributeError(f"error {self.__class__.__name__} not 'audio_tracks'")

        tracks_str = "\n".join(str(track) for track in self.audio_tracks)
        return f"Воспроизведение аудио для {self.__class__.__name__}:\n{tracks_str}"

class VideoFileMixin:
    """Mixin to provide video playback functionality."""
    def play_video(self):
        if not hasattr(self, 'video_files'):
            raise AttributeError(f"error {self.__class__.__name__} not 'video_files'")

        videos_str = "\n".join(map(str, self.video_files))
        return f"Воспроизведение видео для {self.__class__.__name__}:\n{videos_str}"

class MediaPlayer(AudioFileMixin):
    """Device that supports only audio playback."""
    def __init__(self, tracks):
        self.audio_tracks = tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    """Device that supports both audio and video playback."""
    def __init__(self, tracks, videos):
        self.audio_tracks = tracks
        self.video_files = videos

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

player = MediaPlayer(tracks)
print(player.play_audio())


laptop = Laptop(tracks, movies)
print(laptop.play_audio())
print(laptop.play_video())