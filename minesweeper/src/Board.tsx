import { Cell } from "./Cell";
import { useGameContext, useUpdateVisibleBoard } from "./hooks/useGameContext";
import { ClickWrapper } from "./ClickWrapper";

export const Board = () => {
  const { visibleBoard } = useGameContext();
  const updateVisibleBoard = useUpdateVisibleBoard();
  const handleClick = (row: number, col: number) => () =>
    updateVisibleBoard([row, col]);

  return (
    <div>
      {visibleBoard.map((row, rowIndex) => {
        return (
          <div key={`row-${rowIndex}`} style={{ display: "flex" }}>
            {row.map((cellVal, colIndex) => {
              return (
                <ClickWrapper
                  key={`col-${rowIndex}-${colIndex}`}
                  handleClick={handleClick(rowIndex, colIndex)}
                >
                  <Cell value={cellVal} />
                </ClickWrapper>
              );
            })}
          </div>
        );
      })}
    </div>
  );
};
