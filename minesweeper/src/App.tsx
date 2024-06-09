import { Board } from "./Board";
import { DIFFICULTY } from "./constants";

export default function App() {
  return (
    <div>
      <Board difficulty={DIFFICULTY.EASY} />
    </div>
  );
}
