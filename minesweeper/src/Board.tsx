import { useCallback } from "react";
import { Cell } from "./Cell";
import { useGameContext, useUpdateVisibleBoard } from "./hooks/useGameContext";

export const Board = () => {
  const { visibleBoard } = useGameContext();
  const updateVisibleBoard = useUpdateVisibleBoard();
  const handleClick = useCallback(
    (row: number, col: number) => updateVisibleBoard([row, col]),
    [updateVisibleBoard],
  );

  return (
    <div>
      {visibleBoard.map((row, rowIndex) => {
        return (
          <div key={`row-${rowIndex}`} style={{ display: "flex" }}>
            {row.map((cellVal, colIndex) => {
              return (
                <Cell
                  key={`col-${rowIndex}-${colIndex}`}
                  value={cellVal}
                  rowIndex={rowIndex}
                  colIndex={colIndex}
                  handleClick={handleClick}
                />
              );
            })}
          </div>
        );
      })}
    </div>
  );
};
