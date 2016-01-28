from dataGenerate import getValues
from pysynth_src.getScale import getScale

scale = getScale('c4')
print(scale)
noteNum, duration = getValues()

song = []

for note, length in zip(noteNum, duration):
    noteNum = scale[note-1]
    if length == 0:
        noteNum = 'r'
        length = 1
    noteA = noteNum
    song.append((noteA, length))

song = tuple(song)
print(song)

