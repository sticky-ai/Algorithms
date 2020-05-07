from collections import defaultdict as ddict

def solution(genres, plays):
    dic = ddict(list)
    for g, p in zip(genres, plays):
        dic[g].append(p)
    #print(dic)
    
    rank_genres = sorted(dic.keys(), key=lambda x: sum(dic[x]), reverse = True)
    
    dic_2 = ddict(list)
    for idx, (g, p) in enumerate(zip(genres, plays)):
        dic_2[g].append([idx, p])
    
    answer = []
    cnt = 0
    for g in rank_genres:
        if len(dic[g]) == 1:
            answer.append(dic[g][0][0])
        else:
            for i in sorted(dic_2[g], key=lambda x: x[1], reverse = True)[:2]:
                answer.append(i[0])
                
    return answer
            
                
        
        
