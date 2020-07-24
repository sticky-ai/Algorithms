def buildPalindrome(st):
    if st == st[::-1]: return st
    
    for i in range(len(st) + 1): 
        temp = st + st[:i][::-1] 
        if temp == temp[::-1]:
            return tempdef buildPalindrome(st):
    l = len(st)
    st = list(st)
    for v in st:
        if st == st[::-1]:
            return ''.join(st)
        st.insert(l, v)
