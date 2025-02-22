import librosa
import noisereduce as nr
import soundfile as sf

# Step 1: Load the audio file
audio_data, sr = librosa.load('audio.mp3', sr=None)

# Step 2: Identify a noise-only segment (e.g., first second)
noise_sample = audio_data[0:int(sr * 1)]  # Adjust based on your file

# Step 3: Reduce background noise
reduced_noise_audio = nr.reduce_noise(y=audio_data, sr=sr, y_noise=noise_sample)

# Step 4: Save the cleaned audio file
sf.write('output_clean_audio.wav', reduced_noise_audio, sr)

print("Noise reduction complete. Processed audio saved as 'output_clean_audio.wav'.")