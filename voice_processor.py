import os
from pydub import AudioSegment

class VoiceProcessor:
    @staticmethod
    def convert_to_wav(audio_file_path):
        """Convert audio file to WAV format"""
        try:
            if audio_file_path.endswith(('.mp3', '.m4a', '.ogg')):
                audio = AudioSegment.from_file(audio_file_path)
                wav_path = audio_file_path.rsplit('.', 1)[0] + '.wav'
                audio.export(wav_path, format='wav')
                return wav_path
            return audio_file_path
        except Exception as e:
            print(f"Audio conversion error: {e}")
            print("Note: ffmpeg is required for audio conversion. Please ensure it is installed and in your PATH.")
            return audio_file_path
    
    @staticmethod
    def get_audio_duration(audio_file_path):
        """Get duration of audio file in seconds"""
        try:
            audio = AudioSegment.from_file(audio_file_path)
            return len(audio) / 1000.0  # Convert to seconds
        except:
            return 0