def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
  rowSize, colSize = len(mat), len(mat[0])
        
  if rowSize * colSize != r*c:
    return mat
    result = []

    row_so_far = []
    for row in range(rowSize):
      for col in range(colSize):
        row_so_far.append(mat[row][col])
        if len(row_so_far) == c:
          result.append(row_so_far[:])
          row_so_far = []
  return result
      
