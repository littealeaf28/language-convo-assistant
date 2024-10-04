import whisper
import datetime

model = whisper.load_model("base")

audio = whisper.load_audio("output.wav")
audio = whisper.pad_or_trim(audio)

# _, probs = model.detect_language(mel)
# print(f"Detected language {max(probs, key=probs.get)}")

# decode the audio

start = datetime.datetime.now()
options = whisper.DecodingOptions()
result = whisper.decode(model, whisper.log_mel_spectrogram(audio).to(model.device), options)
stop = datetime.datetime.now()

# print the recognized text
print(result.text)
print(stop - start)

audio = whisper.load_audio("output.2.wav")
audio = whisper.pad_or_trim(audio)

start = datetime.datetime.now()
options = whisper.DecodingOptions()
result = whisper.decode(model, whisper.log_mel_spectrogram(audio).to(model.device), options)
stop = datetime.datetime.now()

# print the recognized text
print(result.text)
print(stop - start)