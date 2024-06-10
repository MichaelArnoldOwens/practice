export enum CellType {
  Unmarked = "", // the default
  Mine = "mine",
  Mark = "?",
  Flag = "flag",
  Numberless = "0",
}
// TODO: figure this out later; do we really need these 2 types???
// maybe just need to set values directly
export enum VisibleCellType {
  Unmarked = CellType.Unmarked,
  Mark = CellType.Mark,
  Flag = CellType.Flag,
  Mine = CellType.Mine,
  Numberless = CellType.Numberless,
}

export type BoardDimsType = [number, number];
export type CellIndex = BoardDimsType;
export type Cell =
  | VisibleCellType.Unmarked
  | VisibleCellType.Flag
  | VisibleCellType.Numberless
  | VisibleCellType.Mark
  | VisibleCellType.Mine;
export type VisibleBoardRowType = Cell[];

export type VisibleBoardType = VisibleBoardRowType[];

export type MineSetType = Set<string>;

export interface SettingType {
  boardDims: BoardDimsType;
  numMines: number;
}

export interface DifficultyType {
  EASY: SettingType;
  MEDIUM: SettingType;
  HARD: SettingType;
}
