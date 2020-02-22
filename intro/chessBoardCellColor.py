def chessBoardCellColor(cell1, cell2):
    alpha_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num_lst = ['1', '2', '3', '4', '5', '6', '7', '8']

    color = []

    c1 = [alpha_lst.index(cell1[0])+1, num_lst.index(cell1[1])+1]
    c2 = [alpha_lst.index(cell2[0])+1, num_lst.index(cell2[1])+1]

    return (c1[0] + c1[1]) % 2 == (c2[0] + c2[1]) % 2


