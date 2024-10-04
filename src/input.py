import sounddevice as sd
import numpy as np
import soundfile as sf

# Set the duration of each recording chunk in seconds
chunk_duration = 1  # Adjust as needed

# Set the sampling frequency and the number of channels
fs = 44100  # 44.1 kHz sampling frequency
channels = 1  # Stereo input

# Set the threshold for detecting silence (adjust as needed)
silence_threshold = 0.01  # Adjust as needed based on your input levels

# Initialize variables
recording = False
silence_counter = 0
audio_chunks = []

def process_audio(indata, frames, time, status):
    global recording, silence_counter, audio_chunks

    # Calculate the amplitude of the input audio
    amplitude = np.max(np.abs(indata))

    # Check if the amplitude is below the silence threshold
    if amplitude < silence_threshold:
        silence_counter += 1
    else:
        silence_counter = 0  # Reset the silence counter if there's audio input

    # If silence persists for a certain duration, stop recording
    if silence_counter >= int(chunk_duration * fs):
        recording = False

    # Record audio if recording flag is True
    if recording:
        audio_chunks.append(indata.copy())

# Start recording audio from the default input device
with sd.InputStream(samplerate=fs, channels=channels, callback=process_audio):
    print("Recording... Press Ctrl+C to stop recording.")

    # Set recording flag to True
    recording = True

    # Keep recording until recording flag is False
    while recording:
        sd.sleep(100)

# Concatenate recorded audio chunks into a single NumPy array
audio_data = np.concatenate(audio_chunks, axis=0)

# Specify the filename for the output WAV file
output_file = "recorded_audio.wav"

# Write the recorded audio to a WAV file
sf.write(output_file, audio_data, fs)

print(f"Audio recording saved to {output_file}")