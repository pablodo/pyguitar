notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
notes_len = len(notes)

class Board(object):

    def __init__(self, tuning='EADGBE'):
        self.size = 24
        self.fretboard = self.create_fretboard(tuning)

    def create_fretboard(self, tuning):
        if not tuning or not isinstance(tuning, str):
            raise BadTuningError()

        fretboard = {}
        notes = list(tuning.lower())
        notes.reverse()
        octaves = [4,3,3,3,2,2]
        for note in range(len(notes)):
            fretboard[str(note + 1)] = {'note': notes[note],
                                        'octave': octaves[note]}
        return fretboard

    def get_note(self, string, fret):
        if not isinstance(string, str):
            string = str(string)
        if not string in self.fretboard or not fret:
            raise StringNotInBoardError(string, self.fretboard.keys())

        octave = self.fretboard[string]['octave']
        string_note = self.fretboard[string]['note']

        note_index = notes.index(string_note)
        while note_index + fret >= notes_len:
            note_index -= notes_len
            octave += 1 
        note = notes[note_index + fret]
        return note, octave

    def find_note(self, note, octave):
        if not note in notes:
            raise NoteNotFoundError()

        results = [] 
        note_index = notes.index(note.lower())
        for string, v in self.fretboard.iteritems():
            tune_note_index = notes.index(v['note'])
            if octave > v['octave'] or (octave == v['octave'] and note_index >= tune_note_index):
                fret = (octave - v['octave']) * notes_len
                diff =  note_index - tune_note_index
                fret += diff
                results.append((string, fret))
        return results

    def draw(self, scale):
        lines = "-" * 4 + "|"  
        for i in range(1, self.size + 1):
            lines += " %-2d|" % i
        lines += "\n"

        for string in sorted(self.fretboard.keys()):
            line = string + "(" + self.fretboard[string]['note'] + ")|"

            for i in range(1, self.size + 1):
                note, octave = self.get_note(string, i) 
                if note in scale:
                    line += " %-2s" % note
                else:
                    line += "   "
                if i <= self.size:
                    line += "|"
            lines += line + "\n"
        return lines

class BadTuningError(Exception):
    pass


class StringNotInBoardError(Exception):

    def __init__(self, string, strings):
        self.string = string
        self.strings = strings

    def __str__(self):
        return "The string %s not found in %s" % (self.string, self.strings) 

class NoteNotFoundError(Exception):
    pass
