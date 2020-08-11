def fileNaming(names):
    for i in range(len(names)):
        # print(names[i], names[:i])

        if names[i] in names[:i]:
            j = 1

            while names[i] + '(' + str(j) + ')' in names[:i]:
                j += 1

            names[i] += '(' + str(j) + ')'
            
    return names


