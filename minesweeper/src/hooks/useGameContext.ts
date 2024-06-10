import { GameContext } from "@/contexts/GameContext";
import { CellIndex } from "@/types";
import { useContext } from "react";

export const useGameContext = () => useContext(GameContext);

export const useGetVisibleBoardValContext = ([row, col]: CellIndex) => {
  const { visibleBoard } = useGameContext();
  return visibleBoard[row][col];
};

export const useUpdateVisibleBoard = () => {
  const { updateVisibleBoard } = useGameContext();
  return updateVisibleBoard;
};
