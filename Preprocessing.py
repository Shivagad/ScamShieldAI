from pydub import AudioSegment
from pydub.effects import normalize
import noisereduce as nr
import librosa
import soundfile as sf

# Load and convert to mono
audio = AudioSegment.from_file("harvard.wav").set_channels(1)

# Normalize volume
audio = normalize(audio)

# Export intermediate processed audio
audio.export("normalized_audio.wav", format="wav")

# Load for noise reduction
y, sr = librosa.load("normalized_audio.wav", sr=16000)  # Resample to 16kHz

# Apply noise reduction
y_denoised = nr.reduce_noise(y=y, sr=sr)

# Save final cleaned audio
sf.write("final_audio.wav", y_denoised, sr)
