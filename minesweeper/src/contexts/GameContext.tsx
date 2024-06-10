import { CellIndex, MineSetType, SettingType, VisibleBoardType } from "@/types";
import {
  buildBoard,
  copyVisibleBoard,
  getNextCellType,
  pickRandomMines,
} from "@/utils/board_utils";
import {
  ReactNode,
  useState,
  createContext,
  useMemo,
  useCallback,
} from "react";

interface GameContextType {
  visibleBoard: VisibleBoardType;
  mineSet: MineSetType;
  updateVisibleBoard: (cell: CellIndex) => void;
}

export const GameContext = createContext<GameContextType>({
  visibleBoard: [],
  mineSet: new Set(),
  updateVisibleBoard: () => {},
});

interface GameContextProviderProps {
  children: ReactNode;
  difficulty: SettingType;
}

export const GameContextProvider = ({
  children,
  difficulty,
}: GameContextProviderProps) => {
  const { boardDims } = difficulty;
  const [visibleBoard, setVisibleBoard] = useState<VisibleBoardType>(
    buildBoard(boardDims),
  );
  const [mineSet] = useState<MineSetType>(pickRandomMines(difficulty));

  const updateVisibleBoard = useCallback(
    (cell: CellIndex) => {
      setVisibleBoard((prevBoard) => {
        const newBoard = copyVisibleBoard(prevBoard);
        const [row, col] = cell;
        const currCellType = newBoard[row][col];
        newBoard[row][col] = getNextCellType(currCellType);
        return newBoard;
      });
    },
    [setVisibleBoard],
  );

  const gameContextState = useMemo(() => {
    return { visibleBoard, mineSet, updateVisibleBoard };
  }, [mineSet, visibleBoard, updateVisibleBoard]);

  return (
    <GameContext.Provider value={gameContextState}>
      {children}
    </GameContext.Provider>
  );
};

// type BoardContextType = VisibleBoardType;
// export const BoardContext = createContext<BoardContextType>([]);
// export const BoardContextProvider = () => {
//   const [visibleBoard, setVisibleBoard] = useState<VisibleBoardType>(
//     buildBoard(boardDims),
//   );
// };
