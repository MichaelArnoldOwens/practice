import React, { useState } from "react";
import { CELL_TYPE } from "./constants";
import { SettingType } from "./constants";
import { cellNumToRowCol } from "./utils";

interface BoardProps {
  difficulty: SettingType;
}

export const buildBoard = (boardDims: number[]) => {
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

export const Board = ({ difficulty }: BoardProps) => {
  const { boardDims } = difficulty;
  const [visibleBoard, setVisibleBoard] = useState(buildBoard(boardDims));
  // cellNumToRowCol

  const cell8loc = cellNumToRowCol(8, boardDims);

  const [mineSet, setMineSet] = useState(pickRandomMines(difficulty));
  return <div>board</div>;
};
