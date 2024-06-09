import { BoardDimType, CellIndex, CellType, SettingType } from "../types";

export const buildBoard = (boardDims: BoardDimType) => {
  const [numRows, numCols] = boardDims;
  if (numRows === 0 && numCols === 0) {
    throw new Error("must enter valid row and col count");
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
  return result;
};

export const cellNumToRowColIndex = (
  cellNum: number,
  boardDims: BoardDimType,
) => {
  const [, numCols] = boardDims;
  const cellIndex = cellNum - 1;
  const rowNum = Math.floor(cellIndex / numCols);
  const remainder = cellNum > numCols ? cellNum - rowNum * numCols : 0;
  const colNum = remainder > 0 ? remainder - 1 : cellIndex;

  return [rowNum, colNum];
};

export const rowColIndexToCellNum = (
  cellIndex: CellIndex,
  boardDims: BoardDimType,
) => {
  const [, numCols] = boardDims;
  const [rowIndex, colIndex] = cellIndex;

  return rowIndex * numCols + colIndex + 1;
};
