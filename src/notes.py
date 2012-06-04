fretboard = {'6': {'note':  'e',
                   'octave': 2 },
             '5': {'note':  'a',
                   'octave': 2 },
             '4': {'note':  'd',
                   'octave': 3 },
             '3': {'note':  'g',
                   'octave': 3 },
             '2': {'note':  'b',
                   'octave': 3 },
             '1': {'note':  'e',
                   'octave': 4 }}
notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
notes_len = len(notes)

def get_note_from_fretboard(string, fret):
    if type(string) != type(str):
        string = str(string)

    if not string in fretboard:
        raise Exception("The string is wrong. The accepted strings are " +  str(fretboard.keys()))

    octave      = fretboard[string]['octave']
    string_note = fretboard[string]['note']
    if not string_note in notes:
        raise Exception("The note doesn't exists")

    note_index = notes.index(string_note)
    try:
        while note_index + fret >= len(notes):
            note_index -= len(notes)
            octave     += 1 
        note = notes[note_index + fret]
        return note, octave
    except Exception:
        print("string: " + string)
        print("fret: " + str(fret))
        print("string note: " + string_note)

def get_frets_from_note(note, octave):
    if not note in notes:
        raise Exception("The note doesn't exists")

    frets = [] 
    for k, v in fretboard.iteritems():
        note_index = notes.index(note)
        tune_note_index = notes.index(v['note'])
        if octave > v['octave'] or (octave == v['octave'] and note_index >= tune_note_index):
            fret = (octave - v['octave']) * notes_len
            diff =  note_index - tune_note_index
            fret += diff
            frets.append((k, fret))
    return frets
