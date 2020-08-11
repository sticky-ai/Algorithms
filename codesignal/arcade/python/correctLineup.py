from itertools import chain

def correctLineup(athletes):
    return list(chain(*[i[::-1] for i in zip(athletes[::2], athletes[1::2])]))

