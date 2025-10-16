import { createContext, useContext, useState } from "react";

const KeypadContext = createContext();

export const KeypadProvider = ({ children }) => {
  const [activeInput, setActiveInput] = useState(null);

  return (
    <KeypadContext.Provider value={{ activeInput, setActiveInput }}>
      {children}
    </KeypadContext.Provider>
  );
};

export const useKeypad = () => useContext(KeypadContext);