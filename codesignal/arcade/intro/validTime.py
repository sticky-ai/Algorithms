def validTime(time):
        h, m = time.split(':')
        if int(h) >= 24 or int(m) >= 60: return False
        else: return True

