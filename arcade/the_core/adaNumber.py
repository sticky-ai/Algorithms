import re
rx = re.compile(r'^(?:(\d+)#([\da-fA-F]+)#|(\d+))$')

def adaNumber(line):
    m = rx.search(line.replace('_', ''))
    if m:
        try:
            if m.group(3):
                int(m.group(3))
                return True
            
            base = int(m.group(1) or 10)
            if 2 <= base <= 16:
                int(m.group(2), base)
                return True
            
        except ValueError:
            pass
    return False
