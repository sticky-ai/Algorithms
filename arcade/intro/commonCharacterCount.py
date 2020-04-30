def commonCharacterCount(s1, s2):
    
    lst1 = []
    lst2 = []
    count = 0

    for i in s1:
        lst1.append(ord(i))
    for i in s2:
        lst2.append(ord(i))

    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst2[j] == lst1[i]:
                print(lst2)
                lst2.pop(j)
                count += 1
                break
    return count
