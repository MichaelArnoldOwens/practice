// import { CELL_TYPE } from "@/constants";

export const buildBoard = (boardDims) => {
  const [numRows, numCols] = boardDims;
  const result = [];
  for (let i = 0; i < numRows; i++) {
    const newRow = [];
    for (let col = 0; col < numCols; col++) {
      newRow.push(CELL_TYPE.UNMARKED);
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
};

