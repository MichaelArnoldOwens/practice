import {
  BoardDimsType,
  CellIndex,
  CellType,
  VisibleCellType,
  SettingType,
  VisibleBoardRowType,
  VisibleBoardType,
} from "@/types";

export const buildBoard = (boardDims: BoardDimsType) => {
  const [numRows, numCols] = boardDims;
  if (numRows === 0 && numCols === 0) {
    throw new Error("must enter valid row and col count");
  }
  const result: VisibleBoardType = [];
  for (let i = 0; i < numRows; i++) {
    const newRow: VisibleBoardRowType = [];
    for (let col = 0; col < numCols; col++) {
      newRow.push(CellType.Unmarked);
    }
    result.push(newRow);
  }
  return result;
};

export const pickRandomMines = (difficulty: SettingType): Set<string> => {
  const result: Set<string> = new Set();
  const { boardDims, numMines } = difficulty;
  const [numRows, numCols] = boardDims;
  const totalCells = numRows * numCols;
  while (result.size < numMines) {
    const candidateCellNum = Math.floor(totalCells * Math.random()) + 1;
    const candidate = String(
      cellNumToRowColIndex(candidateCellNum, difficulty.boardDims),
    );
    if (!result.has(candidate)) {
      result.add(candidate);
    }
  }
  return result;
};

export const mineSetValToBoardDim = (mineVal: string) => {
  return mineVal.split(",").map(Number);
};

export const cellNumToRowColIndex = (
  cellNum: number,
  boardDims: BoardDimsType,
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
  boardDims: BoardDimsType,
) => {
  const [, numCols] = boardDims;
  const [rowIndex, colIndex] = cellIndex;

  return rowIndex * numCols + colIndex + 1;
};

// TODO: make the arg generic for any 2D array
export const copyVisibleBoard = (board: VisibleBoardType): VisibleBoardType => {
  return board.map((row) => row.slice());
};

const cellTypeOrder: Record<string, VisibleCellType> = {
  [VisibleCellType.Mark]: VisibleCellType.Unmarked,
  [VisibleCellType.Unmarked]: VisibleCellType.Flag,
  [VisibleCellType.Flag]: VisibleCellType.Mark,
};

export const getNextCellType = (cell: VisibleCellType) => cellTypeOrder[cell];
