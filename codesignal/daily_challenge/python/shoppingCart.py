from collections import defaultdict as D

def shoppingCart(requests):   
    d = D(int) 
    f = lambda x: x.split(' : ')
    
    for r in requests:
        if f(r)[0] == 'quantity_upd':
            o, p, n = r.split(' : ')
            d[p] += int(n)
        
        elif f(r)[0] == 'checkout':
            d = D(int)
            
        else:
            o, p = f(r)
            if o == 'add':
                d[p] = 1
            
            elif o == 'remove':
                del d[p]
                            
    return [k + ' : ' + str(v) for k, v in d.items()]
        
        
            
        
