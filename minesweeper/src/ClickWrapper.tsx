import { MouseEventHandler, ReactNode } from "react";

interface ClickWrapperProps {
  children: ReactNode;
  handleClick: MouseEventHandler;
}

export const ClickWrapper = ({ children, handleClick }: ClickWrapperProps) => {
  return <div onClick={handleClick}>{children}</div>;
};
