import { BoardDimType, CellType, SettingType } from "@/types";
import { buildBoard, cellNumToRowCol, pickRandomMines } from "@/utils/board_utils";

import { useState } from "react";

// import { cellNumToRowCol } from "utils/board_utils";
interface BoardProps {
  difficulty: SettingType;
}

export const Board = ({ difficulty }: BoardProps) => {
  const { boardDims } = difficulty;
  const [visibleBoard, setVisibleBoard] = useState(buildBoard(boardDims));
  // cellNumToRowCol

  const cell8loc = cellNumToRowCol(8, boardDims);
  console.log('cell8loc', cell8loc)

  const [mineSet, setMineSet] = useState(pickRandomMines(difficulty));
  return <div style={{ backgroundColor: 'greenyellow' }}>board</div>;
};
