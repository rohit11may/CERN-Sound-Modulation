import pysynth
test = ( ('c', 4), ('e', 4), ('g', 4), ('c5', 1))
pysynth.make_wav(test, fn = "test.wav")
