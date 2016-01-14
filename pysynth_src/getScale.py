from pysynth_src import notedict

notes = notedict.notes
notes_reverse = dict(zip(notes.values(), notes.keys()))


def getScale(key):
    key = notes_reverse[key]
    general_rule = [2, 2, 1, 2, 2, 2, 1]
    scale = []
    start = 0
    for x in range(7):
        scale.append(notes[key])
        if x == 6:
            break
        else:
            key += general_rule[start]
            start += 1
    return scale



