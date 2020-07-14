def buildPalindrome(st):
    l = len(st)
    st = list(st)
    for v in st:
        if st == st[::-1]:
            return ''.join(st)
        st.insert(l, v)
