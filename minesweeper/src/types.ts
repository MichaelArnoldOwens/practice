export enum CellType {
  Unmarked,
  Mine,
  Mark,
  Flag,
}

export type BoardDimType = number[];
export type CellIndex = BoardDimType;

export interface SettingType {
  boardDims: BoardDimType;
  numMines: number;
}

export interface DifficultyType {
  EASY: SettingType;
  MEDIUM: SettingType;
  HARD: SettingType;
}


