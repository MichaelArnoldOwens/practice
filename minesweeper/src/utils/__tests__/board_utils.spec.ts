import {
  BoardDimsType,
  CellType,
  SettingType,
  VisibleBoardRowType,
  VisibleBoardType,
  VisibleCellType,
} from "@/types";
import {
  buildBoard,
  pickRandomMines,
  cellNumToRowColIndex,
  rowColIndexToCellNum,
  copyVisibleBoard,
  mineSetValToBoardDim,
  getNextCellType,
} from "@/utils/board_utils";

describe("buildBoard", () => {
  it("should initialize an Unmarked board", () => {
    const [row, col] = [2, 3];
    const board = buildBoard([row, col]);
    expect(board.length).toBe(row);
    expect(board[0].length).toBe(col);
  });
  it("should throw error when initialized with 0 row and col", () => {
    expect(() => buildBoard([0, 0])).toThrow(
      "must enter valid row and col count",
    );
  });
});

describe("pickRandomMines", () => {
  it("should return a set of random mines equal to the count of the difficulty", () => {
    const difficulty: SettingType = { numMines: 10, boardDims: [9, 9] };
    const randomMines = pickRandomMines(difficulty);
    expect(randomMines.size).toBe(difficulty.numMines);
  });
  it("should store values that can be converted to an array", () => {
    const difficulty: SettingType = { numMines: 10, boardDims: [9, 9] };
    const randomMines = pickRandomMines(difficulty);
    const result = [];
    for (const mineStr of randomMines) {
      result.push(mineSetValToBoardDim(mineStr));
    }
    for (const cellIndex of result) {
      expect(cellIndex.length === 2);
    }
    expect(randomMines.size).toBe(difficulty.numMines);
  });
});

describe("mineSetValToBoardDim", () => {
  it("should convert mine set value to a board dim", () => {
    expect(mineSetValToBoardDim("1,1")).toEqual([1, 1]);
    expect(mineSetValToBoardDim("2,1")).toEqual([2, 1]);
    expect(mineSetValToBoardDim("2,1,4")).toEqual([2, 1, 4]);
  });
});

describe("cellNumToRowColIndex", () => {
  it("should return the row and col num given a cell number", () => {
    const boardDims: BoardDimsType = [9, 9];
    let result = cellNumToRowColIndex(80, boardDims);
    expect(result).toEqual([8, 7]);

    result = cellNumToRowColIndex(5, boardDims);
    expect(result).toEqual([0, 4]);

    result = cellNumToRowColIndex(12, boardDims);
    expect(result).toEqual([1, 2]);

    result = cellNumToRowColIndex(1, boardDims);
    expect(result).toEqual([0, 0]);

    result = cellNumToRowColIndex(1, boardDims);
    expect(result).toEqual([0, 0]);

    result = cellNumToRowColIndex(9, boardDims);
    expect(result).toEqual([0, 8]);
  });
});

describe("rowColIndexToCellNum", () => {
  it("should return a cell number", () => {
    const boardDims: BoardDimsType = [9, 9];
    let result = rowColIndexToCellNum([0, 0], boardDims);
    expect(result).toBe(1);

    result = rowColIndexToCellNum([1, 0], boardDims);
    expect(result).toBe(10);

    result = rowColIndexToCellNum([1, 4], boardDims);
    expect(result).toBe(14);

    result = rowColIndexToCellNum([8, 8], boardDims);
    expect(result).toBe(81);
  });
});

describe("copyVisibleBoard", () => {
  it("should copy a 2d array and not give a ref", () => {
    const original: VisibleBoardType = [
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15],
    ].map((x) => x.map(() => CellType.Unmarked));

    const copy: VisibleBoardType = copyVisibleBoard(original);
    expect(copy).toEqual(original);

    original[0] = original[0].map(() => CellType.Mark);
    expect(original[0]).toEqual([
      CellType.Mark,
      CellType.Mark,
      CellType.Mark,
      CellType.Mark,
      CellType.Mark,
    ]);

    expect(copy).not.toEqual(original);
    copy[0] = copy[0].map(() => CellType.Numberless) as VisibleBoardRowType;
    expect(copy[0]).toEqual([
      CellType.Numberless,
      CellType.Numberless,
      CellType.Numberless,
      CellType.Numberless,
      CellType.Numberless,
    ]);
  });
});

describe("getNextCellType", () => {
  it("returns unmarked when passed mark", () => {
    expect(getNextCellType(VisibleCellType.Mark)).toBe(CellType.Unmarked);
  });
  it("returns unmarked when passed mark", () => {
    expect(getNextCellType(VisibleCellType.Unmarked)).toBe(CellType.Flag);
  });
  it("returns unmarked when passed mark", () => {
    expect(getNextCellType(VisibleCellType.Flag)).toBe(CellType.Mark);
  });
});
