import { SettingType } from "@/types";
import { buildBoard, cellNumToRowCol, pickRandomMines } from "@/utils/board_utils";

import { useState } from "react";

// import { cellNumToRowCol } from "utils/board_utils";
interface BoardProps {
  difficulty: SettingType;
}

export const Board = ({ difficulty }: BoardProps) => {
  const { boardDims } = difficulty;
  const [mineSet, setMineSet] = useState(pickRandomMines(difficulty));

  return <div style={{ backgroundColor: 'greenyellow' }}>board</div>;
};
