import React, { useReducer } from 'react';

function reducer(state, action) {
  switch (action.type) {
    case 'INCREMENT':
      return { value: state.value + 1 };
    case 'DECREMENT':
      return { value: state.value - 1 };
    default:
      return state; // 아무것도 해당되지 않을 때는 기존 state를 그대로 반환한다.
  }
}
const Counter = () => {
  const [state, dispatch] = useReducer(reducer, { value: 0 });

  return (
    <main>
      <p>현재 카운터 값 : {state.value}</p>
      <button onClick={() => dispatch({ type: 'INCREMENT' })}>+1</button>
      <button onClick={() => dispatch({ type: 'DECREMENT' })}>-1</button>
    </main>
  );
};
export default Counter;
