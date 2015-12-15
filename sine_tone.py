"""Play a fixed frequency sound."""
from __future__ import division
import math
import pyaudio

def sine_tone(frequency, duration, volume=1, sample_rate=22050):

    n_samples = int(round(sample_rate * duration))
    restframes = n_samples % sample_rate

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))
    stream.write(bytes(bytearray(samples)))
    for buf in zip(*[samples]*sample_rate): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()


def playScale(scale):
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2 
    RATE = 44100 #sample rate
    RECORD_SECONDS = 17 
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK) #buffer

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        for x in scale:
            print(x)
            sine_tone(frequency = x,
                      duration = 0.2,
                      volume=.5,
                      sample_rate = 44100)
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


#test
'''
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=550.00, # Hz, waves per second A4
    duration=3.21, # seconds to play sound
    volume=.5, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
)

'''



#To get to the next tone in the same octave, you must multiply by tr2sqared.
tr2 = 2 ** (1.0/12.0)
tr2sqrd = tr2 * tr2

a = 220 #Note A has frequency of 440Hz.
freqList = [a]
temp = a
#+1 = tone, +0.5 = semi-tone
cMaj = [1,1.5,2.5,3.5,4,5]
for x in cMaj:
    new_note = a * (tr2sqrd ** x)
    freqList.append(int(round(new_note)))
cMaj = freqList
print(cMaj)
playScale(cMaj)
