def sortByString(s, t):
    s_list = [c for c in s]
    my_dict = {c : i for i, c in enumerate(t)}
    ans = sorted(s_list, key=my_dict.get)
    return ''.join(ans)
