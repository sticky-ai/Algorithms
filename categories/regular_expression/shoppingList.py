def shoppingList(items):
    return sum(map(float, re.findall('\d+[.]\d+|\d+', items)))
