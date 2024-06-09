export const cellNumToRowCol = (cellNum: number, boardDims: number[]) => {
  const [_, numCols] = boardDims;
  const rowNum = Math.floor(cellNum / numCols);
  const colNum = (cellNum % numCols) - 1;
  return [rowNum, colNum];
};
