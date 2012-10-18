import notes

Major = [2,2,1,2,2,2,1]
Minor = [2,1,2,2,1,2,2]
ArmonicMinor = [2,1,2,2,1,3,1]
Pentatonic = [3,2,2,3,2]

scales = {'major': Major, 
          'minor': Minor, 
          'armonic_minor': ArmonicMinor, 
          'pentatonic': Pentatonic}

def make_scale(tonic, mode):
    scale = [tonic]
    index = 0
    for tone in mode:
        note_index = notes.notes.index(scale[index])
        note = notes.notes[(note_index + tone) - notes.notes_len]
        scale.append(note)
        index += 1
    return scale

