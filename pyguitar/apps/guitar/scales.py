from board import notes, notes_len

major = [2,2,1,2,2,2,1]
minor = [2,1,2,2,1,2,2]
armonic_minor = [2,1,2,2,1,3,1]
pentatonic = [3,2,2,3,2]

scales = {'major': major, 
          'minor': minor, 
          'armonic_minor': armonic_minor, 
          'pentatonic': pentatonic}


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
