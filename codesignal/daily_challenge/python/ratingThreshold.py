t, r = eval(dir()[0])
return [r.index(i) for i in r if numpy.mean(i) < t]


# 115 chars
# def ratingThreshold(threshold, ratings):
#     return [i for i in range(len(ratings)) if sum(ratings[i]) / len(ratings[i]) < threshold]
    
