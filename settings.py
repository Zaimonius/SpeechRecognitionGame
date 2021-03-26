import pyaudio
#tilesize = 48
FPS = 60
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
darkgray = (40, 40, 40)
lightgray = (140, 140, 140)

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 16000  # Record at 16000 samples per second
seconds = 3
filename = "output.wav"

#https://realpython.com/playing-and-recording-sound-python/#recording-audio