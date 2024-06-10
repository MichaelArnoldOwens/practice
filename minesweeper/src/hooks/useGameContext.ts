import { GameContext } from "@/contexts/GameContext";
import { useContext } from "react";

export const useGameContext = () => useContext(GameContext);
