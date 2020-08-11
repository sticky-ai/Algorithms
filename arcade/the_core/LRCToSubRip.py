def lrc2subRip(lrcLyrics, songLength):
    def timeConvert(time):
        mm, ss, xx = map(int, re.split(r":|\.", time))
        hh = mm / 60
        mm %= 60
        return "%02d:%02d:%02d,%03d" % (hh, mm, ss, xx*10)

    ans = []
    for k, line in enumerate(lrcLyrics):
        t = timeConvert(line[1:9])
        if ans: ans[-3] += " --> " + t
        ans.extend([str(k+1), t, line[11:], ""])
    if ans: ans[-3] += " --> " + songLength + ",000"
    return ans[:-1]

