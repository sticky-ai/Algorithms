def knapsackLight(v1, w1, v2, w2, W):
    return max(int(w1 <= W)*v1, int(w2 <= W) *v2, int(w1+w2 <= W) * (v1+v2))
      
