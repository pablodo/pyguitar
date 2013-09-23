from board import notes, notes_len

Major = [2,2,1,2,2,2,1]
Minor = [2,1,2,2,1,2,2]
ArmonicMinor = [2,1,2,2,1,3,1]
Pentatonic = [3,2,2,3,2]

scales = {'major': Major, 
          'minor': Minor, 
          'armonic_minor': ArmonicMinor, 
          'pentatonic': Pentatonic}


def make_scale(tonic, scale):
    if not scale in scales:
        raise ScaleNotFoundError()

    scale_notes = [tonic]
    index = 0
    for tone in scales[scale.lower()]:
        note_index = notes.index(scale_notes[index])
        note = notes[(note_index + tone) - notes_len]
        scale_notes.append(note)
        index += 1
    return scale_notes

class ScaleNotFoundError(Exception):
    pass
