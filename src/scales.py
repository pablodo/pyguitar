import notes

Major = [2,2,1,2,2,2,1]
Minor = [2,1,2,2,1,2,2]
ArmonicMinor = [2,1,2,2,1,3,1]

def make_scale(tonic, mode):
    scale = [tonic]
    index = 0
    for tone in mode:
        note_index = notes.notes.index(scale[index])
        note = notes.notes[(note_index + tone) - notes.notes_len]
        scale.append(note)
        index += 1
    return scale

C = make_scale('c', Major)
D = make_scale('d', Major)
E = make_scale('e', Major)
F = make_scale('f', Major)
G = make_scale('g', Major)
A = make_scale('a', Major)
B = make_scale('b', Major)
Cm = make_scale('c', Minor)
Dm = make_scale('d', Minor)
Em = make_scale('e', Minor)
Fm = make_scale('f', Minor)
Gm = make_scale('g', Minor)
Am = make_scale('a', Minor)
Bm = make_scale('b', Minor)
ArmonicA = make_scale('a', ArmonicMinor)

