def beautifulText(inputString, l, r):      
    strings = inputString.split(' ')
    length = len(inputString)
    div_min, div_max = length // r, length // l
    
    for i in range(div_min, div_max + 1):
        temp_str = ''
        temp_list = []
        s_len = int((length - i + 1) / i)
        for s in strings:
            temp_str += s
            if len(temp_str) == s_len:
                temp_list.append(temp_str)
                temp_str = ''
            else:
                temp_str += ' '
        
        if ' '.join(temp_list) == inputString:
            if l <= len(temp_list[0]) <= r:
                return True
    return False
