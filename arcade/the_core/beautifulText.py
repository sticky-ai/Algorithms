def beautifulText(inputString, l, r):
    for width in range(l, r+1):
        i = width
        while i < len(inputString):
            if inputString[i] != ' ':
                break
            i += width + 1   
        if i == len(inputString):
            return True
    return False

    # text = inputString.split(' ')
    # widths = [i for i in range(1, 10) if l <= len(inputString) / i <= r]
    # #print(widths)
    
    # ans = []
    # temp = ''
    # for w in widths:
    #     for t in text:
    #         temp += t
    #         temp += ' '
            
    #         if len(temp) <= len(inputString) / w:
    #             continue

    #         else:
    #             temp = temp[:len(temp) - 1]
    #             ans.append(temp)
    #             temp = ''
                
    #     print(ans)

    # print(ans)
    # check1 = [True for i in ans if len(i) == len(ans[0])]
    # check2 = [l <= len(i) <= r for i in ans]
    # print(check1 + check2)
    # return all(check1 + check2)
    

    



    
