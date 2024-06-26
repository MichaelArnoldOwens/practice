import { CSSProperties, memo } from "react";
import { VisibleCellType } from "./types";

interface CellProps {
  value: VisibleCellType;
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

const CellComponent = ({ value }: CellProps) => {
  return <div style={styles}>{value}</div>;
};

export const Cell = memo(CellComponent);
