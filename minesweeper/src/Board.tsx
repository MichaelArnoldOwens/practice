import { SettingType } from "@/types";

import { GameContextProvider } from "./contexts/GameContext";

interface BoardProps {
  difficulty: SettingType;
}

export const Board = ({ difficulty }: BoardProps) => {

  return <GameContextProvider difficulty={difficulty}><div style={{ backgroundColor: 'greenyellow' }}>board</div></GameContextProvider>
};
