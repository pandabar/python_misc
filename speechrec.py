import speech_recognition as sr
r = sr.Recognizer()
file = sr.AudioFile("dst.wav")
print(file)
with file as source:
  r.adjust_for_ambient_noise(source)
  audio = r.record(source)
  result = r.recognize_google(audio,language="es-CL")
  text = open("transcript.txt", "w")
print(result, file= text)
text.close()

