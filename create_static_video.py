from moviepy import *
import os

# Define paths
audio_path = "exports/ethio_jazz_instrumental.wav"
image_path = "exports/cofee1.jpeg"
output_path = "exports/ethiopian_coffee_jazz.mp4"

def create_video():
    print(f"🎬 Creating video from:\n  🎵 Audio: {audio_path}\n  🖼️  Image: {image_path}")
    
    # Check if files exist
    if not os.path.exists(audio_path):
        print(f"❌ Error: Audio file not found at {audio_path}")
        return
    if not os.path.exists(image_path):
        print(f"❌ Error: Image file not found at {image_path}")
        return

    try:
        # Load audio
        audio = AudioFileClip(audio_path)
        print(f"   Audio duration: {audio.duration} seconds")

        # Load image and set duration
        # Resize to something reasonable (HD) to avoid huge file sizes if image is massive
        video = ImageClip(image_path).with_duration(audio.duration)
        
        # Set audio
        video = video.with_audio(audio)
        
        # Write video file
        # Check if we should use a temp audio file (sometimes helps with permission/path issues)
        video.write_videofile(
            output_path, 
            fps=24, 
            codec="libx264", 
            audio_codec="libmp3lame",
            temp_audiofile="temp-audio.mp3",
            remove_temp=True
        )
        
        print(f"\n✅ Video successfully created at: {output_path}")

    except Exception as e:
        print(f"\n❌ Error creating video: {e}")

if __name__ == "__main__":
    create_video()
