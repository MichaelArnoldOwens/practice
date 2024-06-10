import { CSSProperties, memo, useCallback } from "react";
import { CellIndex, VisibleCellType } from "./types";
import { useGetVisibleBoardValContext } from "./hooks/useGameContext";
import { copyVisibleBoard } from "./utils/board_utils";

interface CellProps {
  value: VisibleCellType;
  handleClick: () => void;
}

const styles: CSSProperties = {
  cursor: "pointer",
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

const CellComponent = ({ handleClick, cellIndex }: CellProps) => {
  // TODO: All Cell are re-rendering on click
  const value = useGetVisibleBoardValContext(cellIndex);
  console.log("rendering cell value:", value);
  return (
    <div onClick={handleClick} style={styles}>
      {value}
    </div>
  );
};

export const Cell = memo(CellComponent);
