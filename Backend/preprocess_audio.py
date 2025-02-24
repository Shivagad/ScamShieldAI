import librosa
import noisereduce as nr
import soundfile as sf

def preprocess_audio(audio_path, output_path="cleaned_audio.wav"):
    """Loads an audio file, reduces noise, and saves the cleaned version."""
    audio_data, sr = librosa.load(audio_path, sr=None)
    
    # Identify noise from the first second
    noise_sample = audio_data[: int(sr * 1)]
    
    # Reduce background noise
    reduced_noise_audio = nr.reduce_noise(y=audio_data, sr=sr, y_noise=noise_sample)
    
    # Save the processed file
    sf.write(output_path, reduced_noise_audio, sr)
    
    return output_path  # Return the cleaned audio file path
