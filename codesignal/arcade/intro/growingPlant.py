def growingPlant(upSpeed, downSpeed, desiredHeight):
    grown = 0
    count = 0
    
    while(1):
        grown += upSpeed
        
        if grown < desiredHeight:
            grown -= downSpeed
            count += 1
            
        else:
            return count+1
        
