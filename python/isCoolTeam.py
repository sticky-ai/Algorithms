from collections import Counter

class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        names = [lower(i) for i in self.names]
        first = Counter([i[0] for i in names])
        last = Counter([i[-1] for i in names])
        
def isCoolTeam(team):
    return bool(Team(team))

