import { SettingType } from "@/types";
import {
  buildBoard,
  pickRandomMines,
  cellNumToRowColIndex,
  rowColIndexToCellNum,
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
});

describe("cellNumToRowColIndex", () => {
  it("should return the row and col num given a cell number", () => {
    const boardDims = [9, 9];
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
    const boardDims = [9, 9];
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
