from urllib.parse import urlparse, parse_qs
from itertools import takewhile

def urlSimilarity(url1, url2):
    u1, u2 = [urlparse(u) for u in [url1, url2]]
    p1, p2 = [p.path.split('/')[1:] for p in [u1, u2]]
    q1, q2 = [parse_qs(u) for u in [u1.query, u2.query]]

    score = (u1.scheme == u2.scheme) * 5 + (u1.netloc == u2.netloc) * 10
    score += len(list(takewhile(lambda x: x[0] == x[1], zip(p1, p2))))
    score += sum(2 if q1[q] == q2[q] else 1 for q in q1.keys() & q2.keys())
    return score
