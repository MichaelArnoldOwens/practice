export enum CellType {
  Unmarked, // the default
  Mine,
  Mark,
  Flag,
  Numberless,
}

export type BoardDimsType = number[];
export type CellIndex = BoardDimsType;
export type Cell =
  | CellType.Unmarked
  | CellType.Mine
  | CellType.Flag
  | CellType.Numberless
  | CellType.Mark;
export type VisibleBoardRowType = Cell[];

export type VisibleBoardType = VisibleBoardRowType[];

export type MineSetType = Set<number>;

export interface SettingType {
  boardDims: BoardDimsType;
  numMines: number;
}

export interface DifficultyType {
  EASY: SettingType;
  MEDIUM: SettingType;
  HARD: SettingType;
}
