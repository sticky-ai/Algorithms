def bishopDiagonal(b1, b2):
    b1, b2 = [ord(i) for i in b1], [ord(i) for i in b2]
    if abs(b1[0]-b2[0])==abs(b1[1]-b2[1]):
        if b1[0]<b2[0]:
            if b1[1]<b2[1]: 
                while b1[0]>97 and b1[1]>49: b1[0], b1[1] = b1[0]-1, b1[1]-1
                while b2[0]<104 and b2[1]<56: b2[0], b2[1] = b2[0]+1, b2[1]+1
            else:
                while b1[0]>97 and b1[1]<56: b1[0], b1[1] = b1[0]-1, b1[1]+1
                while b2[0]<104 and b2[1]>49: b2[0], b2[1] = b2[0]+1, b2[1]-1
        else:
            if b1[1]<b2[1]: 
                while b1[0]<104 and b1[1]>49: b1[0], b1[1] = b1[0]+1, b1[1]-1
                while b2[0]>97 and b2[1]<56: b2[0], b2[1] = b2[0]-1, b2[1]+1
            else:
                while b1[0]<104 and b1[1]<56: b1[0], b1[1] = b1[0]+1, b1[1]+1
                while b2[0]>97 and b2[1]>49: b2[0], b2[1] = b2[0]-1, b2[1]-1
    return sorted(["".join([chr(b1[0]),chr(b1[1])]),"".join([chr(b2[0]),chr(b2[1])])])
