import scales
import notes


'''
string = input("Insert the string number\n")
fret = input("Insert the fret number\n")
print(get_note_from_fretboard(string, fret))
'''
'''
note  = input("Insert the note\n")
octave = input("Insert the octave\n")
print(get_frets_from_note(note, octave))
'''

def print_board(scale):
    line = "-" * 4 + "|"  
    for i in range(1,24):
        line += " %-2d|" % i
    print line

    for string in sorted(notes.fretboard.keys()):
        line = string + "(" + notes.fretboard[string]['note'] + ")|"

        for i in range(1,24):
            note, octave = notes.get_note_from_fretboard(string, i) 
            if note in scale:
                line += " %-2s" % note
            else:
                line += "   "
            if i < 24:
                line += "|"
        print(line)

def print_board_2():
    line = "-" * 4 + "|"  
    for i in range(1,24):
        line += " %-2d " % i
    print line
    for string in sorted(notes.fretboard.keys()):
        line = string + "(" + notes.fretboard[string]['note'] + ")|"
        for i in range(1,24):
            note, octave = notes.get_note_from_fretboard(string, i) 
            line += " %-2s" % note
            if i < 23:
                line += "-"
        print(line)

while True:
    try:
        note = raw_input("Insert a note\n")
        scale = raw_input("Insert an scale\n")
        if not isinstance(note, str):
            note = str(note)
        if not isinstance(scale, str):
            scale = str(scale)
        scale_notes = scales.make_scale(note, scales.scales[scale])
        print_board(scale_notes)
    except KeyboardInterrupt:
        print "\nBye"
        break
