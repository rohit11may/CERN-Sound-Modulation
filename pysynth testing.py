import pysynth
from pysynth import mix_files
song1 = (('c', 2), ('e', 4), ('g', 7), ('c5', 1))
song2 = (('c5', 1),  ('g', 4), ('e', 4), ('c', 4))


pysynth.make_wav(song1, fn = "test1.wav")
pysynth.make_wav(song2, fn = "test2.wav")

mix_files("test1.wav", "test2.wav", "test3.wav")