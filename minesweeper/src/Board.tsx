import { Cell } from "./Cell";
import { useGameContext } from "./hooks/useGameContext";
import { VisibleBoardRowType } from "./types";

export const Board = () => {
  const { visibleBoard } = useGameContext();

  const Row = ({ row }: { row: VisibleBoardRowType }) =>
    row.map((cellVal, colIndex) => (
      <Cell key={`col-${colIndex}`} value={cellVal} />
    ));

  return (
    <div>
      {visibleBoard.map((row, rowIndex) => {
        return (
          <div key={`row-${rowIndex}`} style={{ display: "flex" }}>
            <Row row={row} />
          </div>
        );
      })}
    </div>
  );
};
