def stolenLunch(note):
    num, letter = '0123456789', 'abcdefghij'
    return note.translate(str.maketrans(num+letter, letter+num))
