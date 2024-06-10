import { Cell } from "./Cell";
import { useGameContext } from "./hooks/useGameContext";
import { VisibleBoardRowType } from "./types";

export const Board = () => {
  const { visibleBoard } = useGameContext();

  const Row = ({
    row,
    rowIndex,
  }: {
    row: VisibleBoardRowType;
    rowIndex: number;
  }) =>
    row.map((cellVal, colIndex) => (
      <Cell
        key={`col-${rowIndex}-${colIndex}`}
        value={cellVal}
        index={[rowIndex, colIndex]}
      />
    ));

  return (
    <div>
      {visibleBoard.map((row, rowIndex) => {
        return (
          <div key={`row-${rowIndex}`} style={{ display: "flex" }}>
            <Row row={row} rowIndex={rowIndex} />
          </div>
        );
      })}
    </div>
  );
};
