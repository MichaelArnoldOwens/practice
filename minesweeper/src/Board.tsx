import { useCallback } from "react";
import { Cell } from "./Cell";
import { useGameContext, useUpdateVisibleBoard } from "./hooks/useGameContext";
import { CellIndex } from "./types";

export const Board = () => {
  const { visibleBoard } = useGameContext();
  const updateVisibleBoard = useUpdateVisibleBoard();
  const handleClick = useCallback(
    (index: CellIndex) => () => updateVisibleBoard(index),
    [updateVisibleBoard],
  );

  return (
    <div>
      {visibleBoard.map((row, rowIndex) => {
        return (
          <div key={`row-${rowIndex}`} style={{ display: "flex" }}>
            {row.map((cellVal, colIndex) => (
              <Cell
                key={`col-${rowIndex}-${colIndex}`}
                value={cellVal}
                cellIndex={[rowIndex, colIndex]}
                handleClick={handleClick([rowIndex, colIndex])}
              />
            ))}
          </div>
        );
      })}
    </div>
  );
};
