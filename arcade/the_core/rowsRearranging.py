def rowsRearranging(matrix):
    return all(list(sorted(set(c))) == list(c) for c in zip(*sorted(matrix)))
            
        
