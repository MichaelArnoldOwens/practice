import { CSSProperties, memo, useMemo } from "react";
import { Cell as CellType, VisibleCellType } from "./types";
import { useGetVisibleBoardValContext } from "./hooks/useGameContext";

interface CellProps {
  value: VisibleCellType;
  handleClick: (row: number, col: number) => void;
  rowIndex: number;
  colIndex: number;
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

const CellComponent = ({ handleClick, rowIndex, colIndex }: CellProps) => {
  // TODO: All Cell are re-rendering on click
  const value: CellType = useGetVisibleBoardValContext([rowIndex, colIndex]);
  const memoValue: CellType = useMemo(() => value, [value]);
  console.log("rendering cell value:", value);
  return (
    <div onClick={() => handleClick(rowIndex, colIndex)} style={styles}>
      {memoValue}
    </div>
  );
};

export const Cell = memo(CellComponent, (prevProps, nextProps) => {
  console.log(
    `[${prevProps.rowIndex}, ${prevProps.colIndex}]`,
    "are equal:",
    prevProps.value === nextProps.value &&
      prevProps.rowIndex === nextProps.rowIndex &&
      prevProps.colIndex === nextProps.colIndex,
  );
  return (
    prevProps.value === nextProps.value &&
    prevProps.rowIndex === nextProps.rowIndex &&
    prevProps.colIndex === nextProps.colIndex
  );
});
