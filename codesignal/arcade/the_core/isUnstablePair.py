def isUnstablePair(filename1, filename2):
    return (filename1.upper() < filename2.upper()) != (filename1 < filename2)
