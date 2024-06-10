import { DifficultyType } from "@/types";

export const DIFFICULTY: DifficultyType = {
  TEST: { boardDims: [1, 2], numMines: 1 },
  EASY: { boardDims: [9, 9], numMines: 10 },
  MEDIUM: { boardDims: [16, 16], numMines: 40 },
  HARD: { boardDims: [30, 16], numMines: 99 },
};
