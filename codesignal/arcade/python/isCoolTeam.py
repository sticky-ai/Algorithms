class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        names = list(map(lambda x: x.lower(), self.names))

        def is_chain(name, others):
            if others == []: return True

            firsts, lasts = [], []
            for x in others:
                firsts.append(x[0])
                lasts.append(x[-1])
    
            ends = 0

            for x in set(firsts + lasts):
                ends += abs(firsts.count(x) - lasts.count(x))
                print(x, ends)
            if ends not in [0, 2]: return False

            return any(is_chain(n, others[:i] + others[i+1:]) for i, n in enumerate(others) if n[0] == name[-1])

        return any(is_chain(n, names[:i] + names[i+1:]) for i, n in enumerate(names))
        

def isCoolTeam(team):
    return bool(Team(team))

