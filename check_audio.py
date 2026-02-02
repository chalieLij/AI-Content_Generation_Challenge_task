from moviepy import *
import os

audio_path = "exports/ethio_jazz_instrumental.wav"

def check_audio():
    if not os.path.exists(audio_path):
        print("Audio file missing")
        return

    try:
        audio = AudioFileClip(audio_path)
        print(f"Audio file: {audio_path}")
        print(f"Duration: {audio.duration}")
        print(f"FPS: {audio.fps}")
        print(f"N channels: {audio.nchannels}")
        audio.close()
    except Exception as e:
        print(f"Error reading audio: {e}")

if __name__ == "__main__":
    check_audio()
