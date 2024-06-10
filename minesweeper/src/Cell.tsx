import { CSSProperties, memo, useCallback } from "react";
import { CellIndex, VisibleCellType } from "./types";
import { useGameContext } from "./hooks/useGameContext";

interface CellProps {
  value: VisibleCellType;
  index: CellIndex;
}

const styles: CSSProperties = {
  filter: `drop-shadow(
    1px 2px 4px hsl(220deg 60% 50%))`,
  width: 40,
  height: 40,
  backgroundColor: `#d1d1d1`,
  borderWidth: `3px`,
  borderStyle: `solid`,
  borderColor: `white #9e9e9e #9e9e9e white`,
  color: "red",
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  flexWrap: "wrap",
};

const CellComponent = ({ value, index }: CellProps) => {
  const { updateVisibleBoard } = useGameContext();
  const handleClick = useCallback(
    () => updateVisibleBoard(index),
    [index, updateVisibleBoard],
  );
  console.log("rendering cell at:", String(index));
  return (
    <div onClick={handleClick} style={styles}>
      {value}
    </div>
  );
};

export const Cell = memo(CellComponent);
