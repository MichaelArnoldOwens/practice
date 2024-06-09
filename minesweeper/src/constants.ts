export enum CELL_TYPE {
  UNMARKED,
  MINE,
  MARK,
  FLAG,
}

export interface SettingType {
  boardDims: number[];
  numMines: number;
}

export interface DifficultyType {
  EASY: SettingType;
  MEDIUM: SettingType;
  HARD: SettingType;
}

export const DIFFICULTY: DifficultyType = {
  EASY: { boardDims: [9, 9], numMines: 10 },
  MEDIUM: { boardDims: [16, 16], numMines: 40 },
  HARD: { boardDims: [30, 16], numMines: 99 },
};

console.log("constants:");
console.log(CELL_TYPE.MINE);
console.log(CELL_TYPE.FLAG);
