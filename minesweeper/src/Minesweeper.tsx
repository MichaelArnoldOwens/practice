import { SettingType } from "@/types";

import { GameContextProvider } from "./contexts/GameContext";
import { Board } from "./Board";

interface BoardProps {
  difficulty: SettingType;
}

export const Minesweeper = ({ difficulty }: BoardProps) => {
  return (
    <GameContextProvider difficulty={difficulty}>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          backgroundColor: "greenyellow",
          height: "100vh",
        }}
      >
        <Board />
      </div>
    </GameContextProvider>
  );
};
