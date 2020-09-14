def shoppingList(i):
    return sum(map(float, re.findall('\d+[.]\d+|\d+', i)))
    
# def shoppingList(items):
#     return sum(map(float, re.findall('\d+[.]\d+|\d+', items)))
    
