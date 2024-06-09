import { BoardDimType, CellType, SettingType } from "../types";

export const buildBoard = (boardDims: BoardDimType) => {
  const [numRows, numCols] = boardDims;
  if (numRows === 0 && numCols === 0) {
    throw new Error('must enter valid row and col count')
  }
  const result: CellType[][] = [];
  for (let i = 0; i < numRows; i++) {
    const newRow: CellType[] = [];
    for (let col = 0; col < numCols; col++) {
      newRow.push(CellType.Unmarked);
    }
    result.push(newRow);
  }
  return result;
};

export const pickRandomMines = (difficulty: SettingType) => {
  const result = new Set();
  const { boardDims, numMines } = difficulty;
  const [numRows, numCols] = boardDims;
  const totalCells = numRows * numCols;
  while (result.size < numMines) {
    const candidate = Math.floor(totalCells * Math.random()) + 1;
    if (!result.has(candidate)) {
      result.add(candidate);
    }
  }
  return result
};

export const cellNumToRowCol = (cellNum: number, boardDims: BoardDimType) => {
  const [, numCols] = boardDims;
  const rowNum = Math.floor(cellNum / numCols);

  const remainder = cellNum > numCols ? cellNum - rowNum * numCols : 0

  const colNum = remainder > 0 ? remainder - 1 : cellNum % numCols


  console.log('cell num:', cellNum);
  console.log('rowNum:', rowNum)
  console.log('colNum:', colNum)
  return [rowNum, colNum];
};
