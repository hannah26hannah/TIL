import React, { useRef } from 'react';

const MyComponent = () => {
  const id = useRef(1);
  const setId = (n) => {
    id.current = n;
  };
  const printId = () => {
    console.log(id.current);
  };

  return (
    <div>
      Ref Sample<button onClick={printId}>콘솔로그</button>
    </div>
  );
};
export default MyComponent;
