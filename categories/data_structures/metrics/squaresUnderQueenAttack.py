import numpy as np
def squaresUnderQueenAttack(n, queens, queries):
    m = np.array(range(n ** 2)).reshape(n, n)
    for q in queens:
        for i in range(n):
            for j in range(n):
                if m[j][i] in np.diag(m, k=q[1] - q[0]):
                    m[j][i] = 9999
                if m[j][i] in np.diag(np.fliplr(m), k= 2 - q[0] if q[0] > 2 else 1 + q[0]):
                    m[j][i] = 9999
    
        for i in range(n):
            m[q[0]][i] = 9999
            m[i][q[1]] = 9999
        
    ans = []
    for x, y in queries:
        if m[x][y] == 9999:
            ans.append(True)
        else:
            ans.append(False)
    return ans
        
        
    #np.fill_diagonal(m, True)
    #np.fill_diagonal(np.fliplr(m), True)
    
    # def get_horizon_vertical_pos(n, queens):
    #     h = [[queens[0], i] for i in range(n)]
    #     v = [[i, queens[1]] for i in range(n)]
    #     return h + v
