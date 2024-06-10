import { useCallback } from "react";
import { Cell } from "./Cell";
import { useGameContext, useUpdateVisibleBoard } from "./hooks/useGameContext";
import { CellIndex, VisibleBoardRowType } from "./types";

export const Board = () => {
  const { visibleBoard } = useGameContext();
  const updateVisibleBoard = useUpdateVisibleBoard();
  const handleClick = useCallback(
    (index: CellIndex) => () => updateVisibleBoard(index),
    [updateVisibleBoard],
  );

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
        cellIndex={[rowIndex, colIndex]}
        handleClick={handleClick([rowIndex, colIndex])}
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
