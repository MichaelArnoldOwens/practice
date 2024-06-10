import { Minesweeper } from "./Minesweeper";
import { DIFFICULTY } from "./constants";

export default function App() {
  return (
    <div>
      <Minesweeper difficulty={DIFFICULTY.EASY} />
    </div>
  );
}
