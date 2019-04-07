from isChord import isChord, isChordLine

# , isChordLine

NOTES = ["C", "D", "E", "F", "G", "A", "B"]


def minor(chord):
    return chord + "m"


def test_blank():
    assert not isChord("")


def test_basic():
    for note in NOTES:
        assert isChord(note)
        assert isChord(minor(note))

        sharp = note + "#"
        flat = note + "b"
        assert isChord(sharp)
        assert isChord(flat)
        assert isChord(minor(sharp))
        assert isChord(minor(flat))


def test_lines():
    shortLine = "A C"
    assert isChordLine(shortLine)
    notQuiteChords = "A carrot"
    assert not isChordLine(notQuiteChords)
    line = "Dm       C              Dm      C     Dm   C"
    assert isChordLine(line)


def test_false_matches():
    test = "Apple"
    assert not isChord(test)


# These chords are so fancy~


def test_chord_with_underscore():
    line = "Dm_1 Caug_22222"
    assert isChordLine(line)


def test_complex_chords():
    complexChords = ["Cmaj7", "Caug", "Bbsus2", "Dbdim", "Gadd9", "Dm", "Emadd9"]
    for chord in complexChords:
        assert isChord(chord), chord

    line = " ".join(complexChords)

    assert isChordLine(line)


def test_no_note():
    # Because ukuleles don't have enough strings
    assert isChordLine("A7no3")
