import wave
import numpy as np
import pyopenjtalk
import simpleaudio as sa

# Define the audio parameters
sample_rate = 44100  # Sample rate in Hz
duration = 5  # Duration of the audio in seconds
frequency = 440  # Frequency of the audio in Hz

# Generate a sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
audio_data = np.sin(2 * np.pi * frequency * t)
print(audio_data.shape[1] if audio_data.ndim > 1 else 1)
print(audio_data.dtype.itemsize)
print(sample_rate)
print(len(audio_data))
print(audio_data.dtype)

audio_data, sample_rate = pyopenjtalk.tts("初めまして、花と申します。 私はあなたに教えようとします、そしてあなたが素晴らしい一日を過ごせることを願っています", speed=0.9)
print(audio_data.shape[1] if audio_data.ndim > 1 else 1)
print(audio_data.dtype.itemsize)
print(sample_rate)
print(len(audio_data))
print(audio_data.dtype)

# Scale the audio data to 16-bit integers (-32768 to 32767)
# scaled_data = np.int8(audio_data * 127)
max_abs = np.max(np.abs(audio_data))
normalized_data = audio_data / max_abs if max_abs != 0 else audio_data
scaled_data = np.int16(normalized_data * 32767)
# scaled_data = np.int32(audio_data * 8388607)
# scaled_data = np.int32(audio_data * 2147483647)

po = sa.play_buffer(scaled_data, 1, 2, sample_rate)
po.wait_done()

# Open a WAV file for writing
with wave.open('output.wav', 'w') as wav_file:
    # Set the parameters of the WAV file
    wav_file.setparams((1, 2, sample_rate, len(scaled_data), 'NONE', 'not compressed'))
    
    # Write the audio data to the WAV file
    wav_file.writeframes(scaled_data.tobytes())