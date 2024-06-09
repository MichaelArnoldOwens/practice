import { BoardDimsType, MineSetType, SettingType, VisibleBoardType } from "@/types";
import { buildBoard, pickRandomMines } from "@/utils/board_utils";
import { ReactNode, useState, createContext, useMemo } from "react";

interface GameContextType {
  visibleBoard: VisibleBoardType,
  mineSet: MineSetType
}

const GameContext = createContext<GameContextType>({ visibleBoard: [], mineSet: new Set() })


interface GameContextProviderProps {
  children: ReactNode
  boardDims: BoardDimsType
  difficulty: SettingType
}

export const GameContextProvider = ({ children, boardDims, difficulty }: GameContextProviderProps) => {
  const [visibleBoard, setVisibleBoard] = useState<VisibleBoardType>(buildBoard(boardDims))
  const [mineSet, setMineSet] = useState<MineSetType>(pickRandomMines(difficulty))

  const gameContextState = useMemo(() => {
    return { visibleBoard, mineSet }
  }, [mineSet, visibleBoard])

  return <GameContext.Provider value={gameContextState}>{children}</GameContext.Provider>
}
