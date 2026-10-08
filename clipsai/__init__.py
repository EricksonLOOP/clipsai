# Functions
from .clip.clipfinder import ClipFinder
from .media.audio_file import AudioFile
from .media.audiovideo_file import AudioVideoFile
from .media.editor import MediaEditor
from .media.video_file import VideoFile
from .transcribe.transcriber import Transcriber

# Types
from .clip.clip import Clip
from .resize.crops import Crops
from .resize.segment import Segment
from .transcribe.transcription import Transcription
from .transcribe.transcription_element import Sentence, Word, Character


def resize(*args, **kwargs):
    """Lazily import and call resize to avoid eager pyannote/torchaudio import."""
    from .resize.resize import resize as _resize
    return _resize(*args, **kwargs)

__all__ = [
    "AudioFile",
    "AudioVideoFile",
    "Character",
    "ClipFinder",
    "Clip",
    "Crops",
    "MediaEditor",
    "Segment",
    "Sentence",
    "Transcriber",
    "Transcription",
    "VideoFile",
    "Word",
    "resize",
]
