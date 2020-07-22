def matrixElementsInSpiralOrder(m):
   return m and [*m.pop(0)] + matrixElementsInSpiralOrder([*zip(*m)][::-1])
