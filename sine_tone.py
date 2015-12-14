"""Play a fixed frequency sound."""
from __future__ import division
import math
from pyaudio import PyAudio

def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in range(n_samples))
    for buf in zip(*[samples]*sample_rate): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()

sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=550.00, # Hz, waves per second A4
    duration=3.21, # seconds to play sound
    volume=.5, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
)
