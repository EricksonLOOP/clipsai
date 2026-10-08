# ClipsAI

<!-- [![PyPI version](https://badge.fury.io/py/project-name.svg)](https://badge.fury.io/py/project-name) -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **⚠️ Community-maintained fork**
> This is a fork of the original [ClipsAI/clipsai](https://github.com/ClipsAI/clipsai) project, which was discontinued in January 2024.
> The goal of this fork is to fix incompatibilities with modern dependency versions, close open issues, and continue development.
> Contributions are welcome!

---

## Quickstart

Clips AI is an open-source Python library that automatically converts long videos into
clips. With just a few lines of code, you can segment a video into multiple clips and
resize its aspect ratio from 16:9 to 9:16.

> **Note:** Clips AI is designed for audio-centric, narrative-based videos such as
podcasts, interviews, speeches, and sermons. It actively employs video transcripts to
identify and create clips. Our resizing algorithm dynamically reframes and focuses on
the current speaker, converting the video into various aspect ratios.

### Installation

1. Install Python dependencies.  
   *We highly suggest using a virtual environment (such as [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)) to avoid dependency conflicts.*

    ```bash
    pip install -e .
    ```

    Install WhisperX separately (not available on PyPI):

    ```bash
    pip install "whisperx @ git+https://github.com/m-bain/whisperx.git@v3.1.1"
    ```

    Or install all pinned dependencies at once:

    ```bash
    pip install -r requirements.txt
    pip install "whisperx @ git+https://github.com/m-bain/whisperx.git@v3.1.1"
    ```

2. Install [libmagic](https://github.com/ahupp/python-magic?tab=readme-ov-file#debianubuntu)

3. Install [ffmpeg](https://github.com/kkroening/ffmpeg-python/tree/master?tab=readme-ov-file#installing-ffmpeg)

### Creating clips

Since clips are found using the video's transcript, the video must first be transcribed. Transcribing is done with [WhisperX](https://github.com/m-bain/whisperX), an open-source wrapper on [Whisper](https://github.com/openai/whisper) with additional functionality for detecting start and stop times for each word.

```python
from clipsai import ClipFinder, Transcriber

transcriber = Transcriber()
transcription = transcriber.transcribe(audio_file_path="/abs/path/to/video.mp4")

clipfinder = ClipFinder()
clips = clipfinder.find_clips(transcription=transcription)

print("StartTime: ", clips[0].start_time)
print("EndTime: ", clips[0].end_time)
```

### Resizing a video

A HuggingFace access token is required to resize a video since [Pyannote](https://github.com/pyannote/pyannote-audio) is used for speaker diarization. You won't be charged for using Pyannote — instructions are on the [Pyannote HuggingFace page](https://huggingface.co/pyannote/speaker-diarization-3.1#requirements).

It is recommended to pass the token via environment variable instead of hardcoding it:

```bash
export HF_AUTH_TOKEN="hf_..."
```

```python
import os
from clipsai import resize

crops = resize(
    video_file_path="/abs/path/to/video.mp4",
    pyannote_auth_token=os.environ["HF_AUTH_TOKEN"],
    aspect_ratio=(9, 16)
)

print("Crops: ", crops.segments)
```

---

## Changes in this fork

| Area | Change |
|------|--------|
| `pyannote.audio` 4.x | Renamed `use_auth_token` → `token` in `PyannoteDiarizer` |
| `texttiler.py` | Replaced `eval()` with `getattr()` (safer) |
| `setup.py` | Moved `pytest` from `install_requires` to `extras_require[dev]` |
| `requirements.txt` | Pinned dependency versions for reproducibility |
| CI | GitHub Actions pipeline with lint (flake8 + black) and tests on Python 3.10/3.11 |
| Security | Removed HuggingFace token from sandbox notebooks |

---

## Contributing

Issues and pull requests are welcome. Before opening a PR, make sure the tests pass:

```bash
pip install -e ".[dev]"
pytest tests/ -v
```
